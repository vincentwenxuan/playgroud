package Beverage;

public class Coke extends Beverage {
	
	
	public Coke(){
		description = "Coke Cola";
		System.out.println("A Coke Cola Created, worth $1.0...");
	}
	
	@Override
	public double cost() {	
		return 1.0;
	}

}
