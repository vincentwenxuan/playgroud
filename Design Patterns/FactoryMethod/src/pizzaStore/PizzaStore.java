package pizzaStore;

import pizza.Pizza;

public abstract class PizzaStore {

	public Pizza orderPizza(){
		Pizza pizza;
		pizza = createPizza();
		
		pizza.prepare();
		pizza.bake();
		pizza.cut();
		pizza.box();
		
		return pizza;
	}
	
	abstract public Pizza createPizza();
	
	
	
}
