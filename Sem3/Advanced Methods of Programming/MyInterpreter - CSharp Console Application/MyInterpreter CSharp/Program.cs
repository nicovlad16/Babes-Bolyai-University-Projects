using System;
using System.IO;
using MyInterpreter_CSharp.controller;
using MyInterpreter_CSharp.domain;
using MyInterpreter_CSharp.domain.adt;
using MyInterpreter_CSharp.domain.expression;
using MyInterpreter_CSharp.domain.statement;
using MyInterpreter_CSharp.repository;
using MyInterpreter_CSharp.view;

namespace MyInterpreter_CSharp
{
    internal class Program
    {
        private static Controller CreateController(IStatement statementInterface, String logFilePath)
        {
            IMyStack<IStatement> exeStack = new MyStack<IStatement>();
            IMyDictionary<string, int> symbolTable = new MyDictionary<string, int>();
            IMyDictionary<int, MyPair<string, TextReader>> fileTable =
                new MyDictionary<int, MyPair<string, TextReader>>();
            IMyList<int> output = new MyList<int>();
            ProgramState programState = new ProgramState(exeStack, symbolTable, output, fileTable, statementInterface);
            IRepository repository = new Repository(logFilePath);
            repository.AddProgram(programState);
            Controller controller = new Controller(repository);
            return controller;
        }


        public static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            try
            {
//            example 1
                IStatement ex1 =
                    new CompoundStatement(
                        new AssignStatement("v", new ConstantExpression(2)),
                        new PrintStatement(new VariableExpression("v")));
                Controller controller1 = CreateController(ex1, "../../logFiles/log1.out");


//            example 2
                IStatement ex2 =
                    new CompoundStatement(
                        new AssignStatement("a",
                            new ArithmeticExpression(
                                new ConstantExpression(2),
                                new ArithmeticExpression(
                                    new ConstantExpression(3),
                                    new ConstantExpression(5),
                                    '*'),
                                '+')),
                        new CompoundStatement(
                            new AssignStatement("b",
                                new ArithmeticExpression(new VariableExpression("a"),
                                    new ConstantExpression(1),
                                    '+')),
                            new PrintStatement(
                                new VariableExpression("b"))));
                Controller controller2 = CreateController(ex2, "../../logFiles/log2.out");


//            example 3
                IStatement ex3 =
                    new CompoundStatement(
                        new AssignStatement("a",
                            new ArithmeticExpression(
                                new ConstantExpression(2),
                                new ConstantExpression(2),
                                '-')),
                        new CompoundStatement(
                            new IfStatement(
                                new VariableExpression("a"),
                                new AssignStatement("v",
                                    new ConstantExpression(2)),
                                new AssignStatement("v",
                                    new ConstantExpression(3))),
                            new PrintStatement(
                                new VariableExpression("v"))));
                Controller controller3 = CreateController(ex3, "../../logFiles/log3.out");


//            example 4 - lab 5 example1
                IStatement comp1 =
                    new CompoundStatement(
                        new OpenStatement("../../inputFiles/test1.in", "var_f"),
                        new CompoundStatement(
                            new ReadStatement(
                                new VariableExpression("var_f"),
                                "var_c"),
                            new PrintStatement(
                                new VariableExpression("var_c"))));
                IStatement comp2 =
                    new CompoundStatement(
                        new IfStatement(
                            new VariableExpression("var_c"),
                            new CompoundStatement(
                                new ReadStatement(
                                    new VariableExpression("var_f"), "var_c"),
                                new PrintStatement(
                                    new VariableExpression("var_c"))),
                            new PrintStatement(
                                new ConstantExpression(0))),
                        new CloseStatement(
                            new VariableExpression("var_f")));
                IStatement ex4 = new CompoundStatement(comp1, comp2);
                Controller controller4 = CreateController(ex4, "../../logFiles/log4.out");


//            example 5 - lab 5 - example2 ; it should print an error message
                IStatement comp3 =
                    new CompoundStatement(
                        new OpenStatement("../../inputFiles/test1.in", "var_f"),
                        new CompoundStatement(
                            new ReadStatement(
                                new ArithmeticExpression(new VariableExpression("var_f"), new ConstantExpression(2),
                                    '+'),
                                "var_c"),
                            new PrintStatement(
                                new VariableExpression("var_c"))));
                IStatement comp4 =
                    new CompoundStatement(
                        new IfStatement(
                            new VariableExpression("var_c"),
                            new CompoundStatement(
                                new ReadStatement(
                                    new VariableExpression("var_f"), "var_c"),
                                new PrintStatement(
                                    new VariableExpression("var_c"))),
                            new PrintStatement(
                                new ConstantExpression(0))),
                        new CloseStatement(
                            new VariableExpression("var_f")));
                IStatement ex5 = new CompoundStatement(comp3, comp4);
                Controller controller5 = CreateController(ex5, "../../logFiles/log5.out");


//            text menu commands
                TextMenu menu = new TextMenu();

                menu.AddCommand(new ExitCommand("0", "exit"));
                menu.AddCommand(new RunExample("1", ex1.ToString(), controller1));
                menu.AddCommand(new RunExample("2", ex2.ToString(), controller2));
                menu.AddCommand(new RunExample("3", ex3.ToString(), controller3));
                menu.AddCommand(new RunExample("4", ex4.ToString(), controller4));
                menu.AddCommand(new RunExample("5", ex5.ToString(), controller5));

                menu.Show();
            }
            catch (RepositoryException exception)
            {
                Console.WriteLine(exception.Message);
            }
            catch (ExpressionException exception)
            {
                Console.WriteLine(exception.Message);
            }
        }
    }
}