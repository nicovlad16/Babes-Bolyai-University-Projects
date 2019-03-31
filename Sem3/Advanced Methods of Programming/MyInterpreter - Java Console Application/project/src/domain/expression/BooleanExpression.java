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
    public int eval(MyDictionaryInterface<String, Integer> symbolTable,
                    MyDictionaryInterface<Integer, Integer> heapTable) throws ExpressionException
    {
        switch (operation)
        {
            case "==":
                if (expression1.eval(symbolTable, heapTable) == expression2.eval(symbolTable, heapTable))
                    return 1;
                return 0;
            case "!=":
                if (expression1.eval(symbolTable, heapTable) != expression2.eval(symbolTable, heapTable))
                    return 1;
                return 0;
            case "<":
                if (expression1.eval(symbolTable, heapTable) < expression2.eval(symbolTable, heapTable))
                    return 1;
                return 0;
            case "<=":
                if (expression1.eval(symbolTable, heapTable) <= expression2.eval(symbolTable, heapTable))
                    return 1;
                return 0;
            case ">":
                if (expression1.eval(symbolTable, heapTable) > expression2.eval(symbolTable, heapTable))
                    return 1;
                return 0;
            case ">=":
                if (expression1.eval(symbolTable, heapTable) >= expression2.eval(symbolTable, heapTable))
                    return 1;
                return 0;
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
