package domain.statement.LockStatements.Semaphore;


import domain.ProgramState;
import domain.statement.StatementException;
import domain.statement.StatementInterface;


public class AcquireStatement implements StatementInterface
{
    private String variable;


    public AcquireStatement(String variable)
    {
        this.variable = variable;
    }


    @Override
    public ProgramState execute(ProgramState programState) throws StatementException
    {
        return null;
    }


    @Override
    public String toString()
    {
        return "acquire(" + variable + ')';
    }
}
