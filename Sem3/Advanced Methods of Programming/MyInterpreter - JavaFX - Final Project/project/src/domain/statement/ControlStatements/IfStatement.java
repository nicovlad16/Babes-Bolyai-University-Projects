package domain.statement.ControlStatements;


import domain.ProgramState;
import domain.adt.MyDictionaryInterface;
import domain.adt.MyStackInterface;
import domain.expression.Expression;
import domain.expression.ExpressionException;
import domain.statement.StatementException;
import domain.statement.StatementInterface;


public class IfStatement implements StatementInterface
{
    private Expression expression;
    private StatementInterface thenStatement;
    private StatementInterface elseStatement;


    public IfStatement(Expression expression, StatementInterface thenStatement,
                       StatementInterface elseStatement)
    {
        this.expression = expression;
        this.thenStatement = thenStatement;
        this.elseStatement = elseStatement;
    }


    @Override
    public String toString()
    {
        return "IF(" + expression.toString() + ")THEN(" + thenStatement.toString()
                + ")ELSE(" + elseStatement.toString() + ")";
    }


    @Override
    public ProgramState execute(ProgramState programState) throws StatementException
    {
        MyStackInterface<StatementInterface> stack = programState.getExeStack();
        MyDictionaryInterface<String, Integer> symbolTable = programState.getSymbolTable();
        MyDictionaryInterface<Integer, Integer> heapTable = programState.getHeapTable();
        try
        {
            if (expression.evaluate(symbolTable, heapTable) != 0)
                stack.push(thenStatement);
            else
                stack.push(elseStatement);
        }
        catch (ExpressionException exception)
        {
            throw new StatementException(exception.getMessage() + " If statement.");
        }
        return null;
    }


    public Expression getExpression()
    {
        return expression;
    }
}
