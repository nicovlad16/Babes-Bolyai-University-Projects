package domain.statement.Other;


import domain.ProgramState;
import domain.adt.MyStackInterface;
import domain.statement.StatementException;
import domain.statement.StatementInterface;


public class SleepStatement implements StatementInterface
{
    private int number;


    public SleepStatement(int number)
    {
        this.number = number;
    }


    @Override
    public ProgramState execute(ProgramState programState) throws StatementException
    {
        MyStackInterface<StatementInterface> exeStack = programState.getExeStack();
        if (number > 0)
        {
            SleepStatement sleepStatement = new SleepStatement(number - 1);
            exeStack.push(sleepStatement);
        }
        return null;
    }


    @Override
    public String toString()
    {
        return "sleep(" + number + ')';
    }
}
