package domain.adt;


import java.util.ArrayList;
import java.util.List;
import java.util.Stack;


public class MyStack<TElement> implements MyStackInterface<TElement>
{
    private Stack<TElement> stack;


    public MyStack()
    {
        stack = new Stack<TElement>();
    }


    @Override
    public void push(TElement element)
    {
        stack.push(element);
    }


    @Override
    public TElement pop() throws AdtException
    {
        if (stack.empty())
            throw new AdtException("Pop from empty stack.");
        return stack.pop();
    }


    @Override
    public TElement top() throws AdtException
    {
        if (stack.empty())
            throw new AdtException("Top from empty stack.");
        return stack.peek();
    }


    @Override
    public boolean isEmpty()
    {
        return stack.empty();
    }


    @Override
    public String toString()
    {
        String str = "";
        Stack<TElement> stk = new Stack<TElement>();

        for (TElement element : stack)
        {
            stk.push(element);
        }

        for (TElement element : stk)
        {
            str += element.toString() + "\n";
        }
        return str;
    }


    @Override
    public List<TElement> getAll()
    {
        return new ArrayList<>(stack);
    }

}