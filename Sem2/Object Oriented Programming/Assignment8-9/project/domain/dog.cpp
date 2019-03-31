//
// Created by nvlad on 01.05.2018.
//

#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <vector>
#include <sstream>
#include "dog.h"
#include "../utils/utils.h"

Dog::Dog() = default;


void Dog::view_photo()
{
    std::string open_url = "chromium-browser  ";
    open_url += photo;
    system(open_url.c_str());
}


Dog::Dog(const std::string &breed, const std::string &name, const int age, const std::string &photo)
{
    this->breed = breed;
    this->name = name;
    this->age = age;
    this->photo = photo;
}


bool Dog::operator==(const Dog &rhs) const
{
    return breed == rhs.breed &&
           name == rhs.name &&
           age == rhs.age &&
           photo == rhs.photo;
}


bool Dog::operator!=(const Dog &rhs) const
{
    return !(rhs == *this);
}


Dog::~Dog() = default;


const std::string &Dog::get_breed() const
{
    return breed;
}


void Dog::set_breed(const std::string &breed)
{
    Dog::breed = breed;
}


const std::string &Dog::get_name() const
{
    return name;
}


void Dog::set_name(const std::string &name)
{
    Dog::name = name;
}


int Dog::get_age() const
{
    return age;
}


void Dog::set_age(int age)
{
    Dog::age = age;
}


const std::string &Dog::get_photo() const
{
    return photo;
}


void Dog::set_photo(const std::string &photo)
{
    Dog::photo = photo;
}




std::ostream &operator<<(std::ostream &os, const Dog &dog)
{
    os << dog.get_breed() << "," << dog.name << "," << dog.get_age() << "," << dog.get_photo() << "\n";
    return os;
}


std::istream &operator>>(std::istream &is, Dog &dog)
{
    std::string line;
    getline(is, line);
    std::vector<std::string> elems;

    elems = split(line, ',');
    if (elems.size() != 4)
        return is;
    dog.breed = elems[0];
    dog.name = elems[1];
    dog.age = stoi(elems[2]);
    dog.photo = elems[3];
    return is;
}
