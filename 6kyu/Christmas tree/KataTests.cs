using NUnit.Framework;

[TestFixture]
class ChristmasTreeGeneratorTests
{
    [Test]
    public void ChristmasTreeTest_0()
    {
        Assert.AreEqual("", ChristmasTreeGenerator.ChristmasTree(0));
    }

    [Test]
    public void ChristmasTreeTest_1()
    {
        Assert.AreEqual("*", ChristmasTreeGenerator.ChristmasTree(1));
    }

    [Test]
    public void ChristmasTreeTest_2()
    {
        Assert.AreEqual(" * \n***", ChristmasTreeGenerator.ChristmasTree(2));
    }

    [Test]
    public void ChristmasTreeTest_3()
    {
        Assert.AreEqual("  *  \n *** \n*****", ChristmasTreeGenerator.ChristmasTree(3));
    }

    [Test]
    public void ChristmasTreeTest_4()
    {
        Assert.AreEqual("   *   \n  ***  \n ***** \n*******", ChristmasTreeGenerator.ChristmasTree(4));
    }

    [Test]
    public void ChristmasTreeTest_5()
    {
        Assert.AreEqual("    *    \n   ***   \n  *****  \n ******* \n*********",
            ChristmasTreeGenerator.ChristmasTree(5));
    }

    [Test]
    public void ChristmasTreeTest_6()
    {
        Assert.AreEqual("     *     \n    ***    \n   *****   \n  *******  \n ********* \n***********",
            ChristmasTreeGenerator.ChristmasTree(6));
    }

    [Test]
    public void ChristmasTreeTest_7()
    {
        Assert.AreEqual(
            "      *      \n     ***     \n    *****    \n   *******   \n  *********  \n *********** \n*************",
            ChristmasTreeGenerator.ChristmasTree(7));
    }

    [Test]
    public void ChristmasTreeTest_8()
    {
        Assert.AreEqual(
            "       *       \n      ***      \n     *****     \n    *******    \n   *********   \n  ***********  \n ************* \n***************",
            ChristmasTreeGenerator.ChristmasTree(8));
    }

    [Test]
    public void ChristmasTreeTest_9()
    {
        Assert.AreEqual(
            "        *        \n       ***       \n      *****      \n     *******     \n    *********    \n   ***********   \n  *************  \n *************** \n*****************",
            ChristmasTreeGenerator.ChristmasTree(9));
    }

    [Test]
    public void ChristmasTreeTest_10()
    {
        Assert.AreEqual(
            "         *         \n        ***        \n       *****       \n      *******      \n     *********     \n    ***********    \n   *************   \n  ***************  \n ***************** \n*******************",
            ChristmasTreeGenerator.ChristmasTree(10));
    }
}