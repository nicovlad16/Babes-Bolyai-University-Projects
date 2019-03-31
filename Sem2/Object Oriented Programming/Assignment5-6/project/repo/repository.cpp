//
// Created by nvlad on 15.04.2018.
//

#include "repository.h"


void Repository::add(const Dog &dog)
{
    if (find(dog))
        throw ("Existing dog.");
    this->dogs.add(dog);
}


DynamicArray<Dog> Repository::get_all()
{
    return dogs;
}


int Repository::get_length()
{
    return dogs.get_length();
}


bool Repository::find(const Dog &dog)
{
    return dogs.find(dog);
}


void Repository::remove(const Dog &dog)
{

//    if (!find(dog))
//        throw ("Inexisting dog.");
//    dogs.remove(dog);
    int pos = dogs.get_pos(dog);
    if (pos != -1)
        dogs.remove(pos);
    else
        throw ("Inexisting dog.");

////     pos != 1 ? dogs.remove(pos) : throw ("Inexisting dog.");
}


void Repository::update(const Dog old_dog, const Dog new_dog)
{
    int pos = dogs.get_pos(old_dog);
    if (pos != -1)
    {
        dogs.remove(pos);
        dogs.add(new_dog);
    } else
        throw ("Inexisting dog.");
}


