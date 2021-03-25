using NUnit.Framework;
using System;
using System.Threading;

[TestFixture]
public class SolutionTest
{
    private readonly object monitor = new object();

    [Test]
    public void SampleTests()
    {
        Worker w = new Worker();
        Random rand = new Random();
        int counter = 20;
        int executionCounter = 0;
        Action a = () =>
        {
            Console.Write('.');
            Thread.Sleep(1000);
            lock (monitor)
            {
                executionCounter++;
            }
        };
        w.Execute(a, 20);
        if (counter != executionCounter)
            Console.WriteLine($"Aciton was executed {executionCounter} times instead of {counter} times");
        Assert.IsTrue(counter == executionCounter);
    }
}