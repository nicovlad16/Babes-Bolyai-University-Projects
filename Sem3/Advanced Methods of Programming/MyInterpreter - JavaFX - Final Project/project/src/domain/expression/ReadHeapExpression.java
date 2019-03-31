package domain.expression;


import domain.adt.AdtException;
import domain.adt.MyDictionaryInterface;


public class ReadHeapExpression extends Expression
{
    private String varName;


    public ReadHeapExpression(String varName)
    {
        this.varName = varName;
    }


    @Override
    public String toString()
    {
        return "rH(" + varName + ')';
    }


    @Override
    public int evaluate(MyDictionaryInterface<String, Integer> symbolTable,
                        MyDictionaryInterface<Integer, Integer> heapTable) throws ExpressionException
    {
        try
        {
            Integer address = symbolTable.get(varName);
            return heapTable.get(address);
        }
        catch (AdtException exception)
        {
            throw new ExpressionException(exception.getMessage() + " Read Heap.");
        }
    }
}