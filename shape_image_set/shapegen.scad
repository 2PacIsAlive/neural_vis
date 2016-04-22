//
//
//
n = 3;
s = 0;
l = "a";
rs = rands(4,25,1);
rx = rands(-30,30,1);
ry = rands(-30,30,1);
rz = rands(0,360,1);
tx = rands(-10,10,1);
ty = rands(-10,10,1);

if(s){
rs = rands(4,10,1);
rotate(concat(rx,ry,rz))
translate(concat(tx,ty))
circle(rs[0],$fn=n);}

else{
rs = rands(4,25,1);
rotate(concat(rx,ry,0))
translate(concat(tx,ty))
text(l,rs[0],valign="center",halign="center");}
