package domain.statement;


import domain.ProgramState;
import domain.adt.MyDictionaryInterface;
import domain.adt.MyListInterface;
import domain.expression.Expression;
import domain.expression.ExpressionException;


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
            queue.add(expression.eval(symbolTable, heapTable));
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
