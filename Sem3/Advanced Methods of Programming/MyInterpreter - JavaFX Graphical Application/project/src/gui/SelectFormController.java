package gui;


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
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
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
                    new CompoundStatement(new AssignStatement("b", new ArithmeticExpression(new VariableExpression("a"), new
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
                            new ReadStatement(new VariableExpression("var_f"), "var_c"),
                            new PrintStatement(new VariableExpression("var_c"))));
            StatementInterface comp2 = new CompoundStatement(new IfStatement(new VariableExpression("var_c"),
                    new CompoundStatement(new ReadStatement(new VariableExpression("var_f"), "var_c"),
                            new PrintStatement(new VariableExpression("var_c"))),
                    new PrintStatement(new ConstantExpression(0))),
                    new CloseStatement(new VariableExpression("var_f")));
            StatementInterface ex4 = new CompoundStatement(comp1, comp2);


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


//            example 6 - lab 6 - example1
            StatementInterface comp5 = new CompoundStatement(new CompoundStatement(new AssignStatement("v", new ConstantExpression(10)),
                    new NewStatement("v", new ConstantExpression(20))),
                    new NewStatement("a", new ConstantExpression(22)));
            StatementInterface comp6 = new CompoundStatement(new PrintStatement(new ArithmeticExpression(new ConstantExpression(100), new ReadHeapExpression("v"), '+')),
                    new PrintStatement(new ArithmeticExpression(new ConstantExpression(100), new ReadHeapExpression("a"), '+')));
            StatementInterface ex6 = new CompoundStatement(comp5, comp6);


//            example 7 - lab 6 - example2
            StatementInterface comp7 = new CompoundStatement(new CompoundStatement(new AssignStatement("v", new ConstantExpression(10)),
                    new NewStatement("v", new ConstantExpression(20))),
                    new NewStatement("a", new ConstantExpression(22)));
            StatementInterface comp8 = new CompoundStatement(new WriteStatement("a", new ConstantExpression(30)),
                    new CompoundStatement(new PrintStatement(new VariableExpression("a")),
                            new PrintStatement(new ReadHeapExpression("a"))));
            StatementInterface ex7 = new CompoundStatement(comp7, comp8);


//            example 8 - lab 6 - example3
            StatementInterface comp9 = new CompoundStatement(new CompoundStatement(new AssignStatement("v", new ConstantExpression(10)),
                    new NewStatement("v", new ConstantExpression(20))),
                    new NewStatement("a", new ConstantExpression(22)));
            StatementInterface comp10 = new CompoundStatement(new CompoundStatement(new WriteStatement("a", new ConstantExpression(30)),
                    new PrintStatement(new VariableExpression("a"))),
                    new CompoundStatement(new PrintStatement(new ReadHeapExpression("a")),
                            new AssignStatement("a", new ConstantExpression(0))));
            StatementInterface ex8 = new CompoundStatement(comp9, comp10);


//            example 9 - lab 7 - example 1
            StatementInterface ex9 = new PrintStatement(new ArithmeticExpression(new ConstantExpression(10),
                    new BooleanExpression(new ConstantExpression(2), new ConstantExpression(6), "<"),
                    '+'));


//            example 10 - lab 7 - example 2
            StatementInterface ex10 = new PrintStatement(new BooleanExpression(new ArithmeticExpression(new ConstantExpression(10), new ConstantExpression(2), '+'),
                    new ConstantExpression(6),
                    "<"));


//            example 11 - lab 7 - example 3
            StatementInterface ex11 = new CompoundStatement(new AssignStatement("v", new ConstantExpression(6)),
                    new CompoundStatement(new WhileStatement(new ArithmeticExpression(new VariableExpression("v"), new ConstantExpression(4), '-'),
                            new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                                    new AssignStatement("v", new ArithmeticExpression(new VariableExpression("v"), new ConstantExpression(1), '-')))),
                            new PrintStatement(new VariableExpression("v"))));


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
//      programStatements.add(ex15);
//      programStatements.add(ex16);
//      programStatements.add(ex17);
//      programStatements.add(ex18);
//      programStatements.add(ex19);
//      programStatements.add(ex20);
//      programStatements.add(ex21);
//      programStatements.add(ex22);
//      programStatements.add(ex23);
//      programStatements.add(ex24);
//      programStatements.add(ex25);
//      programStatements.add(ex26);
//      programStatements.add(ex27);
//      programStatements.add(ex28);
//      programStatements.add(ex29);

        }
        catch (ExpressionException exception)
        {
            Alert errorAlert = new Alert(Alert.AlertType.ERROR);
            errorAlert.setHeaderText("Expression Exception");
            errorAlert.setContentText(exception.getMessage());
            errorAlert.showAndWait();
        }

    }


    private List<String> getStringRepresentations()
    {
        return programStatements.stream().map(StatementInterface::toString).collect(Collectors.toList());
    }


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


    @FXML
    private void executeButtonHandler() throws IOException
    {
        int index = programsListView.getSelectionModel().getSelectedIndex();

        if (index == -1)
        {
            Alert errorAlert = new Alert(Alert.AlertType.ERROR);
            errorAlert.setHeaderText("");
            errorAlert.setContentText("Please select a program.");
            errorAlert.showAndWait();
            return;
        }

        ControllerInterpreter controllerInterpreter = null;
        try
        {
            controllerInterpreter = createController(programStatements.get(index), "./logFiles/log" + index + ".out");
        }
        catch (RepositoryException exception)
        {
            Alert errorAlert = new Alert(Alert.AlertType.ERROR);
            errorAlert.setHeaderText("Repository Exception");
            errorAlert.setContentText(exception.getMessage());
            errorAlert.showAndWait();
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
