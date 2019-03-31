package domain.statement.LockStatements.CountDownLatch;


import domain.ProgramState;
import domain.adt.AdtException;
import domain.adt.MyDictionaryInterface;
import domain.adt.MyListInterface;
import domain.statement.StatementException;
import domain.statement.StatementInterface;


public class CountDownStatement implements StatementInterface
{
    private String variable;


    public CountDownStatement(String variable)
    {
        this.variable = variable;
    }


    @Override
    public ProgramState execute(ProgramState programState) throws StatementException
    {
        MyDictionaryInterface<String, Integer> symbolTable = programState.getSymbolTable();
        MyListInterface<Integer> output = programState.getOutput();

        try
        {
            int index = symbolTable.get(variable);
            synchronized (programState.getLatchTable())
            {
                if (!programState.getLatchTable().containsKey(index))
                    return null;

                int count = programState.getLatchTable().get(index);
                if (count > 0)
                {
                    programState.getLatchTable().update(index, count - 1);
                    output.add(programState.getThreadID());
                }
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
        return "countDown(" + variable + ')';
    }
}
