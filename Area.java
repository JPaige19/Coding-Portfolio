/*
For this exercise you will write a class named Area. The Area class should provide static methods that calculate the areas of different geometric shapes.
The class should have three overloaded static methods named getArea. Here is a description of each method:

The first version of the static getArea method will calculate the area of a circle. It should accept the circle's radius as a double, and return the 
circle's area as a double. See the formula below for calculating the area of a circle.

The second version of the static getArea method will calculate the area of a rectangle. It should accept the rectangle's length and width as doubles, 
and return the rectangle's area as a double. See the formula below for calculating the area of a rectangle.

The third version of the static getArea method will calculate the area of a trapezoid. It should accept the trapezoid's base #1 length, base #2 length,
 and height as doubles, and return the trapezoid's area as a double. See the formula below for calculating the area of a trapezoid.

The Area class should also have a main method that calls each of the overloaded getArea methods. It should display the following values, each on a separate line:

The area of a circle with a radius of 3. The value should be rounded to two decimal places.

The area of a rectangle with a length of 2 and a width of 4. The value should be rounded to one decimal place.

The area of a trapezoid with a base lengths of 3 and 4, and a height of 5. The value should be rounded to one decimal place.

*/


public class Area 
{  
    public static double getArea(double radius)
    {
        return Math.PI * (radius * radius);
    }
   
    public static double getArea(double width, double length)
    {
        return width * length;
    }
   
    public static double getArea(double base1, double base2, double height)
    {
        return (base1 + base2) * height / 2;
    }
    
    public static void main(String[] args)
    {
      
        System.out.printf("%.2f\n", Area.getArea(3.0));
        System.out.printf("%.1f\n", Area.getArea(2.0, 4.0));
        System.out.printf("%.1f\n", Area.getArea(3.0, 4.0, 5.0));
    }
}