package controller;


import domain.ProgramState;
import domain.adt.*;
import domain.expression.ExpressionException;
import domain.expression.VariableExpression;
import domain.statement.File.CloseStatement;
import domain.statement.StatementException;
import domain.statement.StatementInterface;
import repository.Repository;
import repository.RepositoryException;
import repository.RepositoryInterface;

import java.util.*;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;


public class Controller
{
    private RepositoryInterface repository;
    private ExecutorService executor;


    public Controller(RepositoryInterface repository)
    {
        this.repository = repository;
    }


    public void addProgram(ProgramState programState)
    {
        repository.addProgram(programState);
    }


    private void oneStepForAllPrograms(List<ProgramState> programList) throws InterruptedException
    {
        programList.forEach(programState ->
        {
            try
            {
                repository.logProgramStateExec(programState);
            }
            catch (RepositoryException exception)
            {
//                System.out.println(exception.getMessage());
            }
        });

        List<Callable<ProgramState>> callList = programList
                .stream()
                .filter(program -> !program.getExeStack().isEmpty())
                .map((ProgramState program) -> (Callable<ProgramState>) (() ->
                {
                    try
                    {
                        return program.oneStep();
                    }
                    catch (StatementException exception)
                    {
                        System.out.println(exception.getMessage());
                        return null;
                    }
                }))
                .collect(Collectors.toList());

        List<ProgramState> newProgramList = executor
                .invokeAll(callList)
                .stream()
                .map(future ->
                {
                    try
                    {
                        return future.get();
                    }
                    catch (InterruptedException | ExecutionException exception)
                    {
                        System.out.println(exception.getMessage());
                        System.exit(1);
                        return null;
                    }
                })
                .filter(Objects::nonNull)
                .collect(Collectors.toList());

        programList.addAll(newProgramList);
        programList.forEach((program) ->
                {
                    try
                    {
                        program.getHeapTable()
                                .setContent(conservativeGarbageCollector(
                                        program.getSymbolTable(),
                                        program.getHeapTable()));
                        repository.logProgramStateExec(program);
                    }
                    catch (RepositoryException | AdtException exception)
                    {
                        System.out.println(exception.getMessage());
                    }
                }
        );
        repository.setProgramList(programList);

    }


    public void allSteps() throws InterruptedException, ControllerException
    {
        executor = Executors.newFixedThreadPool(2);
        List<ProgramState> programList = removeCompletedPrograms(repository.getProgramList());
        while (programList.size() > 0)
        {
            oneStepForAllPrograms(programList);
            programList = removeCompletedPrograms(repository.getProgramList());
        }
        closeAllOpenedFiles(repository.getCurrentProgram());
        try
        {
            repository.logProgramStateExec(repository.getCurrentProgram());
        }
        catch (RepositoryException exception)
        {
            throw new ControllerException(exception.getMessage());
        }
        executor.shutdownNow();
        repository.setProgramList(programList);
    }


    private void closeAllOpenedFiles(ProgramState programState)
    {
        MyDictionaryInterface<Integer, MyPair> fileTable = programState.getFileTable();
        MyDictionaryInterface<String, Integer> symbolTable = programState.getSymbolTable();

        List<Map.Entry<String, Integer>> keys = symbolTable.entrySet().stream()
                .filter(e -> fileTable.keySet().contains(e.getValue()))
                .collect(Collectors.toList());
        for (Map.Entry<String, Integer> e : keys)
            if (programState.getFileTable().containsKey(e.getValue()))
            {
                try
                {
                    new CloseStatement(new VariableExpression(e.getKey())).execute(programState);
                }
                catch (StatementException ignored)
                {
                }
            }
    }


    private Set conservativeGarbageCollector(MyDictionaryInterface<String, Integer> symbolTableValues,
                                             MyDictionaryInterface<Integer, Integer> heap)
    {
        return heap.entrySet().stream()
                .filter(e -> symbolTableValues.values().contains(e.getKey()))
                .collect(Collectors.toSet());
    }


    private List<ProgramState> removeCompletedPrograms(List<ProgramState> inProgramList)
    {
        return inProgramList.stream()
                .filter(ProgramState::isNotCompleted)
                .collect(Collectors.toList());
    }
}