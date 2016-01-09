package Beverage;

public class Sprite extends Beverage {
		
	public Sprite(){
		description = "Sprite";
		System.out.println("A Sprite Created, worth $1.0...");
	}
	
	@Override
	public double cost() {
		
		return 1.0;
	}

}
