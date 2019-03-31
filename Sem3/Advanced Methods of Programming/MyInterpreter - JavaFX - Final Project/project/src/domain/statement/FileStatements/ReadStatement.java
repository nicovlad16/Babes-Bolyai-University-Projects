package domain.statement.FileStatements;


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


public class ReadStatement implements StatementInterface
{
    private Expression expFileId;
    private String varName;


    public ReadStatement(Expression expFileId, String varName)
    {
        this.expFileId = expFileId;
        this.varName = varName;
    }


    @Override
    public ProgramState execute(ProgramState programState) throws StatementException
    {
        MyDictionaryInterface<Integer, MyPair> fileTable = programState.getFileTable();
        MyDictionaryInterface<String, Integer> symbolTable = programState.getSymbolTable();
        MyDictionaryInterface<Integer, Integer> heapTable = programState.getHeapTable();
        try
        {
            int uniqueKey = expFileId.evaluate(symbolTable, heapTable);
            MyPair pair = fileTable.lookup(uniqueKey);
            BufferedReader reader = (BufferedReader) pair.getSecond();
            int valueFromFile;
            String result = reader.readLine();

            if (result == null)
                valueFromFile = 0;
            else
                valueFromFile = Integer.parseInt(result);

            if (symbolTable.isDefined(varName))
                symbolTable.update(varName, valueFromFile);
            else
                symbolTable.add(varName, valueFromFile);
        }
        catch (ExpressionException | AdtException exception)
        {
            throw new StatementException(exception.getMessage());
        }
        catch (IOException exception)
        {
            throw new StatementException("Cannot read from BufferedReader.");
        }
        return null;
    }


    @Override
    public String toString()
    {
        return "ReadFile(" + expFileId + "," + varName + ')';
    }
}
