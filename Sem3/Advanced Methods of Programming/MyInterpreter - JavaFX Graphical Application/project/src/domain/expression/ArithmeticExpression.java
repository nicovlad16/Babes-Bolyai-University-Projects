package domain.expression;


import domain.adt.MyDictionaryInterface;


public class ArithmeticExpression extends Expression
{
    private Expression e1;
    private Expression e2;
    private char operator;


    public ArithmeticExpression(Expression e1, Expression e2, char operator) throws ExpressionException
    {
        if (operator != '+' && operator != '-' && operator != '*' && operator != '/' && operator != '%')
            throw new ExpressionException("Invalid operator.");
        this.e1 = e1;
        this.e2 = e2;
        this.operator = operator;
    }


    @Override
    public int eval(MyDictionaryInterface<String, Integer> symbolTable,
                    MyDictionaryInterface<Integer, Integer> heapTable) throws ExpressionException
    {
        if (operator == '+')
            return e1.eval(symbolTable, heapTable) + e2.eval(symbolTable, heapTable);
        else if (operator == '-')
            return e1.eval(symbolTable, heapTable) - e2.eval(symbolTable, heapTable);
        else if (operator == '*')
            return e1.eval(symbolTable, heapTable) * e2.eval(symbolTable, heapTable);
        else if (e2.eval(symbolTable, heapTable) == 0)
            throw new ExpressionException("Divide by 0.");
        else if (operator == '/')
            return e1.eval(symbolTable, heapTable) / e2.eval(symbolTable, heapTable);
        else if (operator == '%')
            return e1.eval(symbolTable, heapTable) % e2.eval(symbolTable, heapTable);
        else
            return 0;
    }


    @Override
    public String toString()
    {
        return "(" + e1.toString() + operator + e2.toString() + ")";
    }
}
