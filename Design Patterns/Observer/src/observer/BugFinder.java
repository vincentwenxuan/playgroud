package observer;

public class BugFinder extends ObserverNamedEntity {
	
	public BugFinder(String name) {
		super(name);
	}

	@Override
	public void update(String msg) {
		System.out.println("@@@ BugFinder " + myName + ": I'm finding bugs in this news...");
		if(msg.contains("bug")){
			System.out.println("HAHAHAHA!!!!!There is a bug in today's newspaper!!!!I WIN!!!");
		}else{
			System.out.println("There is no bug in today's newspaper.");
		}
		
	}
		
}
