import singletonClass.GlobalSettings;


/*
This is an example of Singleton Pattern.

Singleton is used when we want to:
1. Instantiate only ONE object of that class.
2. Want to have a global access.  (And only lazy create)



*/




public class SingletonDriver {

	public static void main(String[] args) {
		
		
		GlobalSettings settings = GlobalSettings.getInstance();
	
		System.out.println("=============Display==============");
		settings.displaySettings();
	
	
	
	}
	
	
	
}
