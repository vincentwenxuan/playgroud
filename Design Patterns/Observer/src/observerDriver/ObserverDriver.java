
package observerDriver;

import observable.NewspaperRetailer;
import observer.BugFinder;
import observer.NewspaperAnalyser;
import observer.NormalPeopleReader;


//
//  This program is simulating Observer Pattern  
//	Example is a newspaper distributor:
//		People can register as subscriber of this newspaper
//		When subscribed, they will receive newspaper when a new one is available
//		They can unregister themselves so that they will not receive newspaper anymore 
//


public class ObserverDriver {

	public static void main(String[] args) {
		// construct a new observable, and try to publish a News
		System.out.println("================Day 1=================");
		NewspaperRetailer myStrore = new NewspaperRetailer("Wenxuan Newspaper Shop");
		myStrore.notifyObserver();
		
		// construct different kinds of people(observer)
		NormalPeopleReader personA = new NormalPeopleReader("Wenxuan Tang");
		NormalPeopleReader personB = new NormalPeopleReader("Tony Stark");
		NewspaperAnalyser analyser = new NewspaperAnalyser("Holmes"); 
		BugFinder bugfinder = new BugFinder("Dodge");
		
		// They all registered to this new newspaper!
		System.out.println("================Day 2=================");
		myStrore.registerObserver(personA);
		myStrore.registerObserver(personB);
		myStrore.registerObserver(analyser);
		myStrore.registerObserver(bugfinder);
		
		// A news has come!
		System.out.println("================Day 2=================");
		myStrore.newNewspaperArrived("<ALIEN IS ATTACKING EARTH>");

		// Another news has come!
		System.out.println("================Day 3=================");
		myStrore.newNewspaperArrived("<This ALIEN become EARTH's friend>");

		// Another news has come!
		System.out.println("================Day 4=================");
		myStrore.newNewspaperArrived("<ALIEN: There should be no bug between us!!>");
		
		// PersonB and Holmes disappointed at the newspaper and quit
		// They will NOT receive today's news now!!!
		System.out.println("================Day 5=================");
		personB.removeMyself(myStrore); 
		analyser.removeMyself(myStrore); 
		myStrore.newNewspaperArrived("<There are no bug in our news>");
		
	
		
		
	}

	
	
}
