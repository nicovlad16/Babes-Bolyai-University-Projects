using System;
using MyInterpreter_CSharp.domain;

namespace MyInterpreter_CSharp.repository
{
    public interface IRepository
    {
        void AddProgram(ProgramState programState);
        ProgramState GetCurrentProgram();
        void LogProgramStateExec();
    }
}