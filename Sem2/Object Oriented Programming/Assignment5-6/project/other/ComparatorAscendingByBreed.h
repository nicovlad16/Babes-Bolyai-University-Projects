//
// Created by nvlad on 25.04.2018.
//

#ifndef ASSIGNMENT8_9_COMPARATORASCENDINGBYBREED_H
#define ASSIGNMENT8_9_COMPARATORASCENDINGBYBREED_H


#include "../domain/dog.h"
#include "Comparator.h"

class ComparatorAscendingByBreed: public Comparator<Dog>
{
public:
    bool compare(const Dog &dog1, const Dog &dog2);
};


#endif //ASSIGNMENT8_9_COMPARATORASCENDINGBYBREED_H
