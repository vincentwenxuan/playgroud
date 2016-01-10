package pizza;

public abstract class Pizza {

	String name;
	String dough;
	String sauce;
	
	public void prepare(){
		System.out.println("Preparing " + name );
		System.out.println("Tossing dough...");
		System.out.println("Adding sauce...");
	}
	
	public void bake(){
		System.out.println("Bake for 25minutes at 350...");	
	}
	
	public void cut(){
		System.out.println("Cutting the pizza to 8 pieces...");
	}
	
	public void box(){
		System.out.println("Package pizza in to box...");
	}
	
	public String getName(){
		return name;
	}
	
	
	
}
