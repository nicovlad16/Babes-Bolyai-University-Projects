//
// Created by nvlad on 18.04.2018.
//

#include "doglist.h"
#include "dog.h"


DogList::DogList()
{
    this->current = 0;
}


void DogList::add(const Dog &dog)
{
    this->dogs.add(dog);
}


Dog DogList::get_current_dog()
{
    if (this->current == this->dogs.get_length())
        this->current = 0;
    return this->dogs[this->current];
}


void DogList::view()
{
    if (this->dogs.get_length() == 0)
        return;
    this->current = 0;
    Dog currentDog = this->get_current_dog();
}


void DogList::next()
{
    if (this->dogs.get_length() == 0)
        return;
    this->current++;
    Dog currentDog = this->get_current_dog();
}


bool DogList::isEmpty()
{
    return this->dogs.get_length() == 0;
}


DogList::DogList(DynamicArray<Dog> const &dogs)
{
    this->dogs = dogs;
}


void DogList::remove(const Dog &dog)
{
    int pos = dogs.get_pos(dog);
    dogs.remove(pos);
}


void DogList::clear_list()
{
    int i = dogs.get_length() - 1;
    while (i >= 0)
    {
        dogs.remove(i);
        i--;
    }
}


DynamicArray<Dog> DogList::get_all()
{
    return dogs;
}
