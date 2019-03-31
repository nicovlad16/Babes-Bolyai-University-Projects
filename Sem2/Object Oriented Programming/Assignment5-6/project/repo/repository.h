//
// Created by nvlad on 15.04.2018.
//

#ifndef ASSIGNMENT8_9_REPOSITORY_H
#define ASSIGNMENT8_9_REPOSITORY_H


#include "dynamic_array.h"
#include "../domain/dog.h"

class Repository
{
private:
    DynamicArray<Dog> dogs;
public:
    /* uses the default constructor to create the repository */
    Repository() = default;

    /* adds a new dog to the repository
     * if it exists, exception is thrown */
    void add(const Dog &dog);

    /* returns an array with all the dogs in the repository */
    DynamicArray<Dog> get_all();

    /* returns the number of dogs in the repository */
    int get_length();

    /* checks if a given dog exists in the repository */
    bool find(const Dog &dog);

    /* removes an existing dog from the repository
     * if it doesn't exist, exception is thrown */
    void remove(const Dog &dog);

    /* updates an existing dog with a new one
     * if it doesn't exist, exception is thrown */
    void update(const Dog old_dog, const Dog new_dog);

};

#endif //ASSIGNMENT8_9_REPOSITORY_H
