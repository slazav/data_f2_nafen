function plot_duff2()

  w0 = 1;
  d = 0.2;
  g = 2.5;
  a = -0.002;
  a = 0.03;


  find_figure('duff'); clf; hold on;

  w = 0.5:0.01:2;

  [x y] = x_duff2(w,w0,d,a,g);
  plot(w,hypot(x,y), 'g.-');
  plot(w,atan2(y,x), 'r.-');

  w = 2:-0.01:0.5;

  [x y] = x_duff2(w,w0,d,a,g);
  plot(w,hypot(x,y), 'g.-');
  plot(w,atan2(y,x), 'r.-');



end

