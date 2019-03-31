namespace MyInterpreter_CSharp.domain.adt
{
    public class MyPair<T1, T2>
    {
        private T1 _first;
        private T2 _second;

        public MyPair(T1 first, T2 second)
        {
            _first = first;
            _second = second;
        }

        public T1 First => _first;

        public T2 Second => _second;

        public override string ToString()
        {
            return _first + " " + _second;
        }
    }
}