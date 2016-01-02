package try_Strategy;


import guns.MachineGun;
import ships.FutureShip;
import ships.GunShip;
import ships.HighTechShip;
import ships.Ship;
import bombs.SmallBomb;


public class Strategy_client {

	public static void main(String[] args) {

		
		Ship myBasicShip = new GunShip();
		myBasicShip.performShoot();
		myBasicShip.performBomb();
		
		System.out.println("=======================================");
		Ship myUpGradedShip = new HighTechShip();
		myUpGradedShip.performShoot();
		myUpGradedShip.performBomb();
		
		System.out.println("=======================================");
		Ship myFinalShip = new FutureShip();
		myFinalShip.performShoot();
		myFinalShip.performBomb();			
		
		System.out.println("=======================================");
		System.out.println("degrading my ship.......");
		myFinalShip.setBomb(new SmallBomb());
		myFinalShip.setGun(new MachineGun());
		myFinalShip.performShoot();
		myFinalShip.performBomb();		
	}

}
