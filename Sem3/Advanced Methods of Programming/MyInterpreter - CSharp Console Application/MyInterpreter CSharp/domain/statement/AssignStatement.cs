using System;
using MyInterpreter_CSharp.domain.adt;
using MyInterpreter_CSharp.domain.expression;

namespace MyInterpreter_CSharp.domain.statement
{
    public class AssignStatement : IStatement
    {
        private string _id;
        private Expression _expression;

        public AssignStatement(string id, Expression expression)
        {
            _id = id;
            _expression = expression;
        }

        public ProgramState Execute(ProgramState programState)
        {
            IMyDictionary<string, int> symbolTable = programState.SymbolTable;
            try
            {
                int value = _expression.Eval(symbolTable);
                if (symbolTable.IsDefined(_id))
                    symbolTable.Update(_id, value);
                else
                    symbolTable.Add(_id, value);
            }
            catch (ExpressionException exception)
            {
                throw new StatementException(exception.Message + " " + _expression);
            }
            catch (AdtException exception)
            {
                throw new StatementException(exception.Message + " " + _id);
            }

            return null;
        }

        public override string ToString()
        {
            return _id + "=" + _expression;
        }

        public Expression Expression => _expression;
    }
}