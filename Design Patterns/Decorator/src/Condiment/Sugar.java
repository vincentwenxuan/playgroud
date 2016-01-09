package Condiment;

import Beverage.Beverage;

public class Sugar extends BeverageDecorator {

	public Sugar(Beverage beverage){
		this.beverage = beverage;
		System.out.println("Sugar added, worth $0.5...");
	}
	
	@Override
	public String getDescription() {
		String description = beverage.getDescription() + ", with Sugar";
		return description;
	}

	@Override
	public double cost() {
		double cost = beverage.cost() + 0.5;
		return cost;
	}


}
