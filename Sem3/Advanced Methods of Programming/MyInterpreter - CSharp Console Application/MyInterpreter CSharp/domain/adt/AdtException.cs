using System;

namespace MyInterpreter_CSharp.domain.adt
{
    public class AdtException : Exception
    {
        public AdtException(string message) : base(message)
        {
        }
    }
}