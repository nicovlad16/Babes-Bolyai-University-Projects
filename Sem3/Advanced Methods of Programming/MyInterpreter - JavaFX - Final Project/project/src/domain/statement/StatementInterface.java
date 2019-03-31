package domain.statement;


import domain.ProgramState;


public interface StatementInterface
{
    ProgramState execute(ProgramState programState) throws StatementException;

    String toString();
}
