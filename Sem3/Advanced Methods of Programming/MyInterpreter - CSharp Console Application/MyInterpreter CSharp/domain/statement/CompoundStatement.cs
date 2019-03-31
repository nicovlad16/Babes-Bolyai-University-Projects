using MyInterpreter_CSharp.domain.adt;

namespace MyInterpreter_CSharp.domain.statement
{
    public class CompoundStatement : IStatement
    {
        private IStatement _first;
        private IStatement _second;

        public CompoundStatement(IStatement first, IStatement second)
        {
            _first = first;
            _second = second;
        }


        public ProgramState Execute(ProgramState programState)
        {
            IMyStack<IStatement> stack = programState.ExeStack;
            stack.Push(_second);
            stack.Push(_first);
            return null;
        }

        public override string ToString()
        {
            return "(" + _first + ";" + _second + ")";
        }
    }
}