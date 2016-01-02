package ships;

import guns.PlasmaGun;
import bombs.NuclearBomb;

public class FutureShip extends Ship {
	public FutureShip(){
		System.out.println("A Ultimate Ship from future has been built.");
		gun = new PlasmaGun();
		bomb = new NuclearBomb();
	}
}

