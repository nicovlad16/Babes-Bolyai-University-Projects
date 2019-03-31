using System;
using System.Collections;
using MyInterpreter_CSharp.domain.adt;
using MyInterpreter_CSharp.domain.expression;

namespace MyInterpreter_CSharp.domain.statement
{
    public class IfStatement : IStatement
    {
        private Expression _expression;
        private IStatement _thenStatement;
        private IStatement _elseStatement;

        public IfStatement(Expression expression, IStatement thenStatement, IStatement elseStatement)
        {
            _expression = expression;
            _thenStatement = thenStatement;
            _elseStatement = elseStatement;
        }

        public ProgramState Execute(ProgramState programState)
        {
            IMyStack<IStatement> stack = programState.ExeStack;
            IMyDictionary<string, int> symbolTable = programState.SymbolTable;
            try
            {
                if (_expression.Eval(symbolTable) != 0)
                    stack.Push(_thenStatement);
                else
                    stack.Push(_elseStatement);
            }
            catch (ExpressionException exception)
            {
                throw new StatementException(exception.Message + " " + _expression);
            }

            return null;
        }

        public override string ToString()
        {
            return "IF(" + _expression + ")THEN(" + _thenStatement + ")ELSE(" + _elseStatement + ")";
        }
    }
}