using System;
using System.Threading.Tasks;

public class Worker
{
    public void Execute(Action a, int nTimes) => Parallel.For(0, nTimes, _ => a());
}