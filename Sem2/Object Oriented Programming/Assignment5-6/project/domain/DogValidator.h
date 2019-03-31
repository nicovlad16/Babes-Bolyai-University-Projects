//
// Created by nvlad on 21.04.2018.
//

#ifndef ASSIGNMENT8_9_DOGVALIDATOR_H
#define ASSIGNMENT8_9_DOGVALIDATOR_H


#include "dog.h"

class DogValidator
{
public:
    static void validate(const Dog &dog);
    /* checks if the dog's data is valid, that is:
     *      - breed is a non-empty string
     *      - name is a non-empty string
     *      - age is greater than 0, and smaller than 100
     *      - photo-link is a valid url */
};


#endif //ASSIGNMENT8_9_DOGVALIDATOR_H
