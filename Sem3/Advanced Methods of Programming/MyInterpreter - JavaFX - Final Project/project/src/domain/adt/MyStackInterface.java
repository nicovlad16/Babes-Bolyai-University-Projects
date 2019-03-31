package domain.adt;


import java.util.List;


public interface MyStackInterface<TElement>
{
    void push(TElement element);

    TElement pop() throws AdtException;

    TElement top() throws AdtException;

    boolean isEmpty();

    String toString();

    List<TElement> getAll();
}
