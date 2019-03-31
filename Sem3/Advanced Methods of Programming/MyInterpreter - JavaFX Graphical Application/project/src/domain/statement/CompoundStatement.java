package domain.statement;


import domain.ProgramState;
import domain.adt.MyStackInterface;


public class CompoundStatement implements StatementInterface
{
    private StatementInterface first;
    private StatementInterface second;


    public CompoundStatement(StatementInterface first, StatementInterface second)
    {
        this.first = first;
        this.second = second;
    }


    @Override
    public String toString()
    {
        return "(" + first.toString() + ";" + second.toString() + ")";
    }


    @Override
    public ProgramState execute(ProgramState programState)
    {
        MyStackInterface<StatementInterface> stack = programState.getExeStack();
        stack.push(second);
        stack.push(first);
        return null;
    }
}
