package view;


import controller.Controller;
import controller.ControllerException;


public class RunExample extends Command
{
    private Controller controller;


    public RunExample(String key, String description, Controller controller)
    {
        super(key, description);
        this.controller = controller;
    }


    @Override
    public void execute()
    {
        try
        {
            controller.allSteps();
            System.out.println("Command executed successfully.");
        }
        catch (ControllerException | InterruptedException exception)
        {
            System.out.println(exception.getMessage());
        }
    }
}