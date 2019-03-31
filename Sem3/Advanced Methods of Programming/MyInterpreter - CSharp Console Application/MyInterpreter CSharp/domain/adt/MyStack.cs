using System.Collections.Generic;

namespace MyInterpreter_CSharp.domain.adt
{
    public class MyStack<TElement> : IMyStack<TElement>
    {
        private Stack<TElement> _stack;

        public MyStack()
        {
            _stack = new Stack<TElement>();
        }

        public void Push(TElement element)
        {
            _stack.Push(element);
        }

        public TElement Pop()
        {
            if (_stack.Count == 0)
                throw new AdtException("Pop from empty stack.");
            return _stack.Pop();
        }

        public bool IsEmpty()
        {
            return _stack.Count == 0;
        }

        public override string ToString()
        {
            string str = "";
            Stack<TElement> stk = new Stack<TElement>();

            foreach (TElement element in _stack)
            {
                stk.Push(element);
            }

            foreach (TElement element in stk)
            {
                str += element + "\n";
            }

            return str;
        }
    }
}