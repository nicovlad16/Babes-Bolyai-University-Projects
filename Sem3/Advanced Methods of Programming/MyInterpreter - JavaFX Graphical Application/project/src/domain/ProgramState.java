package domain;


import domain.adt.*;
import domain.statement.Heap.HeapAddressBuilder;
import domain.statement.StatementException;
import domain.statement.StatementInterface;

import java.util.ArrayList;


public class ProgramState
{
    private MyStackInterface<StatementInterface> exeStack;
    private MyDictionaryInterface<String, Integer> symbolTable;
    private MyListInterface<Integer> outputList;
    private StatementInterface originalProgram; //optional
    private MyDictionaryInterface<Integer, MyPair> fileTable;
    private MyDictionaryInterface<Integer, Integer> heapTable;
    private HeapAddressBuilder addressBuilder = new HeapAddressBuilder();


    public int getThreadID()
    {
        return threadID;
    }


    private int threadID;


    public ProgramState(MyStackInterface<StatementInterface> exeStack,
                        MyDictionaryInterface<String, Integer> symbolTable,
                        MyListInterface<Integer> outputList,
                        MyDictionaryInterface<Integer, MyPair> fileTable,
                        MyDictionaryInterface<Integer, Integer> heapTable,
                        Integer threadID,
                        StatementInterface program)

    {
        this.exeStack = exeStack;
        this.symbolTable = symbolTable;
        this.outputList = outputList;
        //this.originalProgram = deepCopy(program);
        this.fileTable = fileTable;
        this.heapTable = heapTable;
        this.threadID = threadID;
        exeStack.push(program);
    }


    public ProgramState(StatementInterface statementInterface)
    {
        exeStack = new MyStack<>();
        symbolTable = new MyDictionary<>();
        outputList = new MyList<>();
        fileTable = new MyDictionary<>();
        heapTable = new MyDictionary<>();
        originalProgram = statementInterface;

        exeStack.push(originalProgram);
    }


    public MyStackInterface<StatementInterface> getExeStack()
    {
        return exeStack;
    }


    public MyDictionaryInterface<String, Integer> getSymbolTable()
    {
        return symbolTable;
    }


    public void setSymbolTable(MyDictionaryInterface<String, Integer> symbolTable)
    {
        this.symbolTable = symbolTable;
    }


    public MyListInterface<Integer> getOutput()
    {
        return outputList;
    }


    public StatementInterface getOriginalProgram()
    {
        return originalProgram;
    }


    public MyDictionaryInterface<Integer, MyPair> getFileTable()
    {
        return fileTable;
    }


    public MyDictionaryInterface<Integer, Integer> getHeapTable()
    {
        return heapTable;
    }


    @Override
    public String toString()
    {
        return "threadID: " + threadID + "\n" +
                "ExeStack:\n" + exeStack.toString() +
                "SymbolTable:\n" + symbolTable.toString() +
                "Print output:\n" + outputList.toString() +
                "FileTable:\n" + fileTable.toString() +
                "HeapTable:\n" + heapTable.toString();
    }


    public Integer getNewAddress()
    {
        return addressBuilder.getFreeAddress();
    }


    public void setExeStack(MyStackInterface<StatementInterface> exeStack)
    {
        this.exeStack = exeStack;
    }


    public boolean isNotCompleted()
    {
        return !exeStack.isEmpty();
    }


    public ProgramState oneStep() throws StatementException
    {
        try
        {
            StatementInterface currentStatement = exeStack.pop();
            return currentStatement.execute(this);
        }
        catch (AdtException exception)
        {
            throw new StatementException(exception.getMessage());
        }
    }
}