package domain.statement.Other;


import domain.ProgramState;
import domain.adt.MyStack;
import domain.statement.StatementException;
import domain.statement.StatementInterface;


public class ForkStatement implements StatementInterface
{
    private StatementInterface statement;
    private static int index = 1;


    public ForkStatement(StatementInterface statement)
    {
        this.statement = statement;
    }


    @Override
    public ProgramState execute(ProgramState programState) throws StatementException
    {
        if (programState == null)
            throw new StatementException("Invalid program state.");
        index++;
        return new ProgramState(new MyStack<>(),
                programState.getSymbolTable().cloneDictionary(),
                programState.getOutput(),
                programState.getFileTable(),
                programState.getHeapTable(),
                programState.getSemaphoreTable(),
                programState.getLatchTable(),
                index,
                statement);
    }


    @Override
    public String toString()
    {
        return "fork(" + statement + ")";
    }
}
