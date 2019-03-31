package domain.statement.Heap;


import domain.ProgramState;
import domain.adt.AdtException;
import domain.adt.MyDictionaryInterface;
import domain.expression.Expression;
import domain.expression.ExpressionException;
import domain.statement.StatementException;
import domain.statement.StatementInterface;


public class WriteStatement implements StatementInterface
{
    private String varName;
    private Expression expression;


    public WriteStatement(String varName, Expression expression)
    {
        this.varName = varName;
        this.expression = expression;
    }


    @Override
    public String toString()
    {
        return "wH(" + varName + "," + expression + ')';
    }


    @Override
    public ProgramState execute(ProgramState programState) throws StatementException
    {
        MyDictionaryInterface<String, Integer> symbolTable = programState.getSymbolTable();
        MyDictionaryInterface<Integer, Integer> heapTable = programState.getHeapTable();

        try
        {
            Integer address = symbolTable.get(varName);
            if (heapTable.containsKey(address))
                heapTable.update(address, expression.eval(symbolTable, heapTable));
            else
                heapTable.add(address, expression.eval(symbolTable, heapTable));
        }
        catch (AdtException | ExpressionException exception)
        {
            throw new StatementException(exception.getMessage() + " Write Statement." + varName + " " + expression);
        }
        return null;
    }
}