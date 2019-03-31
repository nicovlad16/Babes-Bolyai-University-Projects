package domain.statement.FileStatements;


import domain.ProgramState;
import domain.adt.AdtException;
import domain.adt.MyDictionaryInterface;
import domain.adt.MyPair;
import domain.statement.StatementException;
import domain.statement.StatementInterface;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Set;


public class OpenStatement implements StatementInterface
{
    private String filename;
    private String varFileId;
    private static int uniqueKey = 1;


    public OpenStatement(String filename, String varFileId)
    {
        this.filename = filename;
        this.varFileId = varFileId;
    }


    @Override
    public ProgramState execute(ProgramState programState) throws StatementException
    {
        MyDictionaryInterface<Integer, MyPair> fileTable = programState.getFileTable();
        MyDictionaryInterface<String, Integer> symbolTable = programState.getSymbolTable();
        Set<Integer> keys = fileTable.keySet();

        for (Integer key : keys)
        {
            try
            {
                MyPair pair = fileTable.get(key);
                if (filename.equals(pair.getFirst().toString()))
                    throw new StatementException(filename + " already exists in the file table.\nFile already in use.");
            }
            catch (AdtException ignored)
            {
            }
        }

        try
        {
            MyPair<String, BufferedReader> pair = new MyPair<>(filename, new BufferedReader(new FileReader(filename)));
            fileTable.add(uniqueKey, pair);
            symbolTable.add(varFileId, uniqueKey);
            uniqueKey++;
        }
        catch (FileNotFoundException exception)
        {
            throw new StatementException("Error while openning file. " + filename);
        }
        catch (AdtException exception)
        {
            throw new StatementException(exception.getMessage());
        }

        return null;
    }


    @Override
    public String toString()
    {
        return "OpenRFile(" + varFileId + ",\"" + filename + "\")";
    }
}
