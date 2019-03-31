package domain.adt;


public interface MyStackInterface<TElement>
{
    void push(TElement element);

    TElement pop() throws AdtException;

    TElement top() throws AdtException;

    boolean isEmpty();

    String toString();
}
