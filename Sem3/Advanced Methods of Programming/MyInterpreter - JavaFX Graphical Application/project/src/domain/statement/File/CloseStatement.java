package domain.statement.File;


import domain.ProgramState;
import domain.adt.AdtException;
import domain.adt.MyDictionaryInterface;
import domain.adt.MyPair;
import domain.expression.Expression;
import domain.expression.ExpressionException;
import domain.statement.StatementException;
import domain.statement.StatementInterface;

import java.io.BufferedReader;
import java.io.IOException;


public class CloseStatement implements StatementInterface
{
    private Expression expFileId;


    public CloseStatement(Expression expFileId)
    {
        this.expFileId = expFileId;
    }


    @Override
    public ProgramState execute(ProgramState programState) throws StatementException
    {
        MyDictionaryInterface<Integer, MyPair> fileTable = programState.getFileTable();
        MyDictionaryInterface<String, Integer> symbolTable = programState.getSymbolTable();
        MyDictionaryInterface<Integer, Integer> heapTable = programState.getHeapTable();
        try
        {
            int uniqueKey = expFileId.eval(symbolTable, heapTable);
            MyPair pair = fileTable.lookup(uniqueKey);
            BufferedReader reader = (BufferedReader) pair.getSecond();
            reader.close();
            fileTable.remove(uniqueKey);
        }
        catch (ExpressionException | AdtException exception)
        {
            throw new StatementException(exception.getMessage());
        }
        catch (IOException exception)
        {
            throw new StatementException("Cannot close file. " + expFileId.toString());
        }
        return null;
    }


    @Override
    public String toString()
    {
        return "CloseFile(" + expFileId.toString() + ')';
    }
}
