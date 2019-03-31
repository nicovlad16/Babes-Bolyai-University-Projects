//
// Created by nvlad on 01.05.2018.
//

#include "file_doglist.h"
#include "dog.h"
#include <algorithm>


FileDogList::FileDogList()
{
    current = 0;
}


void FileDogList::add(const Dog &dog)
{
    dogs.push_back(dog);
}


Dog FileDogList::get_current_dog()
{
    if (current == dogs.size())
        current = 0;
    return dogs[current];
}


void FileDogList::view()
{
    if (dogs.empty())
        return;
    current = 0;
    Dog currentDog = get_current_dog();
}


void FileDogList::next()
{
    if (dogs.empty())
        return;
    current++;
    Dog currentDog = get_current_dog();
}


void FileDogList::remove(const Dog &dog)
{
    dogs.erase(std::remove(dogs.begin(), dogs.end(), dog), dogs.end());
}


void FileDogList::clear_list()
{
    dogs.clear();
}


 std::vector<Dog> FileDogList::get_all()
{
    return dogs;
}


std::string FileDogList::get_filename()
{
    return filename;
}
