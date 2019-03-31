package domain.statement;


import domain.ProgramState;
import domain.adt.MyDictionaryInterface;
import domain.adt.MyStackInterface;
import domain.expression.Expression;
import domain.expression.ExpressionException;


public class WhileStatement implements StatementInterface
{
    private Expression expression;
    private StatementInterface statement;


    public WhileStatement(Expression expression, StatementInterface statement)
    {
        this.expression = expression;
        this.statement = statement;
    }


    @Override
    public ProgramState execute(ProgramState programState) throws StatementException
    {
        MyDictionaryInterface<String, Integer> symbolTable = programState.getSymbolTable();
        MyDictionaryInterface<Integer, Integer> heapTable = programState.getHeapTable();
        MyStackInterface<StatementInterface> stack = programState.getExeStack();

        try
        {
            if (expression.eval(symbolTable, heapTable) != 0)
            {
                stack.push(this);
                programState.setExeStack(stack);
                statement.execute(programState);
            }
        }
        catch (ExpressionException exception)
        {
            throw new StatementException(exception.getMessage() + " While statement.");
        }
        return null;
    }


    @Override
    public String toString()
    {
        return "(while" + expression.toString() + "" + statement.toString() + ')';
    }
}
