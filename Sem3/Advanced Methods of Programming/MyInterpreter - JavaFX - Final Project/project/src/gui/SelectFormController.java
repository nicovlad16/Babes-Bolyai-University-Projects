package gui;


import controller.ControllerInterpreter;
import domain.ProgramState;
import domain.expression.*;
import domain.statement.*;
import domain.statement.ControlStatements.ForStatement;
import domain.statement.ControlStatements.IfStatement;
import domain.statement.ControlStatements.RepeatStatement;
import domain.statement.ControlStatements.WhileStatement;
import domain.statement.FileStatements.CloseStatement;
import domain.statement.FileStatements.OpenStatement;
import domain.statement.FileStatements.ReadStatement;
import domain.statement.HeapStatements.NewHeapStatement;
import domain.statement.HeapStatements.WriteHeapStatement;
import domain.statement.LockStatements.CountDownLatch.AwaitStatement;
import domain.statement.LockStatements.CountDownLatch.CountDownStatement;
import domain.statement.LockStatements.CountDownLatch.NewCountDownLatch;
import domain.statement.LockStatements.Semaphore.AcquireStatement;
import domain.statement.LockStatements.Semaphore.NewSemaphoreStatement;
import domain.statement.LockStatements.Semaphore.ReleaseStatement;
import domain.statement.Other.*;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.stage.Stage;
import repository.Repository;
import repository.RepositoryException;
import repository.RepositoryInterface;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;


public class SelectFormController
{
    private List<StatementInterface> programStatements;

    @FXML
    public Button executeButton;
    @FXML
    private ListView programsListView;


    private void buildProgramStatements()
    {
        try
        {
//            example 1
            StatementInterface ex1 = new CompoundStatement(new AssignStatement("v", new ConstantExpression(2)),
                    new PrintStatement(new VariableExpression("v")));


//            example 2
            StatementInterface ex2 = new CompoundStatement(
                    new AssignStatement("a", new ArithmeticExpression(new ConstantExpression(2), new
                            ArithmeticExpression(new ConstantExpression(3), new ConstantExpression(5), '*'), '+')),
                    new CompoundStatement(
                            new AssignStatement("b", new ArithmeticExpression(new VariableExpression("a"), new
                                    ConstantExpression(1), '+')), new PrintStatement(new VariableExpression("b"))));


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


//            example 4 - lab 5 example1
            StatementInterface comp1 = new CompoundStatement(new OpenStatement("inputFiles/test1.in", "var_f"),
                    new CompoundStatement(
                            new ReadStatement(new VariableExpression("var_f"),
                                    "var_c"),
                            new PrintStatement(
                                    new VariableExpression("var_c"))));
            StatementInterface comp2 = new CompoundStatement(new IfStatement(new VariableExpression("var_c"),
                    new CompoundStatement(new ReadStatement(
                            new VariableExpression("var_f"),
                            "var_c"),
                            new PrintStatement(
                                    new VariableExpression(
                                            "var_c"))),
                    new PrintStatement(
                            new ConstantExpression(0))),
                    new CloseStatement(new VariableExpression("var_f")));
            StatementInterface ex4 = new CompoundStatement(comp1, comp2);


//            example 5 - lab 5 - example2 ; it should print an error message
            StatementInterface comp3 = new CompoundStatement(new OpenStatement("inputFiles/test1.in", "var_f"),
                    new CompoundStatement(new ReadStatement(
                            new ArithmeticExpression(
                                    new VariableExpression("var_f"),
                                    new ConstantExpression(2), '+'), "var_c"),
                            new PrintStatement(
                                    new VariableExpression(
                                            "var_c"))));
            StatementInterface comp4 = new CompoundStatement(new IfStatement(new VariableExpression("var_c"),
                    new CompoundStatement(new ReadStatement(
                            new VariableExpression("var_f"),
                            "var_c"),
                            new PrintStatement(
                                    new VariableExpression(
                                            "var_c"))),
                    new PrintStatement(
                            new ConstantExpression(0))),
                    new CloseStatement(new VariableExpression("var_f")));
            StatementInterface ex5 = new CompoundStatement(comp3, comp4);


//            example 6 - lab 6 - example1
            StatementInterface comp5 = new CompoundStatement(
                    new CompoundStatement(new AssignStatement("v", new ConstantExpression(10)),
                            new NewHeapStatement("v", new ConstantExpression(20))),
                    new NewHeapStatement("a", new ConstantExpression(22)));
            StatementInterface comp6 = new CompoundStatement(new PrintStatement(
                    new ArithmeticExpression(new ConstantExpression(100), new ReadHeapExpression("v"), '+')),
                    new PrintStatement(new ArithmeticExpression(
                            new ConstantExpression(100),
                            new ReadHeapExpression("a"), '+')));
            StatementInterface ex6 = new CompoundStatement(comp5, comp6);


//            example 7 - lab 6 - example2
            StatementInterface comp7 = new CompoundStatement(
                    new CompoundStatement(new AssignStatement("v", new ConstantExpression(10)),
                            new NewHeapStatement("v", new ConstantExpression(20))),
                    new NewHeapStatement("a", new ConstantExpression(22)));
            StatementInterface comp8 = new CompoundStatement(new WriteHeapStatement("a", new ConstantExpression(30)),
                    new CompoundStatement(
                            new PrintStatement(new VariableExpression("a")),
                            new PrintStatement(new ReadHeapExpression("a"))));
            StatementInterface ex7 = new CompoundStatement(comp7, comp8);


//            example 8 - lab 6 - example3
            StatementInterface comp9 = new CompoundStatement(
                    new CompoundStatement(new AssignStatement("v", new ConstantExpression(10)),
                            new NewHeapStatement("v", new ConstantExpression(20))),
                    new NewHeapStatement("a", new ConstantExpression(22)));
            StatementInterface comp10 = new CompoundStatement(
                    new CompoundStatement(new WriteHeapStatement("a", new ConstantExpression(30)),
                            new PrintStatement(new VariableExpression("a"))),
                    new CompoundStatement(new PrintStatement(new ReadHeapExpression("a")),
                            new AssignStatement("a", new ConstantExpression(0))));
            StatementInterface ex8 = new CompoundStatement(comp9, comp10);


//            example 9 - lab 7 - example 1
            StatementInterface ex9 = new PrintStatement(new ArithmeticExpression(new ConstantExpression(10),
                    new BooleanExpression(
                            new ConstantExpression(2),
                            new ConstantExpression(6),
                            "<"),
                    '+'));


//            example 10 - lab 7 - example 2
            StatementInterface ex10 = new PrintStatement(new BooleanExpression(
                    new ArithmeticExpression(new ConstantExpression(10), new ConstantExpression(2), '+'),
                    new ConstantExpression(6),
                    "<"));


//            example 11 - lab 7 - example 3
            StatementInterface ex11 = new CompoundStatement(new AssignStatement("v", new ConstantExpression(6)),
                    new CompoundStatement(new WhileStatement(
                            new ArithmeticExpression(
                                    new VariableExpression("v"),
                                    new ConstantExpression(4), '-'),
                            new CompoundStatement(new PrintStatement(
                                    new VariableExpression("v")),
                                    new AssignStatement("v",
                                            new ArithmeticExpression(
                                                    new VariableExpression(
                                                            "v"),
                                                    new ConstantExpression(
                                                            1),
                                                    '-')))),
                            new PrintStatement(
                                    new VariableExpression(
                                            "v"))));


//            example 12 - lab 8
            StatementInterface comp11 = new CompoundStatement(
                    new CompoundStatement(new AssignStatement("v", new ConstantExpression(10)),
                            new NewHeapStatement("a", new ConstantExpression(22))),
                    new ForkStatement(new CompoundStatement(
                            new CompoundStatement(new WriteHeapStatement("a", new ConstantExpression(30)),
                                    new AssignStatement("v", new ConstantExpression(32))),
                            new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                                    new PrintStatement(new ReadHeapExpression("a"))))));
            StatementInterface comp12 = new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                    new PrintStatement(new ReadHeapExpression("a")));
            StatementInterface ex12 = new CompoundStatement(comp11, comp12);

//            example 13
            StatementInterface comp13 = new CompoundStatement(
                    new CompoundStatement(new AssignStatement("v", new ConstantExpression(10)),
                            new NewHeapStatement("a", new ConstantExpression(22))),
                    new ForkStatement(new CompoundStatement(
                            new CompoundStatement(new WriteHeapStatement("a", new ConstantExpression(30)),
                                    new AssignStatement("v", new ConstantExpression(32))),
                            new ForkStatement(new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                                    new PrintStatement(
                                            new ReadHeapExpression("a")))))));
            StatementInterface comp14 = new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                    new PrintStatement(new ReadHeapExpression("a")));
            StatementInterface ex13 = new CompoundStatement(comp13, comp14);


//            example 14
            StatementInterface comp15 = new CompoundStatement(
                    new CompoundStatement(new AssignStatement("v", new ConstantExpression(10)),
                            new NewHeapStatement("a", new ConstantExpression(22))),
                    new ForkStatement(new CompoundStatement(
                            new CompoundStatement(new WriteHeapStatement("a", new ConstantExpression(30)),
                                    new AssignStatement("v", new ConstantExpression(32))),
                            new CompoundStatement(new ForkStatement(new PrintStatement(new VariableExpression("v"))),
                                    new ForkStatement(
                                            new PrintStatement(new ReadHeapExpression("a")))))));
            StatementInterface comp16 = new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                    new PrintStatement(new ReadHeapExpression("a")));
            StatementInterface ex14 = new CompoundStatement(comp15, comp16);


//      example 15
            String variable = "v";
            StatementInterface ex15 = new CompoundStatement(
                    new CompoundStatement(
                            new AssignStatement("v", new ConstantExpression(20)),
                            new ForStatement(
                                    variable,
                                    "<",
                                    new ConstantExpression(0),
                                    new ConstantExpression(3),
                                    new ArithmeticExpression(new VariableExpression(variable),
                                            new ConstantExpression(1), '+'),
                                    new ForkStatement(new CompoundStatement(
                                            new PrintStatement(new VariableExpression(variable)),
                                            new AssignStatement(variable, new ArithmeticExpression(
                                                    new VariableExpression(variable), new ConstantExpression(1),
                                                    '+')))))),
                    new PrintStatement(
                            new ArithmeticExpression(new VariableExpression(variable), new ConstantExpression(10),
                                    '*')));

//      example 16
            StatementInterface comp17 = new CompoundStatement(
                    new CompoundStatement(
                            new AssignStatement("a", new ConstantExpression(1)),
                            new AssignStatement("b", new ConstantExpression(2))),
                    new ConditionalAssignment("c", new VariableExpression("a"), new ConstantExpression(100),
                            new ConstantExpression(200)));
            StatementInterface comp18 = new CompoundStatement(
                    new CompoundStatement(
                            new PrintStatement(new VariableExpression("c")),
                            new ConditionalAssignment("c", new ArithmeticExpression(new VariableExpression("b"),
                                    new ConstantExpression(2), '-'),
                                    new ConstantExpression(100), new ConstantExpression(200))),
                    new PrintStatement(new VariableExpression("c")));
            StatementInterface ex16 = new CompoundStatement(comp17, comp18);


//        example 17
            StatementInterface ex17 = new CompoundStatement(
                    new AssignStatement("v", new ConstantExpression(10)),
                    new CompoundStatement(
                            new ForkStatement(new CompoundStatement(
                                    new CompoundStatement(new AssignStatement("v", new ArithmeticExpression(
                                            new VariableExpression("v"), new ConstantExpression(1), '-')),
                                            new AssignStatement("v", new ArithmeticExpression(
                                                    new VariableExpression("v"),
                                                    new ConstantExpression(1), '-'))),
                                    new PrintStatement(new VariableExpression("v")))),
                            new CompoundStatement(
                                    new SleepStatement(10),
                                    new PrintStatement(new ArithmeticExpression(new VariableExpression("v"),
                                            new ConstantExpression(10), '*')))));


//        example 18
            String v1 = "v1";
            String cnt = "cnt";
            StatementInterface comp19 = new CompoundStatement(
                    new CompoundStatement(
                            new CompoundStatement(new NewHeapStatement(v1, new ConstantExpression(1)),
                                    new NewSemaphoreStatement(cnt, new ReadHeapExpression(v1))),
                            new ForkStatement(new CompoundStatement(
                                    new AcquireStatement(cnt),
                                    new WriteHeapStatement(v1, new ArithmeticExpression(new ReadHeapExpression(v1),
                                            new ConstantExpression(10),
                                            '*'))))),
                    new CompoundStatement(
                            new PrintStatement(new ReadHeapExpression(v1)),
                            new ReleaseStatement(cnt)));

            StatementInterface comp20 = new CompoundStatement(
                    new CompoundStatement(
                            new ForkStatement(new CompoundStatement(
                                    new AcquireStatement(cnt),
                                    new WriteHeapStatement(v1, new ArithmeticExpression(new ReadHeapExpression(v1),
                                            new ConstantExpression(10),
                                            '*')))),
                            new WriteHeapStatement(v1, new ArithmeticExpression(new ReadHeapExpression(v1),
                                    new ConstantExpression(2), '*'))),
                    new CompoundStatement(
                            new PrintStatement(new ReadHeapExpression(v1)),
                            new CompoundStatement(
                                    new CompoundStatement(
                                            new ReleaseStatement(cnt),
                                            new AcquireStatement(cnt)),
                                    new CompoundStatement(
                                            new PrintStatement(new ArithmeticExpression(new ReadHeapExpression(v1),
                                                    new ConstantExpression(1),
                                                    '-')),
                                            new ReleaseStatement(cnt)))));

            StatementInterface ex18 = new CompoundStatement(comp19, comp20);

//            v=0;
//            (repeat (fork(print(v);v=v-1);v=v+1) until v==3);
//            x=1;y=2;z=3;w=4;
//            print(v*10)

//        example 19
            StatementInterface ex19 = new CompoundStatement(
                    new CompoundStatement(
                            new AssignStatement("v", new ConstantExpression(0)),
                            new RepeatStatement(
                                    new CompoundStatement(
                                            new ForkStatement(new CompoundStatement(
                                                    new PrintStatement(new VariableExpression("v")),
                                                    new AssignStatement("v", new ArithmeticExpression(
                                                            new VariableExpression("v"), new ConstantExpression(1),
                                                            '-')))),
                                            new AssignStatement("v",
                                                    new ArithmeticExpression(new VariableExpression("v"),
                                                            new ConstantExpression(1),
                                                            '+'))),
                                    new BooleanExpression(new VariableExpression("v"), new ConstantExpression(3),
                                            "=="))),
                    new CompoundStatement(
                            new CompoundStatement(
                                    new AssignStatement("x", new ConstantExpression(1)),
                                    new AssignStatement("y", new ConstantExpression(2))),
                            new CompoundStatement(
                                    new CompoundStatement(
                                            new AssignStatement("z", new ConstantExpression(3)),
                                            new AssignStatement("w", new ConstantExpression(4))),
                                    new PrintStatement(new ArithmeticExpression(new VariableExpression("v"),
                                            new ConstantExpression(10), '*')))));

//        example 20

            v1 = "v1";
            String v2 = "v2";
            String v3 = "v3";
            cnt = "cnt";

            StatementInterface comp21 = new CompoundStatement(
                    new CompoundStatement(
                            new CompoundStatement(new NewHeapStatement(v1, new ConstantExpression(2)),
                                    new NewHeapStatement(v2, new ConstantExpression(3))),
                            new CompoundStatement(new NewHeapStatement(v3, new ConstantExpression(4)),
                                    new NewCountDownLatch(cnt, new ReadHeapExpression(v2)))),
                    new ForkStatement(new CompoundStatement(
                            new CompoundStatement(
                                    new WriteHeapStatement(v1, new ArithmeticExpression(new ReadHeapExpression(v1),
                                            new ConstantExpression(10),
                                            '*')),
                                    new PrintStatement(new ReadHeapExpression(v1))),
                            new CompoundStatement(
                                    new CountDownStatement(cnt),
                                    new ForkStatement(new CompoundStatement(
                                            new CompoundStatement(
                                                    new WriteHeapStatement(v2, new ArithmeticExpression(
                                                            new ReadHeapExpression(v2), new ConstantExpression(10),
                                                            '*')),
                                                    new PrintStatement(new ReadHeapExpression(v2))),
                                            new CompoundStatement(
                                                    new CountDownStatement(cnt),
                                                    new ForkStatement(new CompoundStatement(
                                                            new WriteHeapStatement(v3, new ArithmeticExpression(
                                                                    new ReadHeapExpression(v3),
                                                                    new ConstantExpression(10), '*')),
                                                            new CompoundStatement(
                                                                    new PrintStatement(new ReadHeapExpression(v3)),
                                                                    new CountDownStatement(cnt)))))))))));

            StatementInterface comp22 = new CompoundStatement(
                    new CompoundStatement(
                            new AwaitStatement(cnt),
                            new PrintStatement(new ConstantExpression(100))),
                    new CompoundStatement(
                            new CountDownStatement(cnt),
                            new PrintStatement(new ConstantExpression(100))));

            StatementInterface ex20 = new CompoundStatement(comp21, comp22);


            programStatements = new ArrayList<>(30);
            programStatements.add(ex1);
            programStatements.add(ex2);
            programStatements.add(ex3);
            programStatements.add(ex4);
            programStatements.add(ex5);
            programStatements.add(ex6);
            programStatements.add(ex7);
            programStatements.add(ex8);
            programStatements.add(ex9);
            programStatements.add(ex10);
            programStatements.add(ex11);
            programStatements.add(ex12);
            programStatements.add(ex13);
            programStatements.add(ex14);
            programStatements.add(ex15);
            programStatements.add(ex16);
            programStatements.add(ex17);
            programStatements.add(ex18);
            programStatements.add(ex19);
            programStatements.add(ex20);
        }
        catch (ExpressionException exception)
        {
            MyAlert.showAlert("Expression Exception", exception.getMessage(), "error");
        }

    }


    private List<String> getStringRepresentations()
    {
        return programStatements.stream().map(StatementInterface::toString).collect(Collectors.toList());
    }


    public static ControllerInterpreter createControllerInterpreter(StatementInterface statementInterface,
                                                                    String logFilePath) throws RepositoryException
    {
        ProgramState programState = new ProgramState(statementInterface);

        RepositoryInterface repository = new Repository(logFilePath);
        ControllerInterpreter controller = new ControllerInterpreter(repository);
        controller.addProgram(programState);
        return controller;
    }


    @FXML
    private void executeButtonHandler() throws IOException
    {
        int index = programsListView.getSelectionModel().getSelectedIndex();

        if (index == -1)
        {
            MyAlert.showAlert("", "Please select a program.", "error");
            return;
        }

        ControllerInterpreter controllerInterpreter = null;
        try
        {
            controllerInterpreter = createControllerInterpreter(programStatements.get(index),
                    "./logFiles/log" + (index + 1) + ".out");
        }
        catch (RepositoryException exception)
        {
            MyAlert.showAlert("Repository Exception", exception.getMessage(), "error");
            return;
        }

        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(SelectFormController.class.getResource("runForm.fxml"));
        Parent root = loader.load();

        Stage stage = new Stage();
        stage.setScene(new Scene(root));
        stage.setTitle("Run Program");
        stage.show();

        RunFormController runFormController = loader.getController();
        runFormController.setControllerInterpreter(controllerInterpreter);
    }


    @FXML
    private void initialize()
    {
        buildProgramStatements();
        programsListView.setItems(FXCollections.observableArrayList(getStringRepresentations()));
    }
}
