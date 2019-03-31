package domain.adt;


import java.util.List;


public interface MyListInterface<TElement>
{
    void add(TElement element);

    TElement pop() throws AdtException;

    TElement getFirstElement() throws AdtException;

    String toString();

    List<TElement> getAll();
}
