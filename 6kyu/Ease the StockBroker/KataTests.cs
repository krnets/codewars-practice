using System;
using NUnit.Framework;

[TestFixture]
public class OrdersSummaryTests
{
    [Test]
    public void Test0()
    {
        String l = "GOOG 90 160.45 B, JPMC 67 12.8 S, MYSPACE 24.0 210 B, CITI 50 450 B, CSCO 100 55.5 S";
        String r = "Buy: 14440 Sell: 6408; Badly formed 2: MYSPACE 24.0 210 B ;CITI 50 450 B ;";
        Assert.AreEqual(r, OrdersSummary.balanceStatements(l));
    }

    [Test]
    public void Test1()
    {
        String l = "GOOG 300 542.0 B, AAPL 50 145.0 B, CSCO 250.0 29 B, GOOG 200 580.0 S";
        String r = "Buy: 169850 Sell: 116000; Badly formed 1: CSCO 250.0 29 B ;";
        Assert.AreEqual(r, OrdersSummary.balanceStatements(l));
    }

    [Test]
    public void Test2()
    {
        String l = "ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B, OWW 1000 11.623 B, OGG 20 580.1 B";
        String r = "Buy: 29499 Sell: 0";
        Assert.AreEqual(r, OrdersSummary.balanceStatements(l));
    }
}