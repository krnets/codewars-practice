public class Fraction
{
    private long Top { get; }
    private long Bottom { get; }

    public Fraction(long numerator, long denominator)
    {
        long gcd = GCD(numerator, denominator);
        Top = numerator / gcd;
        Bottom = denominator / gcd;
    }

    public override bool Equals(object o) => Compare(this, o as Fraction) == 0;
    private static long Compare(Fraction f1, Fraction f2) => f1.Top * f2.Bottom - f2.Top * f1.Bottom;
    public override string ToString() => $"{Top}/{Bottom}";

    public static bool operator ==(Fraction f1, Fraction f2) => Compare(f1, f2) == 0;
    public static bool operator !=(Fraction f1, Fraction f2) => Compare(f1, f2) != 0;

    // private static long GCD(long x, long y) => y == 0 ? x : GCD(y, x % y);
    private static long GCD(long x, long y) => x % y == 0 ? y : GCD(y, x % y);

    public static Fraction operator +(Fraction f1, Fraction f2) =>
        new Fraction(f1.Top * f2.Bottom + f2.Top * f1.Bottom, f1.Bottom * f2.Bottom);
}