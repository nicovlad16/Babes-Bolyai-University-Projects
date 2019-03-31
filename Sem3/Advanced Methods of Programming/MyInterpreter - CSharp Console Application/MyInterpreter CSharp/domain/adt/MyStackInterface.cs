using System;

namespace MyInterpreter_CSharp.domain.adt
{
    public interface IMyStack<TElement>
    {
        void Push(TElement element);
        TElement Pop();
        bool IsEmpty();
        string ToString();
    }
}