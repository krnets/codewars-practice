using NUnit.Framework;
using System;

[TestFixture]
public class AgeTest
{
    [Test]
    public void FirstTest()
    {
        DateTime birthday = new DateTime(2015, 10, 16);
        StringAssert.AreEqualIgnoringCase(Kata.HowOld(birthday), Kata.HowOld(birthday),
            string.Format("The output expect {0} but it returns {1}", Kata.HowOld(birthday),
                Kata.HowOld(birthday)));
    }

    [Test]
    public void SecondTest()
    {
        DateTime birthday = new DateTime(2014, 12, 23);
        StringAssert.AreEqualIgnoringCase(Kata.HowOld(birthday), Kata.HowOld(birthday),
            string.Format("The output expect {0} but it returns {1}", Kata.HowOld(birthday),
                Kata.HowOld(birthday)));
    }

    [Test]
    public void ThirdTest()
    {
        DateTime birthday = new DateTime(1983, 09, 21);
        StringAssert.AreEqualIgnoringCase(Kata.HowOld(birthday), Kata.HowOld(birthday),
            string.Format("The output expect {0} but it returns {1}", Kata.HowOld(birthday),
                Kata.HowOld(birthday)));
    }

    [Test]
    public void FourthTest()
    {
        DateTime birthday = new DateTime(2015, 01, 30);
        StringAssert.AreEqualIgnoringCase(Kata.HowOld(birthday), Kata.HowOld(birthday),
            string.Format("The output expect {0} but it returns {1}", Kata.HowOld(birthday),
                Kata.HowOld(birthday)));
    }
}