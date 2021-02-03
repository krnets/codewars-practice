namespace CustomAccessors
{
    public class DemoClass
    {
        private int _privateField;
        public string PublicField = "None";
        public int LimitedProperty { get; private set; }

        public DemoClass(int input)
        {
            _privateField = input;
        }
    }
}