//
// Created by nvlad on 26.04.2018.
//

#ifndef ASSIGNMENT8_9_COMPARATORASCENDINGBYAGE_H
#define ASSIGNMENT8_9_COMPARATORASCENDINGBYAGE_H


#include "Comparator.h"
#include "../domain/dog.h"

class ComparatorAscendingByAge: public Comparator<Dog>
{
public:
    bool compare(const Dog &dog1, const Dog &dog2);
};


#endif //ASSIGNMENT8_9_COMPARATORASCENDINGBYAGE_H
