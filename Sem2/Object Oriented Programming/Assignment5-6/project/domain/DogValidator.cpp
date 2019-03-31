//
// Created by nvlad on 21.04.2018.
//

#include "DogValidator.h"


void DogValidator::validate(const Dog &dog)
{
    std::string errors;
    if (dog.get_breed().empty())
        errors +="Invalid breed. ";
    if (dog.get_name().empty())
        errors += "Invalid name. ";
    if (dog.get_age() < 0 || dog.get_age() > 100)
        errors += "Invalid age. ";
    if (dog.get_photo().empty() || system(("wget --spider -q " + dog.get_photo()).c_str()) != 0)
        errors += "Invalid photo url.";
    if (errors.length())
        throw (errors);
}
