public class Kata
{
    public static string declareWinner(Fighter fighter1, Fighter fighter2, string firstAttacker)
    {
        int att = (fighter2.Health - 1) / fighter1.DamagePerAttack;
        int def = (fighter1.Health - 1) / fighter2.DamagePerAttack;

        return att < def ? fighter1.Name : def < att ? fighter2.Name : firstAttacker;
    }
}