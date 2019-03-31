//
// Created by nvlad on 18.04.2018.
//

#include <iostream>
#include "ui.h"

using namespace std;


void UI::print_menu()
{
    printf("\n");
    printf("0 - Exit.\n");
    printf("1 - Administrator mode.\n");
    printf("2 - User mode.\n");
}


void UI::print_admin_mode_menu()
{
    printf("\nPossible commands:\n");
    printf("\t 0 - Back.\n");
    printf("\t 1 - Add dog.\n");
    printf("\t 2 - Remove dog.\n");
    printf("\t 3 - Update dog.\n");
    printf("\t 4 - Show all dogs.\n");
}


void UI::print_user_mode_menu()
{
    printf("\nPossible commands:\n");
    printf("\t 0 - Back.\n");
    printf("\t 1 - View all dogs.\n");
    printf("\t 2 - View dogs by age and breed.\n");
    printf("\t 3 - See adopted dogs.\n");
}


void UI::print_view_mode_menu()
{
    printf("\nPossible commands:\n");
    printf("\t 0 - Back.\n");
    printf("\t 1 - Adopt dog.\n");
    printf("\t 2 - Next.\n");
}


void UI::run()
{
    printf("Welcome to our Dog Shelter! ^_^\n");
    printf("Adopt a dog, pls. :)\n");
    while (true)
    {
        UI::print_menu();
        string command = read_string(">> ");
        if (command.length() != 1)
        {
            printf("Invalid command.\n");
            continue;
        }
        if (command[0] == '0')
        {
            printf("Thank you for visiting us.\nBye! ^_^\n");
            exit(0);
        } else if (command[0] == '1')
            run_administrator_mode();
        else if (command[0] == '2')
            run_user_mode();
        else
            printf("Invalid command.\n");
    }
}


void UI::run_administrator_mode()
{
    while (true)
    {
        print_admin_mode_menu();
        string command = read_string(">> ");
        if (command.length() != 1)
        {
            printf("Invalid command.\n");
            continue;
        }
        try
        {
            switch (command[0])
            {
                case '0':
                    return;
                case '1':
                    add_dog_shelter();
                    break;
                case '2':
                    remove_dog_shelter();
                    break;
                case '3':
                    update_dog_shelter();
                    break;
                case '4':
                    show_all_dogs_shelter();
                    break;
                default:
                    printf("Invalid command.\n");
                    break;
            }

        }
        catch (string &e)
        {
            cout << e << "\n";
        }
        catch (char const *e)
        {
            cout << e << "\n";
        }
    }
}


void UI::run_user_mode()
{
    while (true)
    {
        print_user_mode_menu();
        string command = read_string(">> ");
        if (command.length() != 1)
        {
            printf("Invalid command.\n");
            continue;
        }
        try
        {
            switch (command[0])
            {
                case '0':
                    return;
                case '1':
                    view_all_dogs();
                    break;
                case '2':
                    view_dogs_by_age_and_breed();
                    break;
                case '3':
                    see_adopted_dogs();
                    break;
                default:
                    printf("Invalid command.\n");
            }
        }
        catch (char const *e)
        {
            cout << e << "\n";
        }
    }
}


void UI::show_dog_list()
{
    ctrl.start_view_dogs();
    while (true)
    {
        DynamicArray<Dog> dogs = ctrl.get_dog_list();
        if (dogs.get_length())
        {
            print_view_mode_menu();
            Dog dog = ctrl.get_current_dog_from_list();
            cout << "A " << dog.get_age() << "-year old dog, named " << dog.get_name() << ", of breed "
                 << dog.get_breed() << ".\n\n";
            dog.view_photo();

            string command = read_string("\n>> ");
            if (command.length() != 1)
            {
                printf("Invalid command.\n");
                continue;
            }
            switch (command[0])
            {
                case '0':
                    return;
                case '1':
                    ctrl.adopt_dog();
                    cout << "Thank you for adopting a dog.\n";
                    break;
                case '2':
                    ctrl.next_dog();
                    break;
                default:
                    printf("Invalid command.\n");
            }
        } else
        {
            printf("404: No dogs found.\n");
            return;
        }
    }
}


int UI::read_number()
{
    try
    {
        std::string line;
        getline(cin, line);
        char str1[2];
        str1[0] = '\0';
        char str2[2];
        str2[0] = '\0';
        int n = stoi(line);
        int number = 0;
        sscanf(line.c_str(), "%d%s %s", &number, str1, str2);
        if (n != number || str1[0] != '\0' || str2[0] != '\0')
        {
            printf("Invalid number.\n>> ");
            read_number();
        }
        return n;
    }
    catch (std::invalid_argument &)
    {
        printf("Invalid number.\n>> ");
        read_number();
    }
    catch (std::out_of_range &)
    {
        printf("Invalid number.\n>> ");
        read_number();
    }
    return 0;
}


std::string UI::read_string(const char *txt)
{
    string command;
    cout << txt;
    getline(cin, command);
    return std::__cxx11::string(command);
}


void UI::add_dog_shelter()
{
    std::string breed = read_string("Breed: ");
    std::string name = read_string("Name: ");
    printf("Age: ");
    int age = read_number();
    std::string link = read_string("Photo link: ");

    this->ctrl.add_dog_to_shelter(breed, name, age, link);
    cout << "Successfully added.\n";
}


void UI::remove_dog_shelter()
{
    std::string breed = read_string("Breed: ");
    std::string name = read_string("Name: ");
    printf("Age: ");
    int age = read_number();
    std::string link = read_string("Photo link: ");

    this->ctrl.remove_dog_from_shelter(breed, name, age, link);
    cout << "Successfully removed.\n";
}


void UI::update_dog_shelter()
{
    std::string old_breed = read_string("Old breed: ");
    std::string old_name = read_string("Old name: ");
    printf("Old age: ");
    int old_age = read_number();
    std::string old_link = read_string("Old photo link: ");

    std::string new_breed = read_string("New breed: ");
    std::string new_name = read_string("New name: ");
    printf("New age: ");
    int new_age = read_number();
    std::string new_link = read_string("New photo link: ");

    this->ctrl.update_dog_shelter(old_breed, old_name, old_age, old_link, new_breed, new_name, new_age, new_link);
    cout << "Successfully updated.\n";
}


void UI::show_all_dogs_shelter()
{
    DynamicArray<Dog> dogs = ctrl.get_all_dogs_shelter();
    int i = 0;
    if (dogs.get_length() != 0)
    {
        cout << "These are the dogs in the shelter:\n";
        while (i < dogs.get_length())
        {
            cout << i << ". " << dogs[i] << "\n";
            i++;
        }
    } else
        cout << "404: No dogs found in the shelter.\n";
}


void UI::view_all_dogs()
{
    ctrl.view_all_dogs();
    show_dog_list();

}


void UI::view_dogs_by_age_and_breed()
{
    printf("Age: ");
    int age = read_number();
    string breed = read_string("Breed: ");
    ctrl.view_filtered_dogs(breed, age);
//        DynamicArray<Dog> dogs = ctrl.get_dog_list();
//        int i = 0;
//        cout << "\nUI:\n";
//        while (i < dogs.get_length())
//        {
//            cout << dogs[i] <<"\n";
//            i++;
//        }
    show_dog_list();
}


void UI::see_adopted_dogs()
{
    DynamicArray<Dog> dogs = ctrl.get_all_adopted_dogs();
    int i = 0;
    if (dogs.get_length() != 0)
    {
        cout << "These are the adopted dogs:\n";
        while (i < dogs.get_length())
        {
            cout << i << ". " << dogs[i] << "\n";
            i++;
        }
    } else
        cout << "404: No adopted dogs found. Pls adopt one, they need you. :(\n";
}


void UI::initialize_repo()
{
    ctrl.add_dog_to_shelter("Collie", "Lassie", 5, "https://bit.ly/2JlQouH");
    ctrl.add_dog_to_shelter("Pooch", "Pavlov's dog", 7, "https://bit.ly/2vzNhgo");
    ctrl.add_dog_to_shelter("Akita", "Hachiko", 3, "https://bit.ly/2vDNzTJ");
    ctrl.add_dog_to_shelter("Stray dog", "Laika", 10, "https://bit.ly/2qVpXEf");
    ctrl.add_dog_to_shelter("Jack Russell Terrier", "Courage", 2, "https://bit.ly/2HnLLiZ");
    ctrl.add_dog_to_shelter("Great Dane", "Scooby Doo", 4, "https://bit.ly/2F9VkjO");
    ctrl.add_dog_to_shelter("American Cocker Spaniel", "Lady", 4, "https://bit.ly/2JkKxFY");
    ctrl.add_dog_to_shelter("Dalmatian", "Perdita", 6, "https://bit.ly/2qRdy50");
    ctrl.add_dog_to_shelter("Cairn Terrier", "Toto", 2, "https://bit.ly/2vJVsXU");
    ctrl.add_dog_to_shelter("Pomeranian", "Boo", 1, "https://bit.ly/2F8bA4B");
}
