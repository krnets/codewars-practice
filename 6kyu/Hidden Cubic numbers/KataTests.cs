using NUnit.Framework;

[TestFixture]
public class CubesTests
{
    [Test]
    public void Test1()
    {
        var s = "0 9026315 -827&()"; // "0 0 Lucky"
        var r = "0 0 Lucky";
        Assert.AreEqual(r, Cubes.isSumOfCubes(s));
    }

    [Test]
    public void Test2()
    {
        var s = "aqdf& 0 1 xyz 153 777.777";
        var r = "0 1 153 154 Lucky";
        Assert.AreEqual(r, Cubes.isSumOfCubes(s));
    }

    [Test]
    public void Test3()
    {
        var s = "QK29 45[&erui";
        var r = "Unlucky";
        Assert.AreEqual(r, Cubes.isSumOfCubes(s));
    }

    [Test]
    public void Test4()
    {
        var s = "&z _upon 407298a --- ???ry, ww/100 I thought, 631str*ng and w===y -721&()"; // "407 407 Lucky"
        var r = "407 407 Lucky";
        Assert.AreEqual(r, Cubes.isSumOfCubes(s));
    }

    [Test]
    public void Test5()
    {
        var s =
            "&z371 upon 407298a --- dreary, ###100.153 I thought, 9926315strong and weary -127&() 1"; // "371 407 153 1 932 Lucky"
        var r = "371 407 153 1 932 Lucky";
        Assert.AreEqual(r, Cubes.isSumOfCubes(s));
    }
}