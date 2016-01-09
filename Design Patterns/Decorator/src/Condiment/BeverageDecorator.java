package Condiment;

import Beverage.Beverage;

public abstract class BeverageDecorator extends Beverage {
	
	Beverage beverage;
	
	public abstract String getDescription();
	
}
