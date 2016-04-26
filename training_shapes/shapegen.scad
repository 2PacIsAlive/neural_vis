
rs = rands(4,10,1);

rx = rands(-30,30,1);
ry = rands(-30,30,1);
rz = rands(0,360,1);
tx = rands(-13,13,1);
ty = rands(-13,13,1);

rotate(concat(rx,ry,rz))
translate(concat(tx,ty))

circle(rs[0],$fn=n);