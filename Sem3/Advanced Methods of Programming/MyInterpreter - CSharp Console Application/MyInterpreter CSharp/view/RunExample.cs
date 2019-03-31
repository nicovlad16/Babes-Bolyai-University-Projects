using System;
using MyInterpreter_CSharp.controller;

namespace MyInterpreter_CSharp.view
{
    public class RunExample : Command
    {
        private Controller _controller;
        public RunExample(string key, string description, Controller controller) : base(key, description)
        {
            _controller = controller;
        }

        public override void Execute()
        {
            try
            {
                _controller.AllStep();
                Console.WriteLine("Command executed successfully.");
            }
            catch (ControllerException exception)
            {
                Console.WriteLine(exception.Message);
            }
        }
    }
}