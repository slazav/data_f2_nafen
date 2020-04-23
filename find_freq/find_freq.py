# functions for finding signal frequency

import numpy
from math import pi,hypot

###################################

# fft maximum
def find_freq_fft(T,A):
  if T.size!=A.size:
    raise ValueError("T and A arrays have different number of points")

  N = T.size - 1
  tstep = (T[-1]-T[0])/(T.size-1)

  fft = numpy.fft.fft(A)
  fft[0] = 0  # remove constant component
  f_ind = numpy.argmax(numpy.abs(fft[0:int(N/2)]))

  return f_ind / tstep / (N+1), fft, f_ind

###################################

# fit fft maximum by 3-point parabola
def find_freq_fftfit_q(T,A):
  freq, fft, f_ind = find_freq_fft(T,A)
  v1 = abs(fft[f_ind-1])
  v2 = abs(fft[f_ind])
  v3 = abs(fft[f_ind+1])
  di = -(v3-v1)/(v1 - 2*v2 + v3)/2
  return freq*(1 + di/f_ind)

###################################

# fit fft near maximum
def find_freq_fftfit_l(T,A):

  freq1, fft1, f_ind1 = find_freq_fft(T,A)

  # Now we should solve problem with too "pure"
  # signals where we have maxinun and zeros near it.

  # we want to remove k points to shift
  # fft node by 1/2 near the resonance i:
  #  i - i (n-k)/n = 1/2,
  #  k = 1/2 n/i,
  N = T.size
  k = int(N/2/f_ind1)

  freq2, fft2, f_ind2 = find_freq_fft(T[0:-k],A[0:-k])

  # choose signal with smaller maximum
  # larger side points:
  if abs(fft1[f_ind1]) > abs(fft2[f_ind2]):
    freq = freq2
    fft = fft2
    f_ind = f_ind2
  else:
    freq = freq1
    fft = fft1
    f_ind = f_ind1

  # fft is proportional to 1/(f-f0)
  # We want to fit 1/fft it with linear function A*x+B
  # and find zero crossing (-B/A)
  # As usual, we minimize  S = sum (a*x +b - y)^2
  # Differentiating by A and B we have
  # A*sum(x*x) + B*sum(x) - sum(y*x) =  0
  # A*sum(x) + B*sum(w) - sum(y) =  0

  # Solving this we have:
  # B = [sum(y*x)*sum(x) - sum(y)*sum(x*x)]/[sum(x)*sum(x) - sum(1)*sum(x*x)]
  # A = [sum(y)*sum(x) - sum(y*x)*sum(1)]/[sum(x)*sum(x) - sum(1)*sum(x*x)]
  # x0 = -B/A = (sum(y*x)*sum(x) - sum(y)*sum(x*x)) / (sum(y*x)*sum(1) - sum(y)*sum(x))

  # it's good to fit in a very narrow window, because 1/fft is very noisy far from f0
  ind_win = 2 #
  sn = 0
  sx = 0
  sy = 0
  sxx = 0
  sxy = 0
  for x in range(-ind_win, +ind_win+1):
    if fft[f_ind + x]==0: continue
    y = numpy.real(1/fft[f_ind + x])
    w = 1/y**2 # Very strong weighting function
    sn  += w
    sx  += x*w
    sy  += y*w
    sxx += x*x*w
    sxy += x*y*w

  di = (sxy*sx-sy*sxx)/(sxy*sn-sy*sx)
  # Another approach, much less accurate:
  # v1 = fft[f_ind-1]
  # v2 = fft[f_ind]
  # v3 = fft[f_ind+1]
  # f_indm = f_ind - (v3-v1)/(v1 - 2*v2 + v3)/2

  return freq*(1 + di/f_ind)

###################################

# one more approach: we calculate "slow" Furier at some frequency F and 
# then maximize its value as a function of F

from scipy.integrate import trapz
from scipy.optimize import minimize

def find_freq_fmax(T,A):

  # initial frequency value:
  freq, fft, f_ind = find_freq_fft(T,A)

  def minfunc(freq, T,A):
    Sin = numpy.sin(2*pi*freq*T)
    Cos = numpy.cos(2*pi*freq*T)
    X = trapz(Cos*A, T)
    Y = trapz(Sin*A, T)
    return -hypot(X,Y)

  res = minimize(minfunc, freq, (T,A),
    options={'disp': False, 'maxiter': 1000})
  return numpy.array(res.x)
