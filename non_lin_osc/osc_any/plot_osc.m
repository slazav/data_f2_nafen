function plot_osc()

  w0 = 1;
  d = 0.2;
  g = 2.5;
  a = 0.05;
  b = 0;
  w = 0.1:0.01:2;


  find_figure('pp'); clf; hold on;

  for g=[1 2 3]

    % harmonic oscillator
%    func = @(p,x,dx) g*cos(p) -d*dx - w0^2*x;

    % duffing oscillator
    % it's hard to find equilibrium properly
%    func = @(p,x,dx)  g*cos(p) - d*dx - w0^2*x - 0.0025*x.^3;

    % pseudoplastic osc
    func = @(p,x,dx) g*sin(p) - d*dx./(1 + a*abs(dx)) - w0^2*x;

    % pseudoplastic osc
    func = @(p,x,dx) g*sin(p) - d*dx./(1 + a*abs(dx)) - w0^2*x;

    % mass change
    func = @(p,x,dx) g*sin(p) - d*dx - w0^2*x.*(1 + 0.003*dx.^2);

    x = nonlin_osc(w,func, [0.1 0.1]);

    plot(w,hypot(x(:,1),x(:,2))/g, 'g.-');
    plot(w,atan2(x(:,2),x(:,1)), 'r.-');
  end

end

