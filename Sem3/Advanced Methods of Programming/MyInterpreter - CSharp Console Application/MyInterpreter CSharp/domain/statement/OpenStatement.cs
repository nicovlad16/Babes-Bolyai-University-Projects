using System.IO;
using MyInterpreter_CSharp.domain.adt;

namespace MyInterpreter_CSharp.domain.statement
{
    public class OpenStatement : IStatement
    {
        private string _filename;
        private string _varFileId;
        private static int _uniqueKey = 1;

        public OpenStatement(string filename, string varFileId)
        {
            _filename = filename;
            _varFileId = varFileId;
        }

        public ProgramState Execute(ProgramState programState)
        {
            IMyDictionary<int, MyPair<string, TextReader>> fileTable = programState.FileTable;
            IMyDictionary<string, int> symbolTable = programState.SymbolTable;
            MyPair<string, TextReader> myPair;

            foreach (int key in fileTable.GetKeys())
            {
                myPair = fileTable.Get(key);
                if (myPair.First == _filename)
                    throw new StatementException("File already open.");
            }

            TextReader textReader = File.OpenText(_filename);
            myPair = new MyPair<string, TextReader>(_filename, textReader);
            fileTable.Add(_uniqueKey, myPair);
            symbolTable.Add(_varFileId, _uniqueKey);
            _uniqueKey++;

            return null;
        }

        public override string ToString()
        {
            return "openRFile(" + _varFileId + ",\"" + _filename + "\"";
        }
    }
}