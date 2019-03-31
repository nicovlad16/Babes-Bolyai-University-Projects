namespace MyInterpreter_CSharp.domain.adt
{
    public abstract class IMyList<TElement>
    {
        public abstract void Add(TElement element);
        public abstract TElement GetFirstElement();
        public abstract string ToString();
    }
}