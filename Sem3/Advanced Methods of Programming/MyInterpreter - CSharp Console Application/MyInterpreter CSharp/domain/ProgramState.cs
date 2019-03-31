using System.IO;
using MyInterpreter_CSharp.domain.adt;
using MyInterpreter_CSharp.domain.statement;

namespace MyInterpreter_CSharp.domain
{
    public class ProgramState
    {
        private IMyStack<IStatement> _exeStack;
        private IMyDictionary<string, int> _symbolTable;
        private IMyList<int> _output;
        private IMyDictionary<int, MyPair<string, TextReader>> _fileTable;

        public ProgramState(
            IMyStack<IStatement> exeStack,
            IMyDictionary<string, int> symbolTable,
            IMyList<int> output,
            IMyDictionary<int, MyPair<string, TextReader>> fileTable,
            IStatement program)
        {
            _exeStack = exeStack;
            _symbolTable = symbolTable;
            _output = output;
            _fileTable = fileTable;
            exeStack.Push(program);
        }

        public IMyStack<IStatement> ExeStack => _exeStack;

        public IMyDictionary<string, int> SymbolTable => _symbolTable;

        public IMyList<int> Output => _output;

        public IMyDictionary<int, MyPair<string, TextReader>> FileTable => _fileTable;

        public override string ToString()
        {
            return "ExeStack:\n" + _exeStack.ToString() +
                   "SymbolTable:\n" + _symbolTable.ToString() +
                   "FileTable:\n" + _fileTable.ToString() +
                   "Print output:\n" + _output.ToString();
        }
    }
}