package Condiment;

import Beverage.Beverage;

public class Ice extends BeverageDecorator {

	public Ice(Beverage beverage){
		this.beverage = beverage;
		System.out.println("Ice added, worth $0.2...");
	}
	
	@Override
	public String getDescription() {
		String description = beverage.getDescription() + ", with Ice";
		return description;
	}

	@Override
	public double cost() {
		double cost = beverage.cost() + 0.2;
		return cost;
	}

}
