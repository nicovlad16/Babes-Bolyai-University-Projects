//
// Created by nvlad on 01.05.2018.
//

#ifndef ASSIGNMENT8_9_DOGLIST_H
#define ASSIGNMENT8_9_DOGLIST_H

#include <vector>
#include "dog.h"

class FileDogList
{
protected:
    std::vector<Dog> dogs;
    int current;
    std::string filename;

public:
    /* creates a view_list of the dogs in the shelter */
    FileDogList();

    /* destroy the objectg */
    virtual ~FileDogList() = default;

    /* adds a dog to the view_list */
    void add(const Dog &dog);

    /* returns the dog that is currently viewed */
    Dog get_current_dog();

    /* starts the view_list - showing the first dog */
    void view();

    /* shows the next dog from the view_list */
    void next();

    /* removes a dog from the view_list */
    void remove(const Dog &dog);

    /* deletes all the dogs from the view_list */
    void clear_list();

    /* returns an array with the dogs in the view_list */
    std::vector<Dog> get_all();

    /* changes the current file, for writing and opening with a different program */
    virtual void set_filename(const std::string &filename) = 0;

    /* writes the adopted dog list to file
       throws: FileException - if it cannot write */
    virtual void write_to_file(std::vector<Dog> adopted) = 0;

    /* displays the adopted dogs list using a program/app */
    virtual void display_doglist() const = 0;

    /* returns the name of the current file */
    std::string get_filename();
};

#endif //ASSIGNMENT8_9_DOGLIST_H
