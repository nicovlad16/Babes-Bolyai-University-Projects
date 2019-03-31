using System;

namespace MyInterpreter_CSharp.domain.expression
{
    public class ExpressionException : Exception
    {
        public ExpressionException(string message) : base(message)
        {
        }   
    }
}