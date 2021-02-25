### Ninja vs Samurai: Strike

Something is wrong with our Warrior class. 

The strike method does not work correctly. 

The following shows an example of this code being used:
```c
var ninja = new Warrior("Ninja");
var samurai = new Warrior("Samurai");

samurai.Strike(ninja, 3);
// ninja.Health should == 70
```
Can you figure out what is wrong?
