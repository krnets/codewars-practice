using System;
using NUnit.Framework;

[TestFixture]
public class ComparingTests
{
    private Random rand = new Random((int) DateTime.Now.Ticks);

    [Test]
    public void Compare1()
    {
        Assert.AreEqual(true, Kata.Compare("AD", "BC"), "'AD' vs 'BC'");
    }

    [Test]
    public void Compare2()
    {
        Assert.AreEqual(false, Kata.Compare("AD", "DD"), "'AD' vs 'DD'");
    }

    [Test]
    public void Compare3()
    {
        Assert.AreEqual(true, Kata.Compare("gf", "FG"), "'gf' vs 'FG'");
    }

    [Test]
    public void Compare4()
    {
        Assert.AreEqual(false, Kata.Compare("Ad", "DD"), "'Ad' vs 'DD'");
    }

    [Test]
    public void Compare5()
    {
        Assert.AreEqual(true, Kata.Compare("zz1", ""), "'zz1' vs ''");
    }

    [Test]
    public void Compare6()
    {
        Assert.AreEqual(true, Kata.Compare("ZzZz", "ffPFF"), "'ZzZz' vs 'ffPFF'");
    }

    [Test]
    public void Compare7()
    {
        Assert.AreEqual(false, Kata.Compare("kl", "lz"), "'kl' vs 'lz'");
    }

    [Test]
    public void Compare8()
    {
        Assert.AreEqual(true, Kata.Compare(null, ""), "'<null>' vs ''");
    }

    [Test]
    public void Compare9()
    {
        Assert.AreEqual(true, Kata.Compare("!!", "7476"), "'!!' vs '7476'");
    }

    [Test]
    public void Compare10()
    {
        Assert.AreEqual(true, Kata.Compare("##", "1176"), "'##' vs '1176'");
    }

    [Test]
    public void CompareRandom()
    {
        for (int i = 0; i < 40; i++)
        {
            var letter1 = (char) rand.Next(65, 90);
            char letter2 = '1';

            do
            {
                letter2 = (char) rand.Next(65, 90);
            } while (letter1 == letter2);

            if (rand.Next(0, 2) == 1)
            {
                Assert.AreEqual(true,
                    Kata.Compare(new string(letter1, 5).ToUpper() + letter2,
                        letter2 + new string(letter1, 5).ToLower()));
            }

            if (rand.Next(0, 2) == 1)
            {
                Assert.AreEqual(false,
                    Kata.Compare(new string(letter1, 4).ToUpper() + letter2 + letter2,
                        letter2 + new string(letter1, 5).ToLower()));
            }
        }
    }
}