using MyInterpreter_CSharp.domain.adt;

namespace MyInterpreter_CSharp.domain.expression
{
    public abstract class Expression
    {
        public abstract int Eval(IMyDictionary<string, int> symbolTable);
    }
}