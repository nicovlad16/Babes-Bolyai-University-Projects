package domain.statement.ControlStatements;


import domain.ProgramState;
import domain.adt.MyStackInterface;
import domain.expression.Expression;
import domain.expression.NotExpression;
import domain.statement.Other.CompoundStatement;
import domain.statement.StatementException;
import domain.statement.StatementInterface;


public class RepeatStatement implements StatementInterface
{
    private StatementInterface statement;
    private Expression expression;


    public RepeatStatement(StatementInterface statement, Expression expression)
    {
        this.statement = statement;
        this.expression = expression;
    }


    @Override
    public ProgramState execute(ProgramState programState) throws StatementException
    {
        MyStackInterface<StatementInterface> exeStack = programState.getExeStack();
        StatementInterface whileStatement = new
                CompoundStatement(statement, new WhileStatement(new NotExpression(expression), statement));
        exeStack.push(whileStatement);

        return null;
    }


    @Override
    public String toString()
    {
        return "(repeat" + statement + "until" + expression + ")";
    }
}
