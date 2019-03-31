using MyInterpreter_CSharp.domain.adt;

namespace MyInterpreter_CSharp.domain.expression
{
    public class VariableExpression : Expression
    {
        private string _id;

        public VariableExpression(string id)
        {
            this._id = id;
        }

        public override int Eval(IMyDictionary<string, int> symbolTable)
        {
            try
            {
                return symbolTable.Lookup(_id);
            }
            catch (AdtException exception)
            {
                throw new ExpressionException(exception.Message + " " + _id);
            }
        }

        public override string ToString()
        {
            return _id;
        }
    }
}