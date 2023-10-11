using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices;
using System.Threading;

namespace rt
{
    class RayTracer
    {
        public RayTracer()
        {
        }

        private double ImageToViewPlane(int n, int imgSize, double viewPlaneSize)
        {
            var u = n * viewPlaneSize / imgSize;
            u -= viewPlaneSize / 2;
            return u;
        }

        private int[,,] ReadData()
        {
            //for the head
             // int xMax = 181;
             // int yMax = 217;
             // int zMax = 181;
             // string filename = "head-181x217x181.dat";
            
            //for the vertebra
            int xMax = 47;
            int yMax = 512;
            int zMax = 512;
            string filename = "vertebra-47x512x512.dat";
            
            int[,,] array3D = new int[xMax, yMax, zMax];
            byte[] data = File.ReadAllBytes(filename);
                var i = 0;
                for (int x = 0; x < xMax; x++)
                {
                    for (int y = 0; y < yMax; y++)
                    {
                        for (int z = 0; z < zMax; z++)
                        {
                            array3D[x, y, z] = data[i];
                            i++;
                        }
                    }
                }

                return array3D;
        }

        public Color ComputeColorsHead(int value)
        {

            if (value < 45)
            {
                return new Color(0, 0, 0, 1);
            }

            if (value < 70)
            {
                return new Color(0, 0, 1, 0.3);
            }

            if (value < 100)
            {
                return new Color(0.49, 0.17, 0.63, 0.4);
            }

            if (value < 140)
            {
                return new Color(1, 0, 0, 0.3);
            }

            if (value < 180)
            {
                return new Color(0, 1, 0, 0.2);
            }

            if (value < 210)
            {
                return new Color(0.72, 0.81, 0.015, 0.27);
            }

            else
            {
                return new Color(0.17, 0.63, 0.59, 0.2);
            }
        }
        
        public Color ComputeColorsVertebra(int value)
        {

            if (value < 10)
            {
                return new Color(0, 0, 0, 1);
            }

            else
            {
                return new Color(value/255.0, 0, 0, 0.3);
            }
        }

        private Boolean IsInside(Vector position, int xMax, int yMax, int zMax)
        {
            if (position.X <= xMax && position.X >= 0 &&
                position.Y <= yMax && position.Y >= 0 &&
                position.Z <= zMax && position.Z >= 0)
            {
                return true;
            }

            return false;
        }


        public void Render(Camera camera, int width, int height, string filename)
        {
            var background = new Color(0,0,0,1);
            var image = new Image(width, height);
            var values = ReadData();
            
            for (var i = 0; i < width; i++)
            {
                for (var j = 0; j < height; j++)
                {
                    // ADD CODE HERE: Implement pixel color calculation
                    Vector x1 = camera.Position + camera.Direction*camera.ViewPlaneDistance +
                                camera.Up*ImageToViewPlane(j,height,camera.ViewPlaneHeight) +
                                (camera.Up^camera.Direction)*ImageToViewPlane(i, width, camera.ViewPlaneWidth);
                    Line line = new Line(camera.Position, x1);

                    var resultColor = new Color();
                    var Alpha = 0.0;
                    var exitFromCube = false;
                    var enteredInCube = false;
                    var samplingSteps = 800; 
                    for (var t = 0; t<samplingSteps; t++)
                    {
                        var position = line.CoordinateToPosition(t);
                        
                        //for the head
                        //if (isInside(position, 180,216,180))
                        
                        //for the vertebra
                        if (IsInside(position, 46,511,511))
                        {
                            enteredInCube = true;
                            var colorValue = values[(int)Math.Floor(position.X), (int)Math.Floor(position.Y),
                                 (int)Math.Floor(position.Z)];
                            
                             //var newColor = computeColorsHead(colorValue); //for head
                             var newColor = ComputeColorsVertebra(colorValue); //for vertebra

                             resultColor =  resultColor * Alpha + newColor * (1.0 - Alpha);
                             Alpha = Alpha + (1.0 - Alpha) * colorValue/255.0;
                            
                             if (Alpha >= 1.0)
                             {
                                 Alpha = 1.0;
                                 exitFromCube = true;
                                 break;
                             }
                        }
                        else
                        {
                            if (enteredInCube)
                            {
                                exitFromCube = true;
                            }
                        }
                        
                    }

                    if (enteredInCube && exitFromCube)
                    {
                        image.SetPixel(i,j, resultColor);
                    }
                    else
                    {
                        image.SetPixel(i, j, background);
                    }
                    
                }
            }
            image.Store(filename);
        }
    }
}