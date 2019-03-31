using MyInterpreter_CSharp.domain.adt;

namespace MyInterpreter_CSharp.domain.expression
{
    public class ConstantExpression : Expression
    {
        private int _number;

        public ConstantExpression(int number)
        {
            this._number = number;
        }

        public override int Eval(IMyDictionary<string, int> symbolTable)
        {
            return _number;
        }

        public override string ToString()
        {
            return _number.ToString();
        }
    }
}