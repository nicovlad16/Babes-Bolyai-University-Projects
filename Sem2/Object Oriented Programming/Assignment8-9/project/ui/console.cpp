//
// Created by nvlad on 01.05.2018.
//

#include "console.h"
#include "../domain/csv_doglist.h"
#include "../domain/dog_validator.h"
#include "../domain/html_doglist.h"
#include <iostream>

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
    printf("\t 4 - Save adopted dogs list to file.\n");
    printf("\t 5 - Open the last saved adopted dogs list file.\n");
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
        catch (exception &e)
        {
            cout << e.what() << "\n";
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
                case '4':
                    save_doglist_to_file();
                    break;
                case '5':
                    see_adopted_dogs_file();
                    break;
                default:
                    printf("Invalid command.\n");
            }
        }
        catch (exception &e)
        {
            cout << e.what() << "\n";
        }
    }
}


void UI::show_dog_list()
{
    ctrl.start_view_dogs();
    while (true)
    {
        std::vector<Dog> dogs = ctrl.get_dog_list();
        if (!dogs.empty())
        {
            print_view_mode_menu();
            Dog dog = ctrl.get_current_dog_from_list();
            cout << "A " << dog.get_age() << "-year old dog, named " << dog.get_name() << ", of breed "
                 << dog.get_breed() << ".\n\n";
//            dog.view_photo();

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
    while (true)
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
                continue;
            }
            return n;
        }
        catch (std::invalid_argument &)
        {
            printf("Invalid number.\n>> ");
            continue;
        }
        catch (std::out_of_range &)
        {
            printf("Invalid number.\n>> ");
            continue;
        }
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
    std::vector<Dog> dogs = ctrl.get_all_dogs_shelter();
    int i = 0;
    if (!dogs.empty())
    {
        cout << "These are the dogs in the shelter:\n";
        while (i < dogs.size())
        {
            Dog dog = dogs[i];
            cout << i << ". A " << dog.get_age() << "-year old dog, named " << dog.get_name() << ", of breed "
                 << dog.get_breed() << ". Photo: " << dog.get_photo() << "\n";
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
    show_dog_list();
}


void UI::see_adopted_dogs()
{
    std::vector<Dog> dogs = ctrl.get_all_adopted_dogs();
    int i = 0;
    if (!dogs.empty())
    {
        cout << "These are the adopted dogs:\n";
        while (i < dogs.size())
        {
            cout << i << ". " << dogs[i];
            i++;
        }
    } else
        cout << "404: No adopted dogs found. Pls adopt one, they need you. :(\n";
}


void UI::initialize_repo()
{
//    ctrl.add_dog_to_shelter("Collie", "Lassie", 5, "https://bit.ly/2JlQouH");
//    ctrl.add_dog_to_shelter("Pooch", "Pavlov's dog", 7, "https://bit.ly/2vzNhgo");
//    ctrl.add_dog_to_shelter("Akita", "Hachiko", 3, "https://bit.ly/2vDNzTJ");
//    ctrl.add_dog_to_shelter("Stray dog", "Laika", 10, "https://bit.ly/2qVpXEf");
//    ctrl.add_dog_to_shelter("Jack Russell Terrier", "Courage", 2, "https://bit.ly/2HnLLiZ");
//    ctrl.add_dog_to_shelter("Great Dane", "Scooby Doo", 4, "https://bit.ly/2F9VkjO");
//    ctrl.add_dog_to_shelter("American Cocker Spaniel", "Lady", 4, "https://bit.ly/2JkKxFY");
//    ctrl.add_dog_to_shelter("Dalmatian", "Perdita", 6, "https://bit.ly/2qRdy50");
//    ctrl.add_dog_to_shelter("Cairn Terrier", "Toto", 2, "https://bit.ly/2vJVsXU");
//    ctrl.add_dog_to_shelter("Pomeranian", "Boo", 1, "https://bit.ly/2F8bA4B");
}


void UI::choose_output_filetype()
{
    printf("Please press 1 for CSV file or 2 for HTML file.\n");
    int i = 0;
    do
    {
        printf(">> ");
        i = read_number();

    } while (i != 1 && i != 2);

    FileDogList *file = nullptr;
    if (i == 1)
        file = new CSVDogList;
    else
    {
        file = new HTMLDogList;
    }

    ctrl.set_adopted_file(file);
}


void UI::save_doglist_to_file()
{
    std::string filename;
    cout << "Input the file name (absolute path): ";
    getline(cin, filename);

    try
    {
        ctrl.save_doglist(filename);

        if (ctrl.get_doglist() == nullptr)
        {
            cout << "Doglist cannot be displayed!" << endl;
            return;
        }
    }
    catch (RepositoryException &e)
    {
        cout << e.what() << endl;
    }
}


void UI::see_adopted_dogs_file()
{
    if (ctrl.get_current_file().empty())
    {
        printf("Please save the file first.\n");
        return;
    }
    ctrl.see_adopted_file();
}
