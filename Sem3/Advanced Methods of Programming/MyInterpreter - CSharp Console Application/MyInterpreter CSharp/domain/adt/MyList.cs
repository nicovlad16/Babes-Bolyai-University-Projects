using System.Collections.Generic;

namespace MyInterpreter_CSharp.domain.adt
{
    public class MyList<TElement> : IMyList<TElement>
    {
        private Queue<TElement> _list;

        public MyList()
        {
            _list = new Queue<TElement>();
        }

        public override void Add(TElement element)
        {
            _list.Enqueue(element);
        }

        public override TElement GetFirstElement()
        {
            if (_list.Peek() != null)
                return _list.Peek();
            throw new AdtException("Peek on empty list.");
        }

        public override string ToString()
        {
            string str = "";
            foreach (var element in _list)
            {
                str += element + "\n";
            }

            return str;
        }
    }
}