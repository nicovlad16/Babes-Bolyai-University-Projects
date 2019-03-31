using System;
using MyInterpreter_CSharp.domain;
using MyInterpreter_CSharp.domain.adt;
using MyInterpreter_CSharp.domain.statement;
using MyInterpreter_CSharp.repository;

namespace MyInterpreter_CSharp.controller
{
    public class Controller
    {
        private IRepository _repository;

        public Controller(IRepository repository)
        {
            _repository = repository;
        }

        private void OneStep(ProgramState programState)
        {
            IMyStack<IStatement> stack = programState.ExeStack;
            try
            {
                IStatement currentStatement = stack.Pop();
                currentStatement.Execute(programState);
            }
            catch (AdtException exception)
            {
                throw new ControllerException(exception.Message);
            }
            catch (StatementException exception)
            {
                throw new ControllerException(exception.Message);
            }
        }

        public void AllStep()
        {
            try
            {
                ProgramState programState = _repository.GetCurrentProgram();
                IMyStack<IStatement> stack = programState.ExeStack;

                do
                {
                    OneStep(programState);
                    _repository.LogProgramStateExec();
                } while (!stack.IsEmpty());
            }
            catch (RepositoryException exception)
            {
                throw new ControllerException(exception.Message);
            }
        }
    }
}