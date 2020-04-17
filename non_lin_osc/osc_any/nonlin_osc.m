% find equilibrium (zero of nonlin_osc_eq function)
function uv = nonlin_osc(w,func, uv0)
  for i=1:length(w)
    f = @(uv) nonlin_osc_eq(uv,w(i),func);
    uv0 = fsolve(f, uv0);
    uv(i,:) = uv0;
  end
end
