using System.IO;
using MyInterpreter_CSharp.domain;
using MyInterpreter_CSharp.domain.adt;

namespace MyInterpreter_CSharp.repository
{
    public class Repository : IRepository
    {
        private IMyList<ProgramState> _states;
        private readonly string _logFilePath;

        public Repository(string logFilePath)
        {
            _states = new MyList<ProgramState>();
            _logFilePath = logFilePath;
            File.WriteAllText(_logFilePath, "");
        }


        public void AddProgram(ProgramState programState)
        {
            _states.Add(programState);
        }

        public ProgramState GetCurrentProgram()
        {
            try
            {
                return _states.GetFirstElement();
            }
            catch (AdtException)
            {
                throw new RepositoryException("Empty repository.");
            }
        }

        public void LogProgramStateExec()
        {
            using (StreamWriter file = new StreamWriter(_logFilePath, true))
            {
                ProgramState programState = _states.GetFirstElement();
                file.WriteLine(programState);
            }
        }
    }       
 }