package domain.adt;


public interface MyListInterface<TElement>
{
    void add(TElement element);

    TElement pop() throws AdtException;

    TElement getFirstElement() throws AdtException;

    String toString();
}
