package view;


import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;


public class TextMenu
{
    private Map<String, Command> commands;


    public TextMenu()
    {
        commands = new TreeMap<>();
    }


    public void addCommand(Command command)
    {
        commands.put(command.getKey(), command);
    }


    private void printMenu()
    {
        System.out.println("\nMenu:");
        for (Command command : commands.values())
        {
            String line = String.format("%4s. %s", command.getKey(), command.getDescription());
            System.out.println(line);
        }
    }


    public void show()
    {
        Scanner scanner = new Scanner(System.in);
        while (true)
        {
            printMenu();
            System.out.print("Input command: ");
            String key = scanner.nextLine();
            Command command = commands.get(key);
            if (command == null)
            {
                System.out.println("Invalid command.");
                continue;
            }
            command.execute();
        }
    }
}
