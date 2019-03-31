package domain.statement;


import domain.ProgramState;
import domain.adt.AdtException;
import domain.adt.MyDictionaryInterface;
import domain.expression.Expression;
import domain.expression.ExpressionException;


public class AssignStatement implements StatementInterface
{
    private String id;
    private Expression expression;


    public AssignStatement(String id, Expression expression)
    {
        this.id = id;
        this.expression = expression;
    }


    @Override
    public String toString()
    {
        return id + "=" + expression.toString();
    }


    @Override
    public ProgramState execute(ProgramState programState) throws StatementException
    {
        MyDictionaryInterface<String, Integer> symbolTable = programState.getSymbolTable();
        MyDictionaryInterface<Integer, Integer> heapTable = programState.getHeapTable();
        try
        {
            int val = expression.eval(symbolTable, heapTable);
            if (symbolTable.isDefined(id))
                symbolTable.update(id, val);
            else
                symbolTable.add(id, val);
        }
        catch (ExpressionException | AdtException exception)
        {
            throw new StatementException(exception.getMessage() + " Assign Statement.");
        }
        return null;
    }


    public Expression getExpression()
    {
        return expression;
    }
}
