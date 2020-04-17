function plot_pp()

  w0 = 1;
  d = 1;
  g = 2.5;
  a = 0.2;
  b = 0;


  find_figure('pp'); clf; hold on;

  for g=[1 2 3]
    w = 0.1:0.01:2;

    [x y] = x_pp(w,w0,d,a,b,g);

    plot(w,x/g, 'g.-');
    plot(w,y/g, 'r.-');
  end

%  [x y] = x_harm(w,w0,d,g);
%  plot(w,hypot(x,y), 'b--');
%  plot(w,atan2(y,x), 'b--');




end

