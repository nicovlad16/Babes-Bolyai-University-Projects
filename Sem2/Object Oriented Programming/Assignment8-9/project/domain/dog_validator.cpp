//
// Created by nvlad on 01.05.2018.
//

#include "dog_validator.h"


ValidationException::ValidationException(const std::string &_message) : message(_message) {}


const char *ValidationException::what() const noexcept
{
    return message.c_str();
}


void DogValidator::validate(const Dog &dog)
{
    std::string errors;
    if (dog.get_breed().empty())
        errors += "Invalid breed. ";
    if (dog.get_name().empty())
        errors += "Invalid name. ";
    if (dog.get_age() < 0 || dog.get_age() > 100)
        errors += "Invalid age. ";
    if (dog.get_photo().empty() || system(("wget --spider -q " + dog.get_photo()).c_str()) != 0)
        errors += "Invalid photo url.";
    if (errors.length())
        throw ValidationException(errors);
}