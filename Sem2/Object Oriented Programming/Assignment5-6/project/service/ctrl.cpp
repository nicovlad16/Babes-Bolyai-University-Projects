//
// Created by nvlad on 18.04.2018.
//

#include <string>
#include <iostream>
#include "ctrl.h"
#include "../domain/DogValidator.h"


void
Controller::add_dog_to_shelter(const std::string &breed, const std::string &name, int age, const std::string &photo)
{
    Dog dog{breed, name, age, photo};
    DogValidator::validate(dog);
    repo.add(dog);
}


void Controller::remove_dog_from_shelter(const std::string &breed, const std::string &name, int age,
                                         const std::string &photo)
{
    Dog dog{breed, name, age, photo};
    DogValidator::validate(dog);
    repo.remove(dog);
}


void Controller::update_dog_shelter(std::string old_breed, std::string old_name, int old_age, std::string old_photo,
                                    std::string new_breed, std::string new_name, int new_age, std::string new_photo)
{
    Dog old_dog{old_breed, old_name, old_age, old_photo};
    try
    {
        DogValidator::validate(old_dog);
    }
    catch (std::string &e)
    {
        throw ("Old dog: " + e);
    }

    Dog new_dog{new_breed, new_name, new_age, new_photo};
    try
    {
        DogValidator::validate(old_dog);
    }
    catch (std::string &e)
    {
        throw ("New dog: " + e);
    }

    repo.update(old_dog, new_dog);

}


void Controller::view_all_dogs()
{
    dogs.clear_list();
    DynamicArray<Dog> all_dogs = getRepo().get_all();

    int i = 0;
    while (i < all_dogs.get_length())
    {
        dogs.add(all_dogs[i]);
        i++;
    }
}


void Controller::view_filtered_dogs(const std::string &breed, int age)
{

    dogs.clear_list();
    DynamicArray<Dog> all_dogs = getRepo().get_all();

    if (breed.empty())
    {
        int i = 0;
        while (i < all_dogs.get_length())
        {
            if (all_dogs[i].get_age() < age)
                dogs.add(all_dogs[i]);

            i++;
        }
    } else
    {
        int i = 0;
        while (i < all_dogs.get_length())
        {
            if (all_dogs[i].get_breed() == breed && all_dogs[i].get_age() < age)
                dogs.add(all_dogs[i]);
            i++;
        }
    }

//    DynamicArray<Dog> dogs_ctrl = dogs.get_all();
//    int i = 0;
//    std::cout << "\nCtrl:\n";
//    while (i < dogs_ctrl.get_length())
//    {
//        std::cout << dogs_ctrl[i] <<"\n";
//        i++;
//    }
}


void Controller::adopt_dog()
{
    Dog dog = dogs.get_current_dog();
    adopted.add(dog);
    dogs.remove(dog);
    repo.remove(dog);
}


DynamicArray<Dog> Controller::get_all_dogs_shelter()
{
    return repo.get_all();
}


DynamicArray<Dog> Controller::get_all_adopted_dogs()
{
    return adopted;
}


DynamicArray<Dog> Controller::get_dog_list()
{
    return dogs.get_all();
}


void Controller::start_view_dogs()
{
    dogs.view();
}


void Controller::next_dog()
{
    dogs.next();
}


Dog Controller::get_current_dog_from_list()
{
    return dogs.get_current_dog();
}
