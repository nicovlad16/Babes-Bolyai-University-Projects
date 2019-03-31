package domain.statement.LockStatements.Semaphore;


import domain.ProgramState;
import domain.statement.StatementException;
import domain.statement.StatementInterface;


public class ReleaseStatement implements StatementInterface
{
    private String variable;


    public ReleaseStatement(String variable)
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
        return "release(" + variable + ')';
    }
}
