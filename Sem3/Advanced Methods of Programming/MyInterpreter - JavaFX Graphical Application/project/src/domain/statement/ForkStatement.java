package domain.statement;


import domain.ProgramState;
import domain.adt.MyStack;


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
                index,
                statement);
    }


    @Override
    public String toString()
    {
        return "fork(" + statement + ")";
    }
}
