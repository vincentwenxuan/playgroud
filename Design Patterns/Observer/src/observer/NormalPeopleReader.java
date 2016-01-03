package observer;


public class NormalPeopleReader extends ObserverNamedEntity{
	
	public NormalPeopleReader(String name) {
		super(name);
	}

	@Override
	public void update(String msg) {
		System.out.println("@@@ Reader " + myName + ": I read today's news is " + msg + ".");
		System.out.println("I'm Happy!!!");
	}
	

}
