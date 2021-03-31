using System;

public class Kata
{
    public IClock Clock;

    public Kata(IClock clock)
    {
        Clock = clock;
    }

    public int GetAgeFromDOB(DateTime birthday)
    {
        var current = Clock.Now;

        return current.Year - birthday.Year - (current.Month < birthday.Month ? 1 : 0);
    }
}

public interface IClock
{
    DateTime Now { get; }
}

public class SystemClock : IClock
{
    public DateTime Now => DateTime.Now;
}

public class StaticClock : IClock
{
    public DateTime Now { get; }

    public StaticClock(DateTime now)
    {
        Now = now;
    }
}