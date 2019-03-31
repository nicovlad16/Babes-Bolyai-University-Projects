package domain.statement.ControlStatements;


import domain.ProgramState;
import domain.adt.MyStackInterface;
import domain.expression.BooleanExpression;
import domain.expression.Expression;
import domain.expression.ExpressionException;
import domain.expression.VariableExpression;
import domain.statement.Other.AssignStatement;
import domain.statement.Other.CompoundStatement;
import domain.statement.StatementException;
import domain.statement.StatementInterface;


public class ForStatement implements StatementInterface
{

    private String comparator;
    private String variable;
    private Expression expression1;
    private Expression expression2;
    private Expression expression3;
    private StatementInterface statement;


    public ForStatement(String variable, String comparator, Expression expression1, Expression expression2, Expression expression3, StatementInterface statement)
    {
        this.variable = variable;
        this.comparator = comparator;
        this.expression1 = expression1;
        this.expression2 = expression2;
        this.expression3 = expression3;
        this.statement = statement;
    }


    public String getVariable()
    {
        return variable;
    }


    public Expression getExpression1()
    {
        return expression1;
    }


    public Expression getExpression2()
    {
        return expression2;
    }


    public Expression getExpression3()
    {
        return expression3;
    }


    public StatementInterface getStatement()
    {
        return statement;
    }


    @Override
    public ProgramState execute(ProgramState programState) throws StatementException
    {
        MyStackInterface<StatementInterface> exeStack = programState.getExeStack();
        try
        {
            StatementInterface newStatement = new CompoundStatement(
                    new AssignStatement(variable, expression1),
                    new WhileStatement(
                            new BooleanExpression(new VariableExpression(variable), expression2, comparator),
                            new CompoundStatement(statement, new AssignStatement(variable, expression3)))
            );

            exeStack.push(newStatement);
        }
        catch (ExpressionException exception)
        {
            throw new StatementException(exception.getMessage());
        }
        return null;
    }


    @Override
    public String toString()
    {
        return "(for(" + variable + "=" + expression1 + ";" +
                variable + "<" + expression2 + ";" + variable + "=" + expression3 +
                ")" + statement + ")";
    }
}