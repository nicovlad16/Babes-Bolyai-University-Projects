#include <iostream>
#include "tests/tests.h"
#include "repo/file_repository.h"
#include "service/ctrl.h"
#include "ui/console.h"


int main()
{

//    Tests::test_all();

    Repository<Dog> repo("../dogs");
    Controller ctrl(repo);
    UI ui(ctrl);

    ui.choose_output_filetype();
    ui.initialize_repo();
    ui.run();
}

/*
* @startuml

package ui <<Folder>> {
 class UI {
    -ctrl: Controller
    +run()
    +initialize_repo()
    +choose_output_filetype()
    -run_administrator_mode()
    -{static}print_menu()
    -add_dog_shelter()
    -show_all_dogs_shelter()
    -{static}print_user_mode_menu()
    -{static}print_view_mode_menu()
    -{static}print_admin_mode_menu()
    -run_user_mode()
    -remove_dog_shelter()
    -update_dog_shelter()
    -view_all_dogs()
    -view_dogs_by_age_and_breed()
    -void see_adopted_dogs()
    -read_number(): int
    -read_string(string: txt): string
    -show_dog_list()
    -save_doglist_to_file()
    -see_adopted_dogs_file()
    }
}

package controller <<Folder>> {
class Controller {
    -repo: Repository<Dog>
    -dogs: FileDogList
    -adopted: vector<Dog>
    +Controller(Repository<Dog>: repo)
    +add_dog_to_shelter(string: breed, string: name, int: age, string: photo)
    +adopt_dog()
    +view_all_dogs()
    +view_filtered_dogs(string: breed, int: age)
    +get_all_dogs_shelter(): vector<Dog>
    +remove_dog_from_shelter(string: breed, string: name, int: age, string: photo)
    +update_dog_shelter(string: old_breed, string: old_name, int: old_age, string: old_photo,
            string: new_breed, string: new_name, int: new_age, string: new_photo)
    +get_all_adopted_dogs(): vector<Dog>
    +start_view_dogs();
    +next_dog();
    +get_dog_list(): vector<Dog>
    +get_current_dog_from_list(): Dog;
    +set_adopted_file(FileDogList *pList)
    +save_doglist(string: filename)
    +get_doglist(): FileDogList*
    +get_current_file(): string
    +see_adopted_file()
    }
}

package repository <<Folder>> {
class Repository {
    -elems: vector
    -filename: filename
    -read_from_file()
    -write_to_file()
    +Repository(string: filename)
    +add(elem)
    +get_all(): vector
    +get_length(): int
    +find(elem): bool
    +remove(elem)
    +update(old_elem, new_elem)
    }
}


package domain <<Folder>> {
class DogValidator {
    +{static}validate(Dog: dog)
}

class Dog {
    -breed: breed
    -name: string
    -age: int
    -photo: string
    +Dog()
    +~Dog()
    +Dog(string: breed, string: name, int: age, string: photo)
    +get_breed(): string
    +set_breed(string: breed)
    +get_name(): string
    +set_name(string: name)
    +get_age(): int
    +set_age(int: age)
    +get_photo(): string
    +set_photo(string: photo)
    +view_photo()
    +operator==(Dog: rhs): bool
    +operator!=(Dog: rhs) bool
    +operator<<(ostream: os, Dog: dog): ostream
    +operator>>(istream: is, Dog: dog): istream
}

class FileDogList {
    #dogs: vector<Dog>
    #current: int
    #filename: string
    +FileDogList()
    +~FileDogList()
    +add(Dog: dog);
    +get_current_dog(): Dog
    +view()
    +next()
    +remove(Dog: dog)
    +clear_list();
    +get_all(): vector<Dog>
    +{abstract}set_filename(string: filename)
    +{abstract}write_to_file(vector<Dog>: adopted)
    +{abstract}display_doglist()
    +get_filename(): string
}

class CSVDogList {
}

class HTMLDogList {
}

FileDogList <|-- CSVDogList : extends
FileDogList <|-- HTMLDogList : extends
}


mix_actor User
mix_actor Admin
User --> AppCoordinator
Admin --> AppCoordinator

AppCoordinator .> Repository : creates
AppCoordinator .> Controller : creates
AppCoordinator .> UI : creates
UI *-- Controller : has a
UI .> FileDogList : creates
Controller *--  Repository : has a
Controller *--  FileDogList : has a
Controller *--  DogValidator : has a
Controller .> DogValidator : creates
Controller .> Dog : creates
Repository .. Dog : of
DogValidator .. Dog


* @enduml
*/