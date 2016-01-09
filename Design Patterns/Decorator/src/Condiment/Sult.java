package Condiment;

import Beverage.Beverage;

public class Sult extends BeverageDecorator {

	public Sult(Beverage beverage){
		this.beverage = beverage;
		System.out.println("Sult added, worth $0.3...");
	}
	
	@Override
	public String getDescription() {
		String description = beverage.getDescription() + ", with Sult";
		return description;
	}

	@Override
	public double cost() {
		double cost = beverage.cost() + 0.3;
		return cost;
	}

}
