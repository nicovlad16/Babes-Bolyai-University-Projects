package domain.expression;


import domain.adt.AdtException;
import domain.adt.MyDictionaryInterface;


public class VariableExpression extends Expression
{
    private String id;


    public VariableExpression(String id)
    {
        this.id = id;
    }


    @Override
    public int evaluate(MyDictionaryInterface<String, Integer> symbolTable,
                        MyDictionaryInterface<Integer, Integer> heapTable) throws ExpressionException
    {
        try
        {
            return symbolTable.lookup(id);
        }
        catch (AdtException exception)
        {
            throw new ExpressionException(exception.getMessage() + " Variable expression.");
        }
    }


    @Override
    public String toString()
    {
        return id;
    }
}