package observer;

import observable.Observable;

public interface Observer {

	public void update(String msg);
	public void addMyself(Observable obs);
	
}
