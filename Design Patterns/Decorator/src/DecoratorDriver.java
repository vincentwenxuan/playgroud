import Beverage.Beverage;
import Beverage.BlackCoffee;
import Condiment.Ice;
import Condiment.Milk;
import Condiment.Sugar;
import Condiment.Sult;




/*
In this example, We'll implement a Beverage shop offers beverage with different condiment 
e.g.:
Beverage: 
	Water, Coke, Sprite, BlackCoffee
Condiment:
	Sugar, Sult, Ice, Milk

The Diver will going to get the whole beverage's name and compute its costs


With Decorator, you can attack additional responsibility to an object at run time!!!
*/



public class DecoratorDriver {

	public static void main(String[] args) {
		
		System.out.println("==============ordering=================");
		//I ordered a coffee with some condiments
		Beverage myBeverage = new BlackCoffee();
		myBeverage = new Milk(myBeverage);
		myBeverage = new Sugar(myBeverage);
		myBeverage = new Sult(myBeverage);
		myBeverage = new Ice(myBeverage);
		
		//I like more sugar, so I add another sugar
		myBeverage = new Sugar(myBeverage);
		
		//Now let's see what we get finally!
		System.out.println();
		System.out.println("==============check=================");
		System.out.println("You have ordered:");
		System.out.println(myBeverage.getDescription());
		
		double cost = myBeverage.cost();
		System.out.println("The total cost is:");
		System.out.println("$" + cost);
		
	}
	
	
	
	
	
}
