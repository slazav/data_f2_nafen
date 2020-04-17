% Equilibriun function of Psudoplastic oscillator
% at periodic drive.
% a - power of viscosity law
%
function f = x_pp_eq(uv,w,w0,d,a,b,g)
 u = uv(1);
 v = uv(2);

 p = 2*pi*(0:0.01:1);
 x = u*cos(p)-v*sin(p);
 dx = w*(-u*sin(p)-v*cos(p));

 ddx = g*cos(p) - d*dx./(1 + a*abs(dx)) - w0^2*x;

 f(1) = -trapz(p, (ddx + w^2*x).*sin(p))/w;
 f(2) = -trapz(p, (ddx + w^2*x).*cos(p))/w;
end
