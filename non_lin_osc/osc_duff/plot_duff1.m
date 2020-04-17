function plot_duff1()

  w0 = 1;
  d = 0.2;
  g = 2.5;
  a = -0.002;
  a = 0.03;


  find_figure('duff'); clf; hold on;

  w = 0.1:0.01:2;

  [x y] = x_duff1(w,w0,d,a,g);
  plot(w,hypot(x,y), 'g.-');
  plot(w,atan2(y,x), 'r.-');

  w = 2:-0.01:0.1;

  [x y] = x_duff1(w,w0,d,a,g);
  plot(w,hypot(x,y), 'g.-');
  plot(w,atan2(y,x), 'r.-');

  [x y] = x_harm(w,w0,d,g);
  plot(w,hypot(x,y), 'b--');
  plot(w,atan2(y,x), 'b--');



end

