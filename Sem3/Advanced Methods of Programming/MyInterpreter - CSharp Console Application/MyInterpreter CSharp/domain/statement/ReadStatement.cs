using System;
using System.IO;
using MyInterpreter_CSharp.domain.adt;
using MyInterpreter_CSharp.domain.expression;

namespace MyInterpreter_CSharp.domain.statement
{
    public class ReadStatement : IStatement
    {
        private Expression _expFileId;
        private string _varName;

        public ReadStatement(Expression expFileId, string varName)
        {
            _expFileId = expFileId;
            _varName = varName;
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
                int valueFromFile;
                string result = textReader.ReadLine();

                if (result == null)
                    valueFromFile = 0;
                else
                    valueFromFile = int.Parse(result);

                if (symbolTable.IsDefined(_varName))
                    symbolTable.Update(_varName, valueFromFile);
                else
                    symbolTable.Add(_varName, valueFromFile);
            }
            catch (ExpressionException exception)
            {
                throw new StatementException(exception.Message + " " + _expFileId);
            }
            catch (AdtException exception)
            {
                throw new StatementException(exception.Message + " " + _varName);
            }

            return null;
        }

        public override string ToString()
        {
            return "ReadFile(" + _expFileId + ", " + _varName + ')';
        }
    }
}