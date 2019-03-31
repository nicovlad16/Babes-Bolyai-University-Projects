package domain.statement.LockStatements.Semaphore;


import domain.ProgramState;
import domain.adt.AdtException;
import domain.adt.MyDictionaryInterface;
import domain.adt.MyPair;
import domain.expression.Expression;
import domain.expression.ExpressionException;
import domain.statement.StatementException;
import domain.statement.StatementInterface;

import java.util.ArrayList;


public class NewSemaphoreStatement implements StatementInterface
{
    private String variable;
    private Expression expression;
    private static int index = 1;


    public NewSemaphoreStatement(String variable, Expression expression)
    {
        this.variable = variable;
        this.expression = expression;
    }


    @Override
    public ProgramState execute(ProgramState programState) throws StatementException
    {
        MyDictionaryInterface<Integer, Integer> heapTable = programState.getHeapTable();
        MyDictionaryInterface<String, Integer> symbolTable = programState.getSymbolTable();
        MyDictionaryInterface<Integer, MyPair> semaphoreTable = programState.getSemaphoreTable();

        try
        {
            int number = expression.evaluate(symbolTable, heapTable);
            semaphoreTable.add(index, new MyPair(number, new ArrayList<>()));
            index++;
            if (symbolTable.containsKey(variable))
                symbolTable.update(variable, index);
            else
                symbolTable.add(variable, index);
        }
        catch (ExpressionException | AdtException exception)
        {
            throw new StatementException(exception.getMessage() + " New Semaphore Statement.");
        }

        return null;
    }


    @Override
    public String toString()
    {
        return "newSemaphore(" + variable + "," + expression + ')';
    }
}