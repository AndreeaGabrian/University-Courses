using System;

namespace rt
{
    public class Sphere : Geometry
    {
        private Vector Center { get; set; }
        private double Radius { get; set; }

        public Sphere(Vector center, double radius, Material material, Color color) : base(material, color)
        {
            Center = center;
            Radius = radius;
        }

        public override Intersection GetIntersection(Line line, double minDist, double maxDist)
        {
            // ADD CODE HERE: Calculate the intersection between the given line and this sphere
            // THIS COMMENTED SECTION WAS THE FIRST ATTEMP DONE COMPONENT BY COMPONENT. iT WORKS AND I WILL LEAVE IT HERE
            // AS MORE DETAILED EXPLICATION ON HOW THIS STUFF WORKS

            // line equation                         sphere equation
            //x = x1 + t*(x2 - x1)                   (x-xc)^2+(y-yc)^2+(z-zc)^2=r^2,  where center of spehere is (xc,yc,zc) and radius r
            //y = y1 + t*(y2 - y1)
            //z = z1 + t*(z2 - z1)
            //we want to find t
            //double x1=line.X0.X;   //coordinates of first point from line equation P(x1,y1,z1)
            //double y1=line.X0.Y;   
            //double z1=line.X0.Z;

            //double dx=line.Dx.X;   //(dx,dy,dx) = (x2-x1,y2-y1,z2-z1)
            //double dy=line.Dx.Y;
            //double dz=line.Dx.Z;

            //double xc=Center.X;
            //double yc=Center.Y;
            //double zc=Center.Z;

            //substituting line equations into sphere eq will result in a quadratic eq A*t^2+B*t+C=0
            //double A = dx*dx+dy*dy+dz*dz;
            //double B = 2*(dx*(x1-xc)+dy*(y1-yc)+dz*(z1-zc));
            //double B = 2*(dx*(x1-xc)+dy*(y1-yc)+dz*(z1-zc));
            //double C = xc*xc + yc*yc + zc*zc + x1*x1 + y1*y1 + z1*z1 -2*(xc*x1+yc*y1+zc*z1) - Radius*Radius;

            bool valid, visible;
            Vector X = line.X0;
            Vector dX = line.Dx;
            
            double A = dX.Length2();
            double B = 2*(dX*(X-Center));
            double C = Center.Length2() + X.Length2() - 2*(Center*X) - Radius*Radius;
            double delta = B*B - 4*A*C;
            double t=0;

            if(delta>=0){
                 double t1 = (-B - System.Math.Sqrt(delta)) / (2.0 * A);
                 double t2 = (-B + System.Math.Sqrt(delta)) / (2.0 * A);

                 if(t1>minDist && t1<maxDist)
                 {
                    if(t2>minDist && t2<maxDist)
                    {
                        if(t1<t2)
                        {
                            t=t1;
                        }
                        else
                        {
                            t=t2;
                        }
                    }
                 }
                 else if(t2>minDist && t2<maxDist)
                 {
                    t=t2;
                 }
                 visible = true;
                 valid = true;
                 return new Intersection(valid, visible, this, line, t);
                
            }
            
            return new Intersection();
        }

        public override Vector Normal(Vector v)
        {
            var n = v - Center;
            n.Normalize();
            return n;
        }
    }
}