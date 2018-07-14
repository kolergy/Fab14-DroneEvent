q = 10;      // Quality factor of the render
 
hi =  100;  // Hight of the side wall
th =    2;  // Wall thickness
wi = 1500;  // Track widith
wm = 1000;
ti =  500;  // Tile dimentions

// Generate a corner with the folowing parameters(re:external radius, w:widith, a: angle)
module corner(re,w,a) { 
    translate([0,w, 0]) rotate([0,0,-90]) {
            color("LemonChiffon") rotate_extrude(angle=a, convexity = 10, $fn=10*q)
        translate([re, 0, 0]) {
            square([th,hi]);
            translate([-w, 0, 0]) square([th,hi]);
        }
        color("darkslategrey") rotate_extrude(angle=a, convexity = 10, $fn=10*q)
        translate([re, 0, 0]) {
            translate([-w, 0])square([w,0.1]);
        }
        color("white") rotate_extrude(angle=a, convexity = 10, $fn=10*q)
        translate([re, 0, 0.2]) {
            translate([-w/2-20, 0])square([20,0.2]);
        }
    }
}

module line(le, w, a){
    rotate([0,0,a]) {
        color("LemonChiffon") translate([0, 0, 0]) cube([le,th,hi]);
        color("darkslategrey") translate([0, 0, 0]) cube([le,w,0.1]);
        color("LemonChiffon") translate([0,w, 0]) cube([le,th,hi]);
        color("white") translate([0, w/2-10, 0.2]) cube([le,20,0.2]);
    }
}

module arrow(le) color("blue") {
    translate([le/2,0,0]) cylinder(d=le/2, h=le/10, center=true, $fn=3);
    cube([le*3/4, le/6, le/10], center = true);
    }

module start(w) {
    for (i=[0:100:400]) {
        for (j=[-w:200:-100]) {
            if (i==0 || i==200 || i== 400) { translate([i, j, 0.2]) cube([100,100, 0.2]);}
            else { translate([i, j+100, 0.2]) cube([100,100, 0.2]);}
        }
    }
}

module conv(le, w1, w2, o, a){
    f=1.5;
    rotate([0,0,a]) {
        a1 = atan(o/le);
        l1 = le / cos(a1);
        o2 = -w1 + w2 + o;
        a2 = atan(o2/le);
        l2 = le / cos(a2);
        ra = w2/w1;
        color("blue") translate([0, 0, 0]) rotate([0, 0, a1]) cube([l1,th,hi]);
        color("blue") translate([0,w1, 0]) rotate([0, 0, a2]) cube([l2,th,hi]);
        color("darkslategrey") translate([0,o*f, 0]) rotate([0,90,0])     linear_extrude(height = le, convexity = 10, scale=[1,ra], $fn=10*q)
            translate([0,-o*f, 0])
            square([th,w1]);
    }
}

module mediatheque() {
     color("brown") difference() {
        translate([ 0,  0, 0]) cube([500, 2000, 1000]);
        translate([-1,490,-10]) cube([502, 1020, 510]);
        }
     color("Silver") translate([-250,0,1000]) cube([750, 2000, 5]);
    }
    
module marteuleur() {
    //translate([0,0,-10]) cube([500,500,1000]);
    translate([250,250,40]) import("Mateleur_v1.stl");
}

module gateA(wi,hi) color("green") {
    translate([   0,-30, 0]) cube([30,30,hi]);
    translate([   0, wi, 0]) cube([30,30,hi]);
    translate([   0,-30,hi]) cube([30,wi+30,30]);
    translate([-250,-30, 0]) cube([500,30,30]);
    translate([-250, wi, 0]) cube([500,30,30]);
}
module gateB(wi,hi) color("green") {
    translate([   0, wi, 0]) cube([30,30,hi]);
    translate([   0,-30,hi]) cube([30,wi+30,30]);
    translate([-250, wi, 0]) cube([500,30,30]);
}
module gateC(wi,hi) color("green") {
    translate([   0, wi, 0]) cube([30,30,hi]);
    translate([   0,-30,hi]) cube([30,wi+30,30]);
    translate([0, wi-250, 0]) cube([30,500,30]);
}
module gateD(wi,hi) color("green") {
    translate([   0, wi, 0]) cube([30,30,hi]);
    translate([   0,-30,hi]) cube([30,wi+30,30]);
}
//module gateB(wi,hi, hi2) color("green") {
//    gateA(wi,hi);
//    translate([   0,-30,hi2]) cube([30,wi+30,30]);
//}

module fence(hi, li) color("green") {
    translate([ 0,   0,0]) cylinder(d=100, h=hi+hi/2);
    translate([ 0,   0,0]) cube([li,5,hi]);
    translate([li,   0,0]) cylinder(d=100, h=hi);
    translate([li,-500,0]) cube([30,1000,30]);
}

module building(hi)  {
    color("grey") translate([0,0,0]) cube([500,500,hi]);
    }

color("darkslategrey") translate([0,0,-2]) cube([12000,6000,1]);   // Race area
translate([ 1527, 500,0]) line(6473, wm,0);
translate([ 8000,3000,0]) corner(3500, wm,90);
translate([11000,4000,0]) rotate([0,0, 90])    corner(1500, wm,  90);
translate([10000,5500,0]) rotate([0,0,180])    corner(1000, wm,  75);
translate([ 9035,4760,0]) rotate([0,0,180+75]) line(  2000, wm,   0);
translate([ 9385,2599,0]) rotate([0,0, 75])    corner(1100, wm,-190);
translate([ 6515,3742,0]) rotate([0,0, 65])    corner(3000, wm,  40);
translate([ 8410,4915,0]) rotate([0,0, 65+40]) corner(1100, wm, 180);
translate([ 5415,4115,0]) rotate([0,0,105])    corner(3000, wm, -30);
translate([ 7300,3099,0]) rotate([0,0,105-30]) corner(1050, wm,-100);
translate([ 2520,3980,0]) rotate([0,0,-25])    line(  3720, wm,   0); // Diag Straight
translate([ 2530,4980,0]) rotate([0,0,180])    corner(1000, wm, -25);
translate([ 2530,4980,0]) rotate([0,0,180])    line(  1000, wm,   0);
translate([ 1530,4980,0]) rotate([0,0,180])    corner(1000, wm,  90);
translate([  527,3980,0]) rotate([0,0,-90])    line(  2480, wm,   0);
translate([  527,1500,0]) rotate([0,0,-90])    corner(1000, wm,  90);
translate([ 4500,1500,0]) start(wm);
translate([ 6500,1000,0]) arrow(wm);

translate([ 3000,   0,   0]) mediatheque();
translate([ 3000,1500,1006]) start(wm);
translate([ 6800,2200,   0]) rotate([0,0,-15]) marteuleur();
translate([ 8000, 200,   0]) rotate([0,0,  0]) gateA(wm+ 500,2000);
translate([11500,4900,   0]) rotate([0,0,120]) gateA(wm+ 500,2000,1000);
translate([10150,4150,   0]) rotate([0,0, 55]) gateB(wm+ 500,2000,1000);
translate([ 8000,1700,   0]) rotate([0,0,-20]) gateC(wm+ 500,2000,1000);
translate([ 8900,5000,   0]) rotate([0,0,115]) gateD(wm+ 500,2000,1000);
translate([ 7500,4400,   0]) rotate([0,0, 55]) gateB(wm+ 500,2000,1000);
translate([ 6100,2200,   0]) rotate([0,0,  0]) gateA(wm+ 500,1500,1000);
translate([ 1800,3700,   0]) rotate([0,0, 45]) gateA(wm+ 500,1000,1000);
translate([ 700,  700,   0]) rotate([0,0,-45]) gateA(wm+ 500,2000,1000);
translate([3250,    0,   0]) rotate([0,0,  0]) gateA(wm+1000,2000,1000);
//translate([ 8400,2850,   0]) rotate([0,0, 75]) fence(1500, 2900);

translate([   0,   0,0]) building(430);
translate([   0, 500,0]) building(1000);
translate([   0,1100,0]) building(800);
translate([   0,1600,0]) building(1000);
translate([   0,2500,0]) building(1200);
translate([   0,3100,0]) building(430);
translate([   0,3600,0]) building(800);
translate([   0,4800,0]) building(1000);
translate([ 400,5500,0]) building(430);
translate([1000,5500,0]) building(1000);
translate([3200,4850,0]) rotate([0,0,-25]) building(430);
translate([4800,4100,0]) rotate([0,0,-25]) building(1000);
translate([4000,4500,0]) rotate([0,0,-25]) building(800);
