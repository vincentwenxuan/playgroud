package ships;

import bombs.SmallBomb;
import guns.MachineGun;

public class GunShip extends Ship {
	
	public GunShip(){
		System.out.println("A GunShip has been built.");
		gun = new MachineGun();
		bomb = new SmallBomb();
		
	}
	

}
