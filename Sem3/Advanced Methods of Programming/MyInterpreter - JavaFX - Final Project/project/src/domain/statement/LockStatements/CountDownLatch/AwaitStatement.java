package domain.statement.LockStatements.CountDownLatch;


import domain.ProgramState;
import domain.adt.AdtException;
import domain.adt.MyDictionaryInterface;
import domain.statement.StatementException;
import domain.statement.StatementInterface;


public class AwaitStatement implements StatementInterface
{
    private String variable;


    public AwaitStatement(String variable)
    {
        this.variable = variable;
    }


    @Override
    public ProgramState execute(ProgramState programState) throws StatementException
    {
        MyDictionaryInterface<String, Integer> symbolTable = programState.getSymbolTable();

        try
        {
            int index = symbolTable.get(variable);
            synchronized (programState.getLatchTable())
            {
                int count = programState.getLatchTable().get(index);
                if (count > 0)
                    programState.getExeStack().push(this);
            }
        }
        catch (AdtException exception)
        {
            throw new StatementException(exception.getMessage() + "Count Down Statement.");
        }
        return null;
    }


    @Override
    public String toString()
    {
        return "await(" + variable + ')';
    }
}
