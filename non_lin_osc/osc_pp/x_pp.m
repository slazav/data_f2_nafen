% find equilibrium (zero of x_pp_eq function)
function [x y] = x_pp(w,w0,d,a,b,g)
  x0 = [0.1, 0.1];
  maxamp = g/w0/d;

  for i=1:length(w)
    f = @(x) x_pp_eq(x,w(i),w0,d,a,b,g);
    x0 = fsolve(f, x0);
    x(i) = x0(1);
    y(i) = x0(2);
%    fprintf('%f %f %f\n', w(i), x0);
  end
end
