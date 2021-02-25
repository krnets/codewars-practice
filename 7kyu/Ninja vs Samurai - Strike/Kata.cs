using System;

public class Warrior
{
    public string Name { get; }
    public int Health { get; set; } = 100;

    public Warrior(string name) => Name = name;

    public void Strike(Warrior enemy, int swings)
    {
        enemy.Health = Math.Max(0, enemy.Health - (swings * 10));
    }
}