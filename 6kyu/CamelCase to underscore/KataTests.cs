using NUnit.Framework;

[TestFixture]
public class CamelCaseTranslatorTests
{
    [Test]
    public void SimpleUnitNameTests()
    {
        Assert.AreEqual("This_Is_A_Unit_Test", CamelCaseTranslator.ToUnderScore("ThisIsAUnitTest"));
        Assert.AreEqual("This_Should_Be_Split_Correct_Into_Underscore",
            CamelCaseTranslator.ToUnderScore("ThisShouldBeSplitCorrectIntoUnderscore"));
    }

    [Test]
    public void CalculationUnitNameTests()
    {
        Assert.AreEqual("Calculate_1_Plus_1_Equals_2", CamelCaseTranslator.ToUnderScore("Calculate1Plus1Equals2"));
        Assert.AreEqual("Calculate_15_Plus_5_Equals_20", CamelCaseTranslator.ToUnderScore("Calculate15Plus5Equals20"));
        Assert.AreEqual("Calculate_500_Divided_By_5_Equals_100",
            CamelCaseTranslator.ToUnderScore("Calculate500DividedBy5Equals100"));
    }

    [Test]
    public void SpecialUnitNameTests()
    {
        Assert.AreEqual("This_Is_Already_Split_Correct",
            CamelCaseTranslator.ToUnderScore("This_Is_Already_Split_Correct"));
        Assert.AreEqual("This_Is_Not_Split_Correct", CamelCaseTranslator.ToUnderScore("ThisIs_Not_SplitCorrect"));
        Assert.AreEqual("_If_A_Test_Start_And_Ends_With_Underscore_It_Should_Be_The_Same_",
            CamelCaseTranslator.ToUnderScore("_IfATestStartAndEndsWithUnderscore_ItShouldBeTheSame_"));
    }
}