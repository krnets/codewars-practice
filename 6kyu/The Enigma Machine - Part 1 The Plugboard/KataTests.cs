using System.Linq;
using NUnit.Framework;

[TestFixture]
public class PlugboardTestConstruction
{
    [Test]
    public void ValidConstruction()
    {
        var pb = new Plugboard("AB");
        Assert.AreEqual('B', pb.process('A'), "A has to be translated to B with 'AB'");
        Assert.AreEqual('A', pb.process('B'), "B has to be translated to A with 'AB'");
        Assert.AreEqual('C', pb.process('C'), "C has to stay C with 'AB'");
    }

    [Test]
    public void TranslateEnigmaMessage()
    {
        var wireConfig = "ABCDEFGHIJZYXWVUTSRQ";
        var pb = new Plugboard(wireConfig);
        var plain = "THE ENIGMA MACHINE CANNOT BE CRACKED";
        var expected = "SGF FNJHMB MBDGJNF DBNNOS AF DQBDKFC";

        var encrypted = plain.Select(c => pb.process(c));
        Assert.AreEqual(expected, encrypted, "Invalid encryption for '" + wireConfig + '"');

        var decrypted = encrypted.Select(c => pb.process(c));
        Assert.AreEqual(plain, decrypted, "Invalid encryption for '" + wireConfig + '"');
    }
}