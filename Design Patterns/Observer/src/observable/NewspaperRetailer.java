package observable;

import java.util.ArrayList;

import observer.Observer;



public class NewspaperRetailer implements Observable{
	
	ArrayList<Observer> peopleSubscribed;
	String storeName;
	String todayMsg;
	
	public NewspaperRetailer(String storeName){
		this.storeName = storeName;
		peopleSubscribed = new ArrayList<Observer>();
		System.out.println('"' + this.storeName + '"' + " has been constructed! Ready for distributing Newspaper");
		todayMsg = "<<<<" + "Our new store!!! " + storeName + ">>>>";
	}
	
	public void newNewspaperArrived(String msg){
		todayMsg = msg;
		notifyObserver();
	}
	
	@Override
	public void registerObserver(Observer observer) {
		peopleSubscribed.add(observer);
		System.out.println(observer.toString() + " has been registered.");
		
		
	}

	@Override
	public void removeObserver(Observer observer) {
		peopleSubscribed.remove(observer);
		System.out.println(observer.toString() + " has been removed from Newspaper!");
		
	}

	@Override
	public void notifyObserver() {
		Boolean hasSubscriber = !peopleSubscribed.isEmpty();
		System.out.println("Today's News!!! " + todayMsg);
		
		if(!hasSubscriber){
			
			System.out.println("Sorry. We've got no subscriber YET, ADD some!!!");	
		}
		else{
			for (Observer person:peopleSubscribed){
				person.update(todayMsg);
				
			}
				
		}		
		
	}
	

}
