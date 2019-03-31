//
// Created by nvlad on 01.05.2018.
//

#ifndef ASSIGNMENT8_9_DOG_VALIDATOR_H
#define ASSIGNMENT8_9_DOG_VALIDATOR_H


#include "dog.h"

class ValidationException: public std::exception
{
private:
    std::string message;
public:
    explicit ValidationException(const std::string &_message);
    const char *what() const noexcept override;

};


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

#endif //ASSIGNMENT8_9_DOG_VALIDATOR_H
