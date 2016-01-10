package pizzaStore;

import pizza.NYPizza;
import pizza.Pizza;

public class NYPizzaStore extends PizzaStore {
	public NYPizzaStore(){
		System.out.println("A NewYork Pizza Store has been created.");
	}
	
	
	public Pizza createPizza(){	
		
		return new NYPizza();
	}


}
