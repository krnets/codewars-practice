using System;
using System.Collections.Generic;
using NUnit.Framework;

[TestFixture]
public class Test
{
    [Test]
    public void SampleTest1()
    {
        // Flips all bits in an array
        Assert.AreEqual(new bool[] {false, false, true, true, false, true, false},
            Kata.Interpreter("10", new bool[] {true, true, false, false, true, false, true}));
        // Assert.AreEqual("0011010", Kata.Interpreter("10", "1100101"));
        // Assert.AreEqual(
        // "1100101"));
        // "0011010", Kata.Interpreter("10",
        // Assert.AreEqual(Convert.ToString(new bool[] {false, false, true, true, false, true, false}),
        // Kata.Interpreter("10", Convert.ToString(new bool[] {true, true, false, false, true, false, true})));
    }

    [Test]
    public void SampleTest2()
    {
        // Flips every second bit in an array
        Assert.AreEqual(new bool[] {false, true, false, true, false, true, false, true, false, true},
            Kata.Interpreter("100", new bool[] {true, true, true, true, true, true, true, true, true, true}));
        // Assert.AreEqual("0101010101", Kata.Interpreter("100", "1111111111"));
    }


    [Test]
    public void SampleTest()
    {
        // Flips all bits in an array
        Assert.AreEqual(new bool[] {false, false, true, true, false, true, false},
            Kata.Interpreter("10", new bool[] {true, true, false, false, true, false, true}));
        // Flips every second bit in an array
        Assert.AreEqual(new bool[] {false, true, false, true, false, true, false, true, false, true},
            Kata.Interpreter("100", new bool[] {true, true, true, true, true, true, true, true, true, true}));
    }

    [Test]
    public void FixedTest()
    {
        Assert.AreEqual(new bool[] {true, false, true, false},
            Kata.Interpreter("110", new bool[] {true, false, true, false}));
        Assert.AreEqual(new bool[] {true, false, false, false, true, false, false, false, true},
            Kata.Interpreter("0", new bool[] {true, false, false, false, true, false, false, false, true}));
        Assert.AreEqual(new bool[] {false, false, false}, Kata.Interpreter("101010", new bool[] {true, true, true}));
    }

    private static bool[] Solution(string code, bool[] array)
    {
        bool[] newArray = (bool[]) array.Clone();
        int ptr = 0;

        while (ptr != newArray.Length)
        {
            for (int i = 0; i < code.Length; ++i)
            {
                if (code[i] == '1')
                {
                    newArray[ptr] = !newArray[ptr];
                }

                if (code[i] == '0')
                {
                    ++ptr;
                }

                if (ptr == newArray.Length) break;
            }
        }

        return newArray;
    }

    private static Random rnd = new Random();

    [Test]
    public void RandomTest()
    {
        for (int i = 0; i < 100; ++i)
        {
            string code = "";
            for (int j = 0; j < 10; ++j)
            {
                code += rnd.Next(0, 2).ToString();
            }

            List<bool> array = new List<bool>();
            for (int j = 0; j < 100; ++j)
            {
                array.Add((rnd.Next(0, 2) == 1) ? true : false);
            }

            Assert.AreEqual(Solution(code, array.ToArray()), Kata.Interpreter(code, array.ToArray()));
        }
    }
}