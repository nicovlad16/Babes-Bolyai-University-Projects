namespace MyInterpreter_CSharp.domain.statement
{
    public interface IStatement
    {
        ProgramState Execute(ProgramState programState);
        string ToString();
    }
}