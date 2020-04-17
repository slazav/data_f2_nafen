% find equilibrium (zero of x_duff_eq function)
function [x y] = x_duff1(w,w0,d,a,g)
  maxamp = g/w0/d;
  for i=1:length(w)
    f = @(x) x_duff_eq(x,w(i),w0,d,a,g);
    [x0(1) x0(2)] = x_harm(w(i),w0,d,g);
    x0 = fsolve(f, x0);
    x(i) = x0(1);
    y(i) = x0(2);
    fprintf('%f %f %f\n', w(i), x0);
  end
end
