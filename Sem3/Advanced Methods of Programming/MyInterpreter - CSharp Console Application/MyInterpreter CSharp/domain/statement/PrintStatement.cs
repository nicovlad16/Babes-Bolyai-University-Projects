using System;
using MyInterpreter_CSharp.domain.adt;
using MyInterpreter_CSharp.domain.expression;

namespace MyInterpreter_CSharp.domain.statement
{
    public class PrintStatement : IStatement
    {
        private Expression _expression;

        public PrintStatement(Expression expression)
        {
            _expression = expression;
        }

        public ProgramState Execute(ProgramState programState)
        {
            IMyList<int> queue = programState.Output;
            IMyDictionary<string, int> symbolTable = programState.SymbolTable;
            try
            {
                queue.Add(_expression.Eval(symbolTable));
            }
            catch (ExpressionException exception)
            {
                throw new StatementException(exception.Message + " " + _expression);
            }

            return null;
        }

        public override string ToString()
        {
            return "print(" + _expression + ")";
        }

        public Expression Expression => _expression;
    }
}