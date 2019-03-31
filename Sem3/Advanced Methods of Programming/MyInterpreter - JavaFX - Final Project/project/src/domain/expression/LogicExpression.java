package domain.expression;


import domain.adt.MyDictionaryInterface;


public class LogicExpression extends Expression
{
    private Expression expression1;
    private Expression expression2;
    private String operation;


    public LogicExpression(Expression expression1, Expression expression2, String operation) throws ExpressionException
    {
        this.expression1 = expression1;
        this.expression2 = expression2;
        if (!operation.equals("and") && !operation.equals("or"))
            throw new ExpressionException("Invalid operation type.");
        this.operation = operation;
    }


    @Override
    public int evaluate(MyDictionaryInterface<String, Integer> symbolTable,
                        MyDictionaryInterface<Integer, Integer> heapTable) throws ExpressionException
    {
        int res1 = expression1.evaluate(symbolTable, heapTable);
        int res2 = expression2.evaluate(symbolTable, heapTable);

        switch (operation)
        {
            case "and":
                return res1 == res2 && res1 == 1 ? 1 : 0;
            case "or":
                return res1 == 1 || res2 == 1 ? 1 : 0;
            default:
                return 0;
        }
    }


    @Override
    public String toString()
    {
        return expression1 + operation + expression2;
    }
}
