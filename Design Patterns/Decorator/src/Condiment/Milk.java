package Condiment;

import Beverage.Beverage;

public class Milk extends BeverageDecorator {
	
	
	public Milk(Beverage beverage){
		this.beverage = beverage;
		System.out.println("Milk added, worth $1...");
	}
	
	@Override
	public String getDescription() {
		String description = beverage.getDescription() + ", with Milk";
		return description;
	}

	@Override
	public double cost() {
		double cost = beverage.cost() + 1.0;
		return cost;
	}

}
