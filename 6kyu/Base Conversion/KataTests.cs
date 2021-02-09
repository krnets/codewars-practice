using System;
using NUnit.Framework;

[TestFixture]
public class ExampleTests {
    Kata k = new Kata();
    [Test]
    public void BetweenNumeralSystems() {
        Assert.AreEqual("1111", k.Convert("15", Alphabet.DECIMAL, Alphabet.BINARY), "\"15\" dec -> bin");
        Assert.AreEqual("17", k.Convert("15", Alphabet.DECIMAL, Alphabet.OCTAL), "\"15\" dec -> oct");
        Assert.AreEqual("10", k.Convert("1010", Alphabet.BINARY, Alphabet.DECIMAL), "\"1010\" bin -> dec");
        Assert.AreEqual("a",k.Convert("1010", Alphabet.BINARY, Alphabet.HEXA_DECIMAL), "\"1010\" bin -> hex");
    }
  
    [Test]
    public void BetweenOtherBases(){
        Assert.AreEqual("a", k.Convert("0", Alphabet.DECIMAL, Alphabet.ALPHA), "\"0\" dec -> alpha");
        Assert.AreEqual("bb", k.Convert("27", Alphabet.DECIMAL, Alphabet.ALPHA_LOWER), "\"27\" dec -> alpha lower");
        Assert.AreEqual("320048", k.Convert("hello", Alphabet.ALPHA_LOWER, Alphabet.HEXA_DECIMAL), "\"hello\" alpha lower -> hex");
        Assert.AreEqual("SAME", k.Convert("SAME",Alphabet.ALPHA_UPPER, Alphabet.ALPHA_UPPER), "\"SAME\" alpha upper -> alpha upper");
    }
}