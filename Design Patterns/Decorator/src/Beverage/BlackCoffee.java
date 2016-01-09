package Beverage;

public class BlackCoffee extends Beverage {

	public BlackCoffee(){
		description = "BlackCoffee";
		System.out.println("A BlackCoffee Created,, worth $2.5...");
	}
	
	
	@Override
	public double cost() {
		
		return 2.5;
	}

}
