using System;

namespace MyInterpreter_CSharp.controller
{
    public class ControllerException : Exception
    {
        public ControllerException(string message) : base(message)
        {
        }
    }
}