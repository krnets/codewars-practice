using NUnit.Framework;

[TestFixture]
public class SqlQueryOutputToCsvConverterTests
{
    [Test]
    public void SmallDataTest()
    {
        string[] lines =
        {
            "MemberId   ,Surname   ,FirstName ,DateOfBirth,MembershipStartDate,NumberOfDependents,MonthlyPremiumRands\r\n",
            "-----------,----------,----------,-----------,-------------------,------------------,---------------------------------------\r\n",
            "1          ,Downs     ,Graham    ,1980-12-14 ,1998-01-01         ,1                 ,5120\r\n",
            "2          ,Blogs     ,Joe       ,1978-03-20 ,2012-06-01         ,0                 ,2965\r\n",
            "3          ,Smith     ,Jenny     ,1994-01-01 ,2005-12-01         ,11                ,31658\r\n",
            "\r\n",
            "(3 row(s) affected)\r\n"
        };
        var result = new SqlQueryOutputToCsvConverter().Convert(lines);
        Assert.AreEqual(
            "MemberId,Surname,FirstName,DateOfBirth,MembershipStartDate,NumberOfDependents,MonthlyPremiumRands\r\n" +
            "1,Downs,Graham,1980-12-14,1998-01-01,1,5120\r\n" +
            "2,Blogs,Joe,1978-03-20,2012-06-01,0,2965\r\n" +
            "3,Smith,Jenny,1994-01-01,2005-12-01,11,31658\r\n", result);
    }
}