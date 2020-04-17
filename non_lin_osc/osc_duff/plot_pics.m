function plot_pics()

  w0 = 1;
  d = 0.2;
  g = 2.5;
  a = -0.002;
  a = 0.03;

  find_figure('duff-pot');
  for w = 0.1:0.1:2.5
    clf; hold on;
    [xx, yy] = meshgrid (-10:0.5:10);
    for x = 1:length(xx(:,1))
      for y = 1:length(yy(1,:))
        f = x_duff_eq([xx(x,y) yy(x,y)],w,w0,d,a,g);
        dx(x,y) = f(1);
        dy(x,y) = f(2);
      end
    end
    dd = hypot(dx,dy);
    quiver(xx,yy, dx./dd, dy./dd);
    xlim([-10 10]);
    ylim([-10 10]);

    [x,y] = x_duff1(w,w0,d,a,g);
    plot(x, y, 'r*')

%    x = x_duff2(w,w0,d,a,g);
%    plot(real(x), imag(x), 'go')

    print('-dpng', sprintf('pic%3.1f.png', w));
  end

end

