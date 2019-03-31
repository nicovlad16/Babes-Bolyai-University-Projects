package gui;


import controller.ControllerInterpreter;
import domain.ProgramState;
import domain.adt.AdtException;
import domain.adt.MyDictionaryInterface;
import domain.adt.MyPair;
import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.*;

import java.util.*;
import java.util.stream.Collectors;


public class RunFormController
{

    @FXML
    public ListView outputListView;
    @FXML
    public ListView threadListView;
    @FXML
    public TableView symbolTableView;
    @FXML
    public Button oneStepButton;
    @FXML
    public TableView fileTableView;
    @FXML
    public TableView heapTableView;
    @FXML
    public ListView exeStackListView;
    @FXML
    public TableColumn<Map.Entry<String, Integer>, String> symbolTableColumnVariable;
    @FXML
    public TableColumn<Map.Entry<String, Integer>, Integer> symbolTableColumnValue;
    @FXML
    public TableColumn<Map.Entry<Integer, String>, Integer> fileTableColumnId;
    @FXML
    public TableColumn<Map.Entry<Integer, String>, String> fileTableColumnFilename;
    @FXML
    public TableColumn<Map.Entry<Integer, Integer>, Integer> heapTableColumnAddress;
    @FXML
    public TableColumn<Map.Entry<Integer, Integer>, Integer> heapTableColumnValue;
    @FXML
    public TableView semaphoreTableView;
    @FXML
    public TableColumn<Map.Entry<Integer, MyPair<Integer, String>>, Integer> semaphoreTableViewIndexColumn;
    @FXML
    public TableColumn<Map.Entry<Integer, MyPair<Integer, String>>, Integer> semaphoreTableViewValueColumn;
    @FXML
    public TableColumn<Map.Entry<Integer, MyPair<Integer, String>>, String> semaphoreTableViewListColumn;
    @FXML
    public TableView latchTableView;
    @FXML
    public TableColumn<Map.Entry<Integer, Integer>, Integer> latchTableLocationColumn;
    @FXML
    public TableColumn<Map.Entry<Integer, Integer>, Integer> latchTableValueColumn;


    private ControllerInterpreter controllerInterpreter;


    void setControllerInterpreter(ControllerInterpreter controllerInterpreter)
    {
        this.controllerInterpreter = controllerInterpreter;
        populateThreadList();
        populateAllLists(getCurrentProgramState());
    }


    private List<Integer> getProgramStatesIds(List<ProgramState> programStates)
    {
        return programStates.stream().map(ProgramState::getThreadID).collect(Collectors.toList());
    }


    private void populateThreadList()
    {
        List<ProgramState> programStates = controllerInterpreter.getProgramList();
        ObservableList<Integer> statesIds = FXCollections.observableArrayList(getProgramStatesIds(programStates));
        threadListView.setItems(statesIds);

        int index = threadListView.getFocusModel().getFocusedIndex();
//    if (index != -1)
//      threadListView.getSelectionModel().select(index);
//    else
        if (statesIds.size() > 0)
            threadListView.getSelectionModel().select(0);
    }


    @FXML
    private void initialize()
    {
        symbolTableColumnVariable.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().getKey() + ""));
        symbolTableColumnValue.setCellValueFactory(p -> new SimpleIntegerProperty(p.getValue().getValue()).asObject());

        fileTableColumnId.setCellValueFactory(p -> new SimpleIntegerProperty(p.getValue().getKey()).asObject());
        fileTableColumnFilename.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().getValue() + ""));

        heapTableColumnAddress.setCellValueFactory(p -> new SimpleIntegerProperty(p.getValue().getKey()).asObject());
        heapTableColumnValue.setCellValueFactory(p -> new SimpleIntegerProperty(p.getValue().getValue()).asObject());

        semaphoreTableViewIndexColumn
                .setCellValueFactory(p -> new SimpleIntegerProperty(p.getValue().getKey()).asObject());
        semaphoreTableViewValueColumn
                .setCellValueFactory(p -> new SimpleIntegerProperty(p.getValue().getValue().getFirst()).asObject());
        semaphoreTableViewListColumn
                .setCellValueFactory(p -> new SimpleStringProperty(p.getValue().getValue().getSecond() + ""));

        latchTableLocationColumn.setCellValueFactory(p -> new SimpleIntegerProperty(p.getValue().getKey()).asObject());
        latchTableValueColumn.setCellValueFactory(p -> new SimpleIntegerProperty(p.getValue().getValue()).asObject());
    }


    @FXML
    public void executeOneStep()
    {
        try
        {

            if (controllerInterpreter == null)
            {
                MyAlert.showAlert("Repository Exception", "Please select a program.", "error");
                return;
            }

            boolean programIsFinished = (getCurrentProgramState() == null);
            if (programIsFinished)
            {
                MyAlert.showAlert("", "Program has finished.", "information");
                return;
            }
            controllerInterpreter.executeOneStep();
            populateThreadList();
            populateAllLists(getCurrentProgramState());


        }
        catch (InterruptedException exception)
        {
            MyAlert.showAlert("Interrupted Exception", exception.getMessage(), "error");
        }
    }


    private ProgramState getCurrentProgramState()
    {
        if (threadListView.getFocusModel().getFocusedIndex() == -1)
            return null;
        int index = (int) threadListView.getFocusModel().getFocusedItem();

//    if (threadListView.getSelectionModel().getSelectedIndex() == -1)
//      return null;

//    int index = (int) threadListView.getSelectionModel().getSelectedItem();
        return controllerInterpreter.getProgramStateByID(index);
    }


    private void populateAllLists(ProgramState programState)
    {
        if (programState == null)
            return;

        System.out.println(programState);

        updateSymbolTable(programState);
        updateOutput(programState);
        updateHeapTable(programState);
        updateFileTable(programState);
        updateExeStack(programState);
        updateSemaphoreTable(programState);
        updateLatchTable(programState);
    }


    private void updateLatchTable(ProgramState programState)
    {
        MyDictionaryInterface<Integer, Integer> latchTable = programState.getLatchTable();
        List<Map.Entry<Integer, Integer>> latchTableList = new ArrayList<>(latchTable.entrySet());
        ObservableList list = FXCollections.observableArrayList(latchTableList);
        latchTableView.setItems(list);
    }


    private void updateSemaphoreTable(ProgramState programState)
    {
        MyDictionaryInterface<Integer, MyPair> semaphoreTable = programState.getSemaphoreTable();
        Map<Integer, MyPair> semaphoreMap = new HashMap<>();

        for (Integer entry : semaphoreTable.keySet())
        {
            try
            {
                MyPair<Integer, List<Integer>> pair = semaphoreTable.get(entry);
                Integer value = pair.getFirst();
                String s = "";
                for (Integer i : pair.getSecond())
                {
                    s += i + " ";
                }
                semaphoreMap.put(entry, new MyPair(value, s));

            }
            catch (AdtException ignored)
            {
            }
        }

        List<Map.Entry<Integer, MyPair>> semaphoreList = new ArrayList<>(semaphoreMap.entrySet());
        ObservableList list = FXCollections.observableArrayList(semaphoreList);
        semaphoreTableView.setItems(list);
    }


    private void updateExeStack(ProgramState programState)
    {
        ObservableList list = FXCollections.observableArrayList(programState.getExeStack().getAll());
        exeStackListView.setItems(list);

    }


    private void updateFileTable(ProgramState programState)
    {
        MyDictionaryInterface<Integer, MyPair> fileTable = programState.getFileTable();
        Map<Integer, String> fileTableMap = new HashMap<>();

        for (Integer entry : fileTable.keySet())
        {
            try
            {
                String filename = fileTable.get(entry).getFirst().toString();
                fileTableMap.put(entry, filename);
            }
            catch (AdtException ignored)
            {
            }
        }

        List<Map.Entry<Integer, String>> fileTableList = new ArrayList<>(fileTableMap.entrySet());
        ObservableList list = FXCollections.observableArrayList(fileTableList);
        fileTableView.setItems(list);

    }


    private void updateHeapTable(ProgramState programState)
    {
        MyDictionaryInterface<Integer, Integer> heapTable = programState.getHeapTable();
        List<Map.Entry<Integer, Integer>> heapTableList = new ArrayList<>(heapTable.entrySet());
        ObservableList list = FXCollections.observableArrayList(heapTableList);
        heapTableView.setItems(list);
    }


    private void updateOutput(ProgramState programState)
    {
        ObservableList list = FXCollections.observableArrayList(programState.getOutput().getAll());
        outputListView.setItems(list);
    }


    private void updateSymbolTable(ProgramState programState)
    {
        MyDictionaryInterface<String, Integer> symbolTable = programState.getSymbolTable();
        List<Map.Entry<String, Integer>> symbolTableList = new ArrayList<>(symbolTable.entrySet());
        symbolTableView.setItems(FXCollections.observableArrayList(symbolTableList));
    }


    @FXML
    public void changeCurrentProgramState()
    {
        int index = (int) threadListView.getSelectionModel().getSelectedItem();
        ProgramState programState = controllerInterpreter.getProgramStateByID(index);
        populateAllLists(programState);
    }
}
