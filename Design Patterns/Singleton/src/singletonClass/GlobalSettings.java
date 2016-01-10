package singletonClass;

public class GlobalSettings {
	
	private static GlobalSettings globalSettingsInstance;
	
	private String fond;
	private double size;
	
	private GlobalSettings(){
		System.out.println("Global settings instance created!");
		fond = "A New Fond";
		size = 100.99;
		
	}
	
	public static GlobalSettings getInstance(){
		if(globalSettingsInstance == null){
			globalSettingsInstance = new GlobalSettings();
		}
		
		return globalSettingsInstance;
	}
	
	public String getFond(){
		return fond;
	}
	
	public double getSize(){
		return size;
	}
	
	public void displaySettings(){
		System.out.println("Settings are:");
		System.out.println("Fond: " + fond);
		System.out.println("Size: " + size);
		
	}
	
	
}
