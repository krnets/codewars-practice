using NUnit.Framework;
using System;

[TestFixture]
public class SolutionTest
{
    [Test]
    public void SampleTest1()
    {
        Assert.AreEqual("VALID", validPass.validator("Username123"));
    }

    [Test]
    public void SampleTest2()
    {
        Assert.AreEqual("INVALID", validPass.validator("Username"));
    }

    [Test]
    public void SampleTest3()
    {
        Assert.AreEqual("INVALID", validPass.validator("123"));
    }

    [Test]
    public void SampleTest4()
    {
        Assert.AreEqual("INVALID", validPass.validator("Username123!"));
    }

    [Test]
    public void SampleTest5()
    {
        Assert.AreEqual("INVALID", validPass.validator("ThisPasswordIsTooLong1234"));
    }

    [Test]
    public void SampleTestLessThan20()
    {
        Assert.AreEqual("VALID", validPass.validator("Username123tstSampl"));
    }

    [Test]
    public void LengthTest()
    {
        Assert.AreEqual("VALID", validPass.validator("JQzXhxk6YcgmyKh2"));
        Assert.AreEqual("INVALID", validPass.validator("m7b4XR2q8qmRMsW7ZkuVvUq"));
        Assert.AreEqual("VALID", validPass.validator("KLuMdun5V"));
        Assert.AreEqual("INVALID", validPass.validator("b4d"));
    }
}