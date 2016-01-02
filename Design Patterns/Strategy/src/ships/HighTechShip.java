package ships;

import guns.LaserGun;
import bombs.BigBomb;

public class HighTechShip extends Ship{
	
	public HighTechShip(){
		System.out.println("A Stronger HighTechShip has been built.");
		gun = new LaserGun();
		bomb = new BigBomb();
	}
	
}

