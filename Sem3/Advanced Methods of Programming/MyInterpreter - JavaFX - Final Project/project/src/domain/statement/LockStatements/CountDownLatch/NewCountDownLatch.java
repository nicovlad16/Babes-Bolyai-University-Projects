package domain.statement.LockStatements.CountDownLatch;


import domain.ProgramState;
import domain.adt.AdtException;
import domain.adt.MyDictionary;
import domain.adt.MyDictionaryInterface;
import domain.expression.Expression;
import domain.expression.ExpressionException;
import domain.statement.StatementException;
import domain.statement.StatementInterface;


public class NewCountDownLatch implements StatementInterface
{
    private String variable;
    private Expression expression;
    private static int index = 0;


    public NewCountDownLatch(String variable, Expression expression)
    {
        this.variable = variable;
        this.expression = expression;
    }


    @Override
    public ProgramState execute(ProgramState programState) throws StatementException
    {
        MyDictionaryInterface<String, Integer> symbolTable = programState.getSymbolTable();
        MyDictionaryInterface<Integer, Integer> heapTable = programState.getHeapTable();

        try
        {
            int number = expression.evaluate(symbolTable, heapTable);
            synchronized (programState.getLatchTable())
            {
                programState.getLatchTable().add(index, number);

                if (symbolTable.containsKey(variable))
                    symbolTable.update(variable, index);
                else
                    symbolTable.add(variable, index);
                index++;
            }
        }
        catch (ExpressionException | AdtException exception)
        {
            throw new StatementException(exception.getMessage() + " New Latch Statement.");
        }
        return null;
    }


    @Override
    public String toString()
    {
        return "newLatch(" + variable + "," + expression + ')';
    }
}
