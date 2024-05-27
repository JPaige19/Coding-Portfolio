/*
A bag of cookies holds 40 cookies. 
The calorie information on the bag claims that there are 10 servings in the bag and that a serving equals 300 calories. 
Write a program that lets the user enter the number of cookies he or she actually ate and then reports the number of 
total calories consumed.
*/

import java.util.Scanner;

public class CookieCalorieCounter
{
   public static void main(String[] args)
   {
      final int NUM_COOKIES_BAG = 40;
      final int SERVING_SIZE = 10;
      final int CALS_PER_SERVING = 300;
      final int COOKIES_PER_SERVING = NUM_COOKIES_BAG / SERVING_SIZE;
      final int CALS_PER_COOKIE = CALS_PER_SERVING / COOKIES_PER_SERVING;

      //Getting user input 
      Scanner keyboard = new Scanner(System.in);
      System.out.print("Enter number of cookies eaten: ");
      int numCookiesEaten = keyboard.nextInt();
      
      //Returning calorieCount
      int calorieCount = CALS_PER_COOKIE * numCookiesEaten;
      System.out.println("Your calorie intake was: " + calorieCount + 
                         " calories.");
   }
}