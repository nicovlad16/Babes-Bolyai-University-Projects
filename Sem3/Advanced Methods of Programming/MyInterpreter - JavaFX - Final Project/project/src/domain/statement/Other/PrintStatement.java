package domain.statement.Other;


import domain.ProgramState;
import domain.adt.MyDictionaryInterface;
import domain.adt.MyListInterface;
import domain.expression.Expression;
import domain.expression.ExpressionException;
import domain.statement.StatementException;
import domain.statement.StatementInterface;


public class PrintStatement implements StatementInterface
{
    private Expression expression;


    public PrintStatement(Expression expression)
    {
        this.expression = expression;
    }


    @Override
    public String toString()
    {
        return "print(" + expression.toString() + ")";
    }


    @Override
    public ProgramState execute(ProgramState programState) throws StatementException
    {
        MyListInterface<Integer> queue = programState.getOutput();
        MyDictionaryInterface<String, Integer> symbolTable = programState.getSymbolTable();
        MyDictionaryInterface<Integer, Integer> heapTable = programState.getHeapTable();
        try
        {
            queue.add(expression.evaluate(symbolTable, heapTable));
        }
        catch (ExpressionException exception)
        {
            throw new StatementException(exception.getMessage() + " Print statement.");
        }
        return null;
    }


    public Expression getExpression()
    {
        return expression;
    }
}
