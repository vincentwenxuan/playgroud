package observer;

import observable.Observable;

public abstract class ObserverNamedEntity implements Observer {
	
	String myName;
	
	public ObserverNamedEntity(String name){
		myName = name;
	}
	
	public abstract void update(String msg);
	

	public void addMyself(Observable obs) {
		obs.registerObserver(this);
	}
	
	public void removeMyself(Observable obs) {
		obs.removeObserver(this);
	}
		
	public String toString() {
		return myName;
	}
		

}
