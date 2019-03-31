using System;

namespace MyInterpreter_CSharp.repository
{
    public class RepositoryException : Exception
    {
        public RepositoryException(string message) : base(message)
        {
        }
    }
}