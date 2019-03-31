package domain.expression;


import domain.adt.MyDictionaryInterface;


public class ConstantExpression extends Expression
{
    private int number;


    public ConstantExpression(int number)
    {
        this.number = number;
    }


    @Override
    public int evaluate(MyDictionaryInterface<String, Integer> symbolTable,
                        MyDictionaryInterface<Integer, Integer> heapTable) throws ExpressionException
    {
        return number;
    }


    @Override
    public String toString()
    {
        return Integer.toString(number);
    }
}