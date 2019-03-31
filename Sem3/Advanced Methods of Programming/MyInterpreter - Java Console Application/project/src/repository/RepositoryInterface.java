package repository;


import domain.ProgramState;
import domain.adt.MyList;
import domain.adt.MyListInterface;

import java.util.List;


public interface RepositoryInterface
{
    void addProgram(ProgramState programState);

    List<ProgramState> getProgramList();

    void setProgramList(List<ProgramState> programList);

    void logProgramStateExec(ProgramState programState) throws RepositoryException;

    String toString();

    ProgramState getCurrentProgram();
}
