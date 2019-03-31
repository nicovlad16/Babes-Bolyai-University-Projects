namespace MyInterpreter_CSharp.view
{
    public abstract class Command
    {
        private string _key;
        private string _description;

        public Command(string key, string description)
        {
            _key = key;
            _description = description;
        }

        public abstract void Execute();

        public string Key => _key;

        public string Description => _description;
    }
}