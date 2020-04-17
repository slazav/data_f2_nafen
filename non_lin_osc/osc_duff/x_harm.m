% equilibrium for harmonic oscillator, use for initial conditions
function [x y] = x_harm(w,w0,d,g)
  x = - (w.^2-w0^2)*g./((w.^2-w0^2).^2 + (w*d).^2);
  y = - w*d*g./((w.^2-w0^2).^2 + (w*d).^2);
end
