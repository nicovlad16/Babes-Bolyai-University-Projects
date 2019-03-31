//
// Created by nvlad on 15.04.2018.
//

#include <cstring>
#include <cstdlib>
#include <zconf.h>
#include <cstdio>
#include <iostream>
#include "dog.h"


Dog::Dog() = default;


void Dog::view_photo()
{
    std::string open_url = "chromium-browser  ";
    open_url += photo;
    system(open_url.c_str());

//cealaltă variantă deschide doar un browser gol, fără url; de verificat de ce face asta

//    pid_t pid;
//    char *array[2];
//    array[0] = photo;
//    array[1] = nullptr;
//
//    pid = fork();
//    if (pid == 0)
//    {
//        if (execv("/usr/bin/chromium-browser", array) < 0)
//        {
//            printf("-1");
//            return;
//        }
//
//        else
//        {
//            printf("1");
//            return;
//        }
//    }
//    else if (pid > 0)
//    {
//        printf("2");
//        return;
//    }
//    else
//    {
//        printf("0");
//        return;
//    }
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


std::ostream &operator<<(std::ostream &os, const Dog &dog)
{
    os << "breed: " << dog.breed << "\tname: " << dog.name << "\tage: " << dog.age << "\tphoto: " << dog.photo;
    return os;
}


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