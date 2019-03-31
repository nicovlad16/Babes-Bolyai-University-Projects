package domain.expression;


import domain.adt.MyDictionaryInterface;


public class BooleanExpression extends Expression
{
    private Expression expression1;
    private Expression expression2;
    private String operation;


    public BooleanExpression(Expression expression1, Expression expression2, String operation)
            throws ExpressionException
    {
        this.expression1 = expression1;
        this.expression2 = expression2;
        if (!operation.equals("<") && !operation.equals("<=") &&
                !operation.equals(">") && !operation.equals(">=") &&
                !operation.equals("==") && !operation.equals("!="))
            throw new ExpressionException("Invalid operation.");
        this.operation = operation;
    }


    @Override
    public int evaluate(MyDictionaryInterface<String, Integer> symbolTable,
                        MyDictionaryInterface<Integer, Integer> heapTable) throws ExpressionException
    {
        switch (operation)
        {
            case "==":
                return expression1.evaluate(symbolTable, heapTable) == expression2.evaluate(symbolTable, heapTable) ? 1 : 0;
            case "!=":
                return expression1.evaluate(symbolTable, heapTable) != expression2.evaluate(symbolTable, heapTable) ? 1 : 0;
            case "<":
                return expression1.evaluate(symbolTable, heapTable) < expression2.evaluate(symbolTable, heapTable) ? 1 : 0;
            case "<=":
                return expression1.evaluate(symbolTable, heapTable) <= expression2.evaluate(symbolTable, heapTable) ? 1 : 0;
            case ">":
                return expression1.evaluate(symbolTable, heapTable) > expression2.evaluate(symbolTable, heapTable) ? 1 : 0;
            case ">=":
                return expression1.evaluate(symbolTable, heapTable) >= expression2.evaluate(symbolTable, heapTable) ? 1 : 0;
            default:
                return 0;
        }
    }


    @Override
    public String toString()
    {
        return "(" + expression1.toString() + operation + expression2.toString() + ")";
    }
}
