% Equilibriun function of a non-linear oscillator
% at periodic drive.
%
% u,v - van der Pol coordinates (x,x' rotated by w*t)
% w - frequency
% func - second derivative function, x'' = func(phase, x, x')
%
% Coordinated are averaged over rotation period (phase 0..2*pi)
% Output is u' and v',  they should be zero in equilibrium.
%
% See text in http://www.scholarpedia.org/article/Duffing_oscillator
%
function f = nonlin_osc_eq(uv,w,func)
 u = uv(1);
 v = uv(2);

 p = 2*pi*(0:0.01:1); % phase for integration
 x = u*cos(p)-v*sin(p);
 dx = w*(-u*sin(p)-v*cos(p));
 ddx = func(p,x,dx);

 f(1) = -trapz(p, (ddx + w^2*x).*sin(p))/w;
 f(2) = -trapz(p, (ddx + w^2*x).*cos(p))/w;
end
