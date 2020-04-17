% Equilibriun function of Duffing oscillator
% at periodic drive.
% see http://www.scholarpedia.org/article/Duffing_oscillator
#
function f = x_duff_eq(uv,w,w0,d,a,g)
 u = uv(1);
 v = uv(2);
 if (1)
   p = 2*pi*(0:0.01:1);
   x = u*cos(p)-v*sin(p);
   dx = w*(-u*sin(p)-v*cos(p));
   ddx = g*cos(p) - d*dx - w0^2*x - a*x.^3;

   f(1) = -trapz(p, (ddx + w^2*x).*sin(p))/w;
   f(2) = -trapz(p, (ddx + w^2*x).*cos(p))/w;
 else
   f(1) = (-w*d*u + (w^2-w0^2)*v - 3/4.0*a*(u^2+v^2)*v)/2/w;
   f(2) = (-w*d*v - (w^2-w0^2)*u + 3/4.0*a*(u^2+v^2)*u - g)/2/w;
 end
end
