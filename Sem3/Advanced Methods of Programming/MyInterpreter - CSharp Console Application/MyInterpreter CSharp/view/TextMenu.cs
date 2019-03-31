using System;
using System.Collections.Generic;

namespace MyInterpreter_CSharp.view
{
    public class TextMenu
    {
        private Dictionary<string, Command> _commands;

        public TextMenu()
        {
            _commands = new Dictionary<string, Command>();
        }

        public void AddCommand(Command command)
        {
            _commands.Add(command.Key, command);
        }

        private void PrintMenu()
        {
            Console.WriteLine("\nMenu:");
            foreach (Command cmd in _commands.Values)
            {
                string line = cmd.Key + ". " + cmd.Description;
                Console.WriteLine(line);
            }
        }

        public void Show()
        {
            while (true)
            {
                PrintMenu();
                Console.WriteLine("Input command: ");
                string key = Console.ReadLine();
                if (key == null || !_commands.TryGetValue(key, out Command command))
                {
                    Console.WriteLine("Invalid command.");
                    continue;
                }

                command.Execute();
            }
        }
    }
}