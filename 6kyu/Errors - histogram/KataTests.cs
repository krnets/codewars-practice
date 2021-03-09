using NUnit.Framework;
using System;

[TestFixture]
public static class HistTests
{
    private static void Testing(string s, string expect)
    {
        Console.WriteLine("testing: " + s);
        string actual = Hist.hist(s);
        Console.WriteLine("Actual\n" + actual);
        Console.WriteLine("Expect\n" + expect);
        Console.WriteLine("-");
        Assert.AreEqual(expect, actual);
    }

    [Test]
    public static void Tests()
    {
        Console.WriteLine("Fixed Tests");
        Testing("tpwaemuqxdmwqbqrjbeosjnejqorxdozsxnrgpgqkeihqwybzyymqeazfkyiucesxwutgszbenzvgxibxrlvmzihcb",
            "u  3     ***\rw  4     ****\rx  6     ******\rz  6     ******");
        Testing("aaifzlnderpeurcuqjqeywdq", "u  2     **\rw  1     *\rz  1     *");
        Testing("sjeneccyhrcpfvpujfaoaykqllteovskclebmzjeqepilxygdmzvdfmxbqdzubkzturnuqxsewrwgmdfwgdx",
            "u  4     ****\rw  3     ***\rx  4     ****\rz  4     ****");
        Testing("bnxyytdtqrkeaswymiwbxnuydwthweyzny", "u  1     *\rw  4     ****\rx  2     **\rz  1     *");
        Testing("ttopvdaxgwfpzjmomkwssytktaizqtsekfmfhrabidwaugioqyyzrxbugsusxkfdevmijqyprcoxfyjqwsutoutjgozyhsoytg",
            "u  5     *****\rw  4     ****\rx  4     ****\rz  4     ****");

        Testing("slirsxpbiholwngafelbbfxrpvqbcaykiazzgivjwgdqmz",
            "w  2     **\rx  2     **\rz  3     ***");
        Testing("dqyfsyvsdcohcdkxguxvvgobsmdbokaxblrsqjxaxtmisycyuwvaoirvfdzxzbxwjwgwmuzhwzuvmlun",
            "u  5     *****\rw  5     *****\rx  7     *******\rz  4     ****");
        Testing("uqxaxmffljgjanfnhayhzgbgbzjtxuwuuofzlswh",
            "u  4     ****\rw  2     **\rx  3     ***\rz  3     ***");
        Testing("ykotnfvvsjpfbzqgryokfwiygyhbnuuxgegzklsuxdejovxnza",
            "u  3     ***\rw  1     *\rx  3     ***\rz  3     ***");
        Testing("xlmsuuwwclqxmulthtxudlrwpextjgymnikwwcwewayzsznxczxrvmrxhtnpvqlchwhtenvukqou",
            "u  6     ******\rw  8     ********\rx  7     *******\rz  3     ***");

        Testing("loxssnpvnbzifiblquftlqzyxuafvgxzqcbxgojizveuextxnixqvgtxvnue",
            "u  4     ****\rx  8     ********\rz  4     ****");
        Testing("kfxbpcxcglioftgyxvxivypz",
            "x  4     ****\rz  1     *");
        Testing("hpszqbciswtriszumirjdettdgeqtegkqrcyysnnzjwpoifmjbwynvhwmqglwonkoushrxxrvjsvvgmuuhkcpyrkifzhjotvvq",
            "u  4     ****\rw  5     *****\rx  2     **\rz  4     ****");
        Testing("lwmttlojvdhuqaozilogsrbkqwrcncpghzdzwcolqlxpvzpktdxabmnwwzfyxpdkmvnxayzwmxlurlvwulievvxcku",
            "u  4     ****\rw  7     *******\rx  6     ******\rz  6     ******");
        Testing("mdrdynisnwxmzkrrucehagtsjikjceulicjyomsdxiplhuvanqyp",
            "u  3     ***\rw  1     *\rx  2     **\rz  1     *");

        Testing("htiroicmdatvknrmwgofubksfffuxcybvlzqnjttmuihojwgrfztxauxfbcxzgbofvqyfoxnpogvxfllxupdtzrhswwobgqy",
            "u  5     *****\rw  4     ****\rx  7     *******\rz  4     ****");
        Testing("hzqrlsvtngonkrktrrxojfqiioflfhpdjvcpanvzuyjsuxhjnuxhtkivhminviujizvhfpupmljwkddhubbkiv",
            "u  6     ******\rw  1     *\rx  3     ***\rz  3     ***");
        Testing("iqzrgevsmbvxevxmomsrmxzbjhmvsexbccdzmjjgwatqtvlseovhrmavstucveqllwkdijudkeauui",
            "u  4     ****\rw  2     **\rx  4     ****\rz  3     ***");
        Testing("piekhlepxfqjdregmobsutpnbtymlztexcbtkbxryvxhpfxhtpxfyrlujqyewblilwytrcyxzipxqxyewglknvlzquvlyp",
            "u  3     ***\rw  3     ***\rx  9     *********\rz  3     ***");
        Testing("kwlrizwobqwbtlfwwbnt", "w  5     *****\rz  1     *");
        Testing("kwlriwobqwbtlfwwbnt", "w  5     *****");
        Testing("tpaemqdmqbqrjbeosjnejqordosnrgpgqkeihqybyymqeafkyicestgsbenvgibrlvmihcb", "");
    }
}