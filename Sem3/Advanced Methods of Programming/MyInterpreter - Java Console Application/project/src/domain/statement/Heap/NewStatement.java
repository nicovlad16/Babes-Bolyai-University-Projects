package domain.statement.Heap;


import domain.ProgramState;
import domain.adt.AdtException;
import domain.adt.MyDictionaryInterface;
import domain.expression.Expression;
import domain.expression.ExpressionException;
import domain.statement.StatementException;
import domain.statement.StatementInterface;


public class NewStatement implements StatementInterface
{
    private String varName;
    private Expression expression;


    public NewStatement(String varName, Expression expression)
    {
        this.varName = varName;
        this.expression = expression;
    }


    @Override
    public ProgramState execute(ProgramState programState) throws StatementException
    {
        MyDictionaryInterface<String, Integer> symbolTable = programState.getSymbolTable();
        MyDictionaryInterface<Integer, Integer> heapTable = programState.getHeapTable();

        Integer heapAddress = programState.getNewAddress();
        try
        {
            heapTable.add(heapAddress, expression.eval(symbolTable, heapTable));
            if (symbolTable.containsKey(varName))
                symbolTable.update(varName, heapAddress);
            else
                symbolTable.add(varName, heapAddress);
        } catch (AdtException | ExpressionException exception)
        {
            throw new StatementException(exception.getMessage() + " Heap allocation." + varName + expression);
        }
        return null;
    }


    @Override
    public String toString()
    {
        return "new(" + varName + "," + expression + ')';
    }
}
