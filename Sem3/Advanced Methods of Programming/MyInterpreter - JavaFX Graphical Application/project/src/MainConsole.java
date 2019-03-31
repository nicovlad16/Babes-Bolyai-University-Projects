import controller.ControllerInterpreter;
import domain.ProgramState;
import domain.adt.*;
import domain.expression.*;
import domain.statement.*;
import domain.statement.File.CloseStatement;
import domain.statement.File.OpenStatement;
import domain.statement.File.ReadStatement;
import domain.statement.Heap.NewStatement;
import domain.statement.Heap.WriteStatement;
import repository.Repository;
import repository.RepositoryException;
import repository.RepositoryInterface;
import view.ExitCommand;
import view.RunExample;
import view.TextMenu;


public class MainConsole
{
    private static ControllerInterpreter createController(StatementInterface statementInterface, String logFilePath)
            throws RepositoryException
    {
        Integer threadID = 1;
        MyStackInterface<StatementInterface> exeStack = new MyStack<>();
        MyDictionaryInterface<String, Integer> symbolTable = new MyDictionary<>();
        MyDictionaryInterface<Integer, MyPair> fileTable = new MyDictionary<>();
        MyDictionaryInterface<Integer, Integer> heapTable = new MyDictionary<>();
        MyListInterface<Integer> out = new MyList<>();
        ProgramState programState = new ProgramState(exeStack, symbolTable, out, fileTable, heapTable,
                threadID, statementInterface);
        RepositoryInterface repository = new Repository(logFilePath);
        ControllerInterpreter controller = new ControllerInterpreter(repository);
        controller.addProgram(programState);
        return controller;
    }


    public static void main(String[] args)
    {
        try
        {
//            example 1
            StatementInterface ex1 = new CompoundStatement(new AssignStatement("v", new ConstantExpression(2)),
                    new PrintStatement(new VariableExpression("v")));
            ControllerInterpreter controller1 = createController(ex1, "logFiles/log1.out");


//            example 2
            StatementInterface ex2 = new CompoundStatement(
                    new AssignStatement("a", new ArithmeticExpression(new ConstantExpression(2), new
                            ArithmeticExpression(new ConstantExpression(3), new ConstantExpression(5), '*'), '+')),
                    new CompoundStatement(new AssignStatement("b", new ArithmeticExpression(new VariableExpression("a"), new
                            ConstantExpression(1), '+')), new PrintStatement(new VariableExpression("b"))));
            ControllerInterpreter controller2 = createController(ex2, "logFiles/log2.out");


//            example 3
            StatementInterface ex3 = new CompoundStatement
                    (new AssignStatement("a",
                            new ArithmeticExpression(new ConstantExpression(2),
                                    new ConstantExpression(2),
                                    '-')),
                            new CompoundStatement(new IfStatement(new VariableExpression("a"),
                                    new AssignStatement("v", new ConstantExpression(2)),
                                    new AssignStatement("v", new ConstantExpression(3))),
                                    new PrintStatement(new VariableExpression("v"))));
            ControllerInterpreter controller3 = createController(ex3, "logFiles/log3.out");


//            example 4 - lab 5 example1
            StatementInterface comp1 = new CompoundStatement(new OpenStatement("inputFiles/test1.in", "var_f"),
                    new CompoundStatement(
                            new ReadStatement(new VariableExpression("var_f"), "var_c"),
                            new PrintStatement(new VariableExpression("var_c"))));
            StatementInterface comp2 = new CompoundStatement(new IfStatement(new VariableExpression("var_c"),
                    new CompoundStatement(new ReadStatement(new VariableExpression("var_f"), "var_c"),
                            new PrintStatement(new VariableExpression("var_c"))),
                    new PrintStatement(new ConstantExpression(0))),
                    new CloseStatement(new VariableExpression("var_f")));
            StatementInterface ex4 = new CompoundStatement(comp1, comp2);
            ControllerInterpreter controller4 = createController(ex4, "logFiles/log4.out");


//            example 5 - lab 5 - example2 ; it should print an error message
            StatementInterface comp3 = new CompoundStatement(new OpenStatement("inputFiles/test1.in", "var_f"),
                    new CompoundStatement(new ReadStatement(new ArithmeticExpression(new VariableExpression("var_f"), new ConstantExpression(2), '+'), "var_c"),
                            new PrintStatement(new VariableExpression("var_c"))));
            StatementInterface comp4 = new CompoundStatement(new IfStatement(new VariableExpression("var_c"),
                    new CompoundStatement(new ReadStatement(new VariableExpression("var_f"), "var_c"),
                            new PrintStatement(new VariableExpression("var_c"))),
                    new PrintStatement(new ConstantExpression(0))),
                    new CloseStatement(new VariableExpression("var_f")));
            StatementInterface ex5 = new CompoundStatement(comp3, comp4);
            ControllerInterpreter controller5 = createController(ex5, "logFiles/log5.out");


//            example 6 - lab 6 - example1
            StatementInterface comp5 = new CompoundStatement(new CompoundStatement(new AssignStatement("v", new ConstantExpression(10)),
                    new NewStatement("v", new ConstantExpression(20))),
                    new NewStatement("a", new ConstantExpression(22)));
            StatementInterface comp6 = new CompoundStatement(new PrintStatement(new ArithmeticExpression(new ConstantExpression(100), new ReadHeapExpression("v"), '+')),
                    new PrintStatement(new ArithmeticExpression(new ConstantExpression(100), new ReadHeapExpression("a"), '+')));
            StatementInterface ex6 = new CompoundStatement(comp5, comp6);
            ControllerInterpreter controller6 = createController(ex6, "logFiles/log6.out");


//            example 7 - lab 6 - example2
            StatementInterface comp7 = new CompoundStatement(new CompoundStatement(new AssignStatement("v", new ConstantExpression(10)),
                    new NewStatement("v", new ConstantExpression(20))),
                    new NewStatement("a", new ConstantExpression(22)));
            StatementInterface comp8 = new CompoundStatement(new WriteStatement("a", new ConstantExpression(30)),
                    new CompoundStatement(new PrintStatement(new VariableExpression("a")),
                            new PrintStatement(new ReadHeapExpression("a"))));
            StatementInterface ex7 = new CompoundStatement(comp7, comp8);
            ControllerInterpreter controller7 = createController(ex7, "logFiles/log7.out");


//            example 8 - lab 6 - example3
            StatementInterface comp9 = new CompoundStatement(new CompoundStatement(new AssignStatement("v", new ConstantExpression(10)),
                    new NewStatement("v", new ConstantExpression(20))),
                    new NewStatement("a", new ConstantExpression(22)));
            StatementInterface comp10 = new CompoundStatement(new CompoundStatement(new WriteStatement("a", new ConstantExpression(30)),
                    new PrintStatement(new VariableExpression("a"))),
                    new CompoundStatement(new PrintStatement(new ReadHeapExpression("a")),
                            new AssignStatement("a", new ConstantExpression(0))));
            StatementInterface ex8 = new CompoundStatement(comp9, comp10);
            ControllerInterpreter controller8 = createController(ex8, "logFiles/log8.out");


//            example 9 - lab 7 - example 1
            StatementInterface ex9 = new PrintStatement(new ArithmeticExpression(new ConstantExpression(10),
                    new BooleanExpression(new ConstantExpression(2), new ConstantExpression(6), "<"),
                    '+'));
            ControllerInterpreter controller9 = createController(ex9, "logFiles/log9.out");


//            example 10 - lab 7 - example 2
            StatementInterface ex10 = new PrintStatement(new BooleanExpression(new ArithmeticExpression(new ConstantExpression(10), new ConstantExpression(2), '+'),
                    new ConstantExpression(6),
                    "<"));
            ControllerInterpreter controller10 = createController(ex10, "logFiles/log10.out");


//            example 11 - lab 7 - example 3
            StatementInterface ex11 = new CompoundStatement(new AssignStatement("v", new ConstantExpression(6)),
                    new CompoundStatement(new WhileStatement(new ArithmeticExpression(new VariableExpression("v"), new ConstantExpression(4), '-'),
                            new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                                    new AssignStatement("v", new ArithmeticExpression(new VariableExpression("v"), new ConstantExpression(1), '-')))),
                            new PrintStatement(new VariableExpression("v"))));
            ControllerInterpreter controller11 = createController(ex11, "logFiles/log11.out");


//            example 12 - lab 8
            StatementInterface comp11 = new CompoundStatement(new CompoundStatement(new AssignStatement("v", new ConstantExpression(10)),
                    new NewStatement("a", new ConstantExpression(22))),
                    new ForkStatement(new CompoundStatement(new CompoundStatement(new WriteStatement("a", new ConstantExpression(30)),
                            new AssignStatement("v", new ConstantExpression(32))),
                            new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                                    new PrintStatement(new ReadHeapExpression("a"))))));
            StatementInterface comp12 = new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                    new PrintStatement(new ReadHeapExpression("a")));
            StatementInterface ex12 = new CompoundStatement(comp11, comp12);
            ControllerInterpreter controller12 = createController(ex12, "logFiles/log12.out");

//            example 13
            StatementInterface comp13 = new CompoundStatement(new CompoundStatement(new AssignStatement("v", new ConstantExpression(10)),
                    new NewStatement("a", new ConstantExpression(22))),
                    new ForkStatement(new CompoundStatement(new CompoundStatement(new WriteStatement("a", new ConstantExpression(30)),
                            new AssignStatement("v", new ConstantExpression(32))),
                            new ForkStatement(new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                                    new PrintStatement(new ReadHeapExpression("a")))))));
            StatementInterface comp14 = new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                    new PrintStatement(new ReadHeapExpression("a")));
            StatementInterface ex13 = new CompoundStatement(comp13, comp14);
            ControllerInterpreter controller13 = createController(ex13, "logFiles/log13.out");


//            example 14
            StatementInterface comp15 = new CompoundStatement(new CompoundStatement(new AssignStatement("v", new ConstantExpression(10)),
                    new NewStatement("a", new ConstantExpression(22))),
                    new ForkStatement(new CompoundStatement(new CompoundStatement(new WriteStatement("a", new ConstantExpression(30)),
                            new AssignStatement("v", new ConstantExpression(32))),
                            new CompoundStatement(new ForkStatement(new PrintStatement(new VariableExpression("v"))),
                                    new ForkStatement(new PrintStatement(new ReadHeapExpression("a")))))));
            StatementInterface comp16 = new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                    new PrintStatement(new ReadHeapExpression("a")));
            StatementInterface ex14 = new CompoundStatement(comp15, comp16);
            ControllerInterpreter controller14 = createController(ex14, "logFiles/log14.out");

//            text menu commands
            TextMenu menu = new TextMenu();

            menu.addCommand(new ExitCommand("0", "exit"));
            menu.addCommand(new RunExample("01", ex1.toString(), controller1));
            menu.addCommand(new RunExample("02", ex2.toString(), controller2));
            menu.addCommand(new RunExample("03", ex3.toString(), controller3));
            menu.addCommand(new RunExample("04", ex4.toString(), controller4));
            menu.addCommand(new RunExample("05", ex5.toString(), controller5));
            menu.addCommand(new RunExample("06", ex6.toString(), controller6));
            menu.addCommand(new RunExample("07", ex7.toString(), controller7));
            menu.addCommand(new RunExample("08", ex8.toString(), controller8));
            menu.addCommand(new RunExample("09", ex9.toString(), controller9));
            menu.addCommand(new RunExample("10", ex10.toString(), controller10));
            menu.addCommand(new RunExample("11", ex11.toString(), controller11));
            menu.addCommand(new RunExample("12", ex12.toString(), controller12));
            menu.addCommand(new RunExample("13", ex13.toString(), controller13));
            menu.addCommand(new RunExample("14", ex14.toString(), controller14));

            menu.show();
        }
        catch (RepositoryException | ExpressionException exception)
        {
            System.out.println(exception.getMessage());
        }
    }
}