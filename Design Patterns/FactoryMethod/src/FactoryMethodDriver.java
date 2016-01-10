import pizzaStore.ItalyPizzaStore;
import pizzaStore.NYPizzaStore;
import pizzaStore.PizzaStore;



/*

This an example of FactoryMethod Pattern
The idea is to let subclass decide with component to create

Example was illustrated by a Pizza Store who offers different kinds of Pizza,
Pizza store abstract was in charge of serving Pizza, but leave pizza creation itself to its subclass. 


Pizza Abstract                PizzaStore Abstract
		|							|
		|							|
concrete Pizza	  <--------		concrete Store	

*/


public class FactoryMethodDriver {

	public static void main(String[] args) {
		
		
		PizzaStore myStore = new ItalyPizzaStore();
		myStore.orderPizza();
		
		System.out.println("=============My order complete!===============");
		
		PizzaStore yourStore = new NYPizzaStore();
		yourStore.orderPizza();
		
		System.out.println("=============Your order complete!===============");
		
	}


	




}
