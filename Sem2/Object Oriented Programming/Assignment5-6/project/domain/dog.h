//
// Created by nvlad on 15.04.2018.
//

#ifndef ASSIGNMENT8_9_DOG_H
#define ASSIGNMENT8_9_DOG_H

#include <string>
#include <ostream>

class Dog
{
private:
    std::string breed;
    std::string name;
    int age;
    std::string photo;
public:
    Dog();

    virtual ~Dog();

    Dog(const std::string &breed, const std::string &name, int age, const std::string &photo);


    const std::string &get_breed() const;

    void set_breed(const std::string &breed);

    const std::string &get_name() const;

    void set_name(const std::string &name);

    int get_age() const;

    void set_age(int age);

    const std::string &get_photo() const;

    void set_photo(const std::string &photo);

    void view_photo();

    bool operator==(const Dog &rhs) const;

    bool operator!=(const Dog &rhs) const;

    friend std::ostream &operator<<(std::ostream &os, const Dog &dog);


};

#endif //ASSIGNMENT8_9_DOG_H
