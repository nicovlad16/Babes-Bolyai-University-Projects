//
// Created by nvlad on 18.04.2018.
//

#ifndef ASSIGNMENT8_9_DOGLIST_H
#define ASSIGNMENT8_9_DOGLIST_H

#include "dog.h"
#include "../repo/dynamic_array.h"

class DogList
{
private:
    DynamicArray<Dog> dogs;
    int current;

public:
    DogList();

    explicit DogList(DynamicArray<Dog> const &dogs);

    /* creates a view_list of the dogs in the shelter */

    void add(const Dog &dog);

    /* adds a dog to the view_list */


    Dog get_current_dog();

    /* returns the dog that is currently viewed */

    void view();

    /* starts the view_list - showing the first dog */

    void next();

    /* shows the next dog from the view_list */

    bool isEmpty();

    /* checks if there are no dogs to be viewed */

    void remove(const Dog &dog);

    /* removes a dog from the view_list */

    void clear_list();

    /* deletes all the dogs from the view_list */

    DynamicArray<Dog> get_all();
    /* returns an array with the dogs in the view_list */
};


#endif //ASSIGNMENT8_9_DOGLIST_H
