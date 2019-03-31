using System;
using System.IO;
using MyInterpreter_CSharp.domain.adt;
using MyInterpreter_CSharp.domain.expression;

namespace MyInterpreter_CSharp.domain.statement
{
    public class CloseStatement : IStatement
    {
        private Expression _expFileId;

        public CloseStatement(Expression expFileId)
        {
            _expFileId = expFileId;
        }

        public ProgramState Execute(ProgramState programState)
        {
            IMyDictionary<int, MyPair<string, TextReader>> fileTable = programState.FileTable;
            IMyDictionary<string, int> symbolTable = programState.SymbolTable;
            try
            {
                int uniqueKey = _expFileId.Eval(symbolTable);
                MyPair<string, TextReader> myPair = fileTable.Lookup(uniqueKey);
                TextReader textReader = myPair.Second;
                textReader.Close();
                fileTable.Remove(uniqueKey);
            }
            catch (ExpressionException exception)
            {
                throw new StatementException(exception.Message + " " + _expFileId);
            }

            return null;
        }

        public override string ToString()
        {
            return "CloseFile(" + _expFileId + ')';
        }
    }
}