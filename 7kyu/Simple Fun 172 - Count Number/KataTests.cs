namespace myjinxin
{
    using NUnit.Framework;
    using System;
    
    [TestFixture]
    public class myjinxin
    {

        [Test]
        public void BasicTest1()
        {
            var kata = new Kata();
            Assert.AreEqual(2, kata.CountNumber(5, 5));
        }

        [Test]
        public void BasicTest2(){
            var kata=new Kata();
            Assert.AreEqual(2, kata.CountNumber(10, 5));
        }

        [Test]
        public void BasicTest3(){
            var kata=new Kata();
            Assert.AreEqual(4, kata.CountNumber(6, 12));
        }

        [Test]
        public void BasicTest4(){
            var kata=new Kata();
            Assert.AreEqual(16, kata.CountNumber(100000, 1000000000));
        }

        [Test]
        public void BasicTest5(){
            var kata=new Kata();
            Assert.AreEqual(0,kata.CountNumber(9,484));
        }
                 
    }
}