package domain.adt;


import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;


public class MyList<TElement> implements MyListInterface<TElement>
{
    private Queue<TElement> list;


    public MyList()
    {
        list = new LinkedList<TElement>();
    }


    @Override
    public void add(TElement element)
    {
        list.add(element);
    }


    @Override
    public TElement pop() throws AdtException
    {
        if (list.isEmpty())
            throw new AdtException("Pop from empty list.");
        return list.poll();
    }


    @Override
    public TElement getFirstElement() throws AdtException
    {
        if (list.peek() != null)
            return list.peek();
        throw new AdtException("Peek on empty list.");
    }


    @Override
    public String toString()
    {
        String str = "";
        for (TElement element : list)
        {
            str += element.toString() + "\n";
        }
        return str;
    }


    @Override
    public List<TElement> getAll()
    {
        return new ArrayList<>(list);
    }
}