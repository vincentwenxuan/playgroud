package ships;

import bombs.BombBehavior;
import guns.GunBehavior;

public abstract class Ship {
	public GunBehavior gun;
	public BombBehavior bomb;
	
	public Ship(){
		System.out.println("A ship has been built.");
		
	}
	
	public void performShoot(){
		gun.shoot();
	}
	
	public void performBomb(){
		bomb.throwBomb();
	}	
	
	public void setGun(GunBehavior newGun){
		gun = newGun;
		String gunInfo = newGun.toString();
		System.out.println("Gun has been set to " + gunInfo);
	}
	
	public void setBomb(BombBehavior newBomb){
		bomb = newBomb;
		String bombInfo = newBomb.toString();
		System.out.println("Bomb has been set to " + bombInfo);
	}	
	
}
