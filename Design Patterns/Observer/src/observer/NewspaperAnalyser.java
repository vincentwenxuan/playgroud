package observer;


public class NewspaperAnalyser extends ObserverNamedEntity {
	
	public NewspaperAnalyser(String name) {
		super(name);
	}

	@Override
	public void update(String msg) {
		System.out.println("@@@ Analyser " + myName + ": I'm Analysing this news!!");
		System.out.println("It has " + msg.length() + " characters!!!!" );

	}
		

}
