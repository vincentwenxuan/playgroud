package Beverage;

public class Water extends Beverage {

	
	public Water(){
		description = "Water";
		System.out.println("A Water Created, worth $0.5...");
	}

	
	@Override
	public double cost() {

		return 0.5;
	}

}
