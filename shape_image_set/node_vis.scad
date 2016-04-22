s = 10;
h = 20;

translate([-s/2*10,-s/2*10,-h/2])
for(i=[0:s-1],j=[0:s-1],k=[0:1]){translate([i*10,j*10,k*h])color("blue")sphere(2,center=true);
    for(a=[10:10],b=[10:10])
    synapse(0,0,i*10,j*10);
    }

module synapse (x1,y1,x2,y2)
{
$fn=3;

l=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)+h*h);
l1=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));

angle = atan2((y2-y1),(x2-x1));
angle2 = atan2(h,l1);

color("red")
translate([(x2-x1)/2,(y2-y1)/2,h/2])

rotate([0,90-angle2,angle])
cylinder(l,r=.25,center=true);
}