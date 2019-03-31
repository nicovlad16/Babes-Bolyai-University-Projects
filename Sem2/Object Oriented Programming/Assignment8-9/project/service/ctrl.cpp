//
// Created by nvlad on 01.05.2018.
//

#include "ctrl.h"
#include "../domain/dog_validator.h"


ControllerException::ControllerException(const std::string &_message) : message(_message) {}


const char *ControllerException::what() const noexcept
{
    return message.c_str();
}


void
Controller::add_dog_to_shelter(const std::string &breed, const std::string &name, int age, const std::string &photo)
{
    Dog dog{breed, name, age, photo};
    DogValidator::validate(dog);
    try
    {
        repo.add(dog);
    }
    catch (std::exception &e)
    {
        throw ControllerException("Existing dog.");
    }
}


void Controller::remove_dog_from_shelter(const std::string &breed, const std::string &name, int age,
                                         const std::string &photo)
{
    Dog dog{breed, name, age, photo};
    DogValidator::validate(dog);
    try
    {
        repo.remove(dog);
    }
    catch (std::exception &e)
    {
        throw ControllerException("Inexisting dog.");
    }
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
        throw ControllerException("Old dog: " + e);
    }

    Dog new_dog{new_breed, new_name, new_age, new_photo};
    try
    {
        DogValidator::validate(old_dog);
    }
    catch (std::string &e)
    {
        throw ControllerException("New dog: " + e);
    }

    try
    {
        repo.update(old_dog, new_dog);
    }
    catch (std::exception &e)
    {
        throw ControllerException("Inexisting dog.");
    }
}


void Controller::view_all_dogs()
{
    if (dogs == nullptr)
        return;

    dogs->clear_list();
    std::vector<Dog> all_dogs = repo.get_all();

    int i = 0;
    while (i < all_dogs.size())
    {
        dogs->add(all_dogs[i]);
        i++;
    }
}


void Controller::view_filtered_dogs(const std::string &breed, int age)
{
    if (dogs == nullptr)
        return;

    dogs->clear_list();
    std::vector<Dog> all_dogs = repo.get_all();

    if (breed.empty())
    {
        int i = 0;
        while (i < all_dogs.size())
        {
            if (all_dogs[i].get_age() < age)
                dogs->add(all_dogs[i]);

            i++;
        }
    } else
    {
        int i = 0;
        while (i < all_dogs.size())
        {
            if (all_dogs[i].get_breed() == breed && all_dogs[i].get_age() < age)
                dogs->add(all_dogs[i]);
            i++;
        }
    }
}


void Controller::adopt_dog()
{
    if (dogs == nullptr)
        return;

    Dog dog = dogs->get_current_dog();
    adopted.push_back(dog);
    dogs->remove(dog);
    repo.remove(dog);
}


std::vector<Dog> Controller::get_all_dogs_shelter()
{
    return repo.get_all();
}


std::vector<Dog> Controller::get_all_adopted_dogs()
{
    return adopted;
}


std::vector<Dog> Controller::get_dog_list()
{
    return dogs->get_all();
}


void Controller::start_view_dogs()
{
    if (dogs == nullptr)
        return;

    dogs->view();
}


void Controller::next_dog()
{
    if (dogs == nullptr)
        return;

    dogs->next();
}


Dog Controller::get_current_dog_from_list()
{
    return dogs->get_current_dog();
}


void Controller::set_adopted_file(FileDogList *pList)
{
    dogs = pList;
}


void Controller::save_doglist(const std::string &filename)
{
    if (dogs == nullptr)
        return;

    dogs->set_filename("../" + filename);
    dogs->write_to_file(adopted);
}


FileDogList *Controller::get_doglist() const { return dogs; }


std::string Controller::get_current_file()
{
    if (dogs == nullptr)
        return nullptr;
    return dogs->get_filename();

}


void Controller::see_adopted_file()
{
    if (dogs == nullptr)
        return;

    dogs->display_doglist();
}


Controller::~Controller()
{
    delete dogs;
}
