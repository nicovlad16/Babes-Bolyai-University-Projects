package domain.statement.Other;


import domain.ProgramState;
import domain.adt.MyStackInterface;
import domain.expression.Expression;
import domain.statement.ControlStatements.IfStatement;
import domain.statement.Other.AssignStatement;
import domain.statement.StatementException;
import domain.statement.StatementInterface;


public class ConditionalAssignment implements StatementInterface
{
    private String variable;
    private Expression expression1;
    private Expression expression2;
    private Expression expression3;


    public ConditionalAssignment(String variable, Expression expression1, Expression expression2,
                                 Expression expression3)
    {
        this.variable = variable;
        this.expression1 = expression1;
        this.expression2 = expression2;
        this.expression3 = expression3;
    }


    @Override
    public ProgramState execute(ProgramState programState) throws StatementException
    {
        MyStackInterface<StatementInterface> exeStack = programState.getExeStack();
        StatementInterface ifStatement = new IfStatement(expression1,
                new AssignStatement(variable, expression2),
                new AssignStatement(variable, expression3));
        exeStack.push(ifStatement);
        return null;
    }


    @Override
    public String toString()
    {
        return variable + "=" + expression1 + "?" + expression2 + ":" + expression3;
    }
}
