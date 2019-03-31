using System;

namespace MyInterpreter_CSharp.domain.statement
{
    public class StatementException : Exception
    {
        public StatementException(string message) : base(message)
        {
        }
    }
}