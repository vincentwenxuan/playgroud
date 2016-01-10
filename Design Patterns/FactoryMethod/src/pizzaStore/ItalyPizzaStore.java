package pizzaStore;

import pizza.ItalyPizza;
import pizza.Pizza;

public class ItalyPizzaStore extends PizzaStore {
	
	public ItalyPizzaStore(){
		System.out.println("A Italy Pizza Store has been created.");
	}
	
	
	public Pizza createPizza(){	
		
		return new ItalyPizza();
	}
	
	
	
	
}
