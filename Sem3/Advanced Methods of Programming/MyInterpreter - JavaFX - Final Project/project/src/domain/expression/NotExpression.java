package domain.expression;


import domain.adt.MyDictionaryInterface;


public class NotExpression extends Expression
{
    private Expression expression;


    public NotExpression(Expression expression)
    {
        this.expression = expression;
    }


    @Override
    public int evaluate(MyDictionaryInterface<String, Integer> symbolTable,
                        MyDictionaryInterface<Integer, Integer> heapTable) throws ExpressionException
    {
        int res = expression.evaluate(symbolTable, heapTable);
        return res == 0 ? 1 : 0;
    }


    @Override
    public String toString()
    {
        return "(!" + expression + ")";
    }
}
