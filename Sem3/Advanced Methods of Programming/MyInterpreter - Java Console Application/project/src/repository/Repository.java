package repository;


import domain.ProgramState;
import domain.adt.AdtException;
import domain.adt.MyList;
import domain.adt.MyListInterface;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;


public class Repository implements RepositoryInterface
{
    private String logFilePath;
    private List<ProgramState> programList;


    public Repository(String logFilePath) throws RepositoryException
    {
        programList = new ArrayList<>();
        this.logFilePath = logFilePath;
        try
        {
            PrintWriter logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, false)));
            logFile.println("");
            logFile.close();
        }
        catch (IOException exception)
        {
            throw new RepositoryException("Cannot write to file." + logFilePath);
        }
    }


    @Override
    public void addProgram(ProgramState programState)
    {
        programList.add(programState);
    }


    @Override
    public void logProgramStateExec(ProgramState programState) throws RepositoryException
    {
        try
        {
            PrintWriter logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)));
            logFile.println(programState.toString());
            logFile.close();
        }
        catch (IOException exception)
        {
            throw new RepositoryException("Cannot write to file." + logFilePath);
        }
    }


    @Override
    public ProgramState getCurrentProgram()
    {
        return programList.get(0);
    }


    @Override
    public List<ProgramState> getProgramList()
    {
        return programList;
    }


    @Override
    public void setProgramList(List<ProgramState> programList)
    {
        this.programList = programList;
    }
}
