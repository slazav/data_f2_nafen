% find equilibrium (zero of x_duff_eq function)
function [x y] = x_duff2(w,w0,d,a,g)
  x = zeros(size(w));
  y = zeros(size(w));
  x0=[0 0];
  for i=1:length(w)
%    [x0(1) x0(2)] = x_harm(w(i),w0,d,g);
    f = @(x) x_duff_eq(x,w(i),w0,d,a,g);
%    x0 = fsolve(f, x0, optimset('ComplexEqn', 'on'));
    for j=1:10000
      dx = f(x0);
      dd = abs(dx);
      x0 += dx*2*pi/w(i)/100;
      if (dd < 1e-8) break; end
      if (isnan(dx)); break; end
    end
    if (isnan(x0)); break; end
    x(i) = x0(1);
    y(i) = x0(2);
    fprintf('%f %f %f\n', w(i), x0);
  end
end
