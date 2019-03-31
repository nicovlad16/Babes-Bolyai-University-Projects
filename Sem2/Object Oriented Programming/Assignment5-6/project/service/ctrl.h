//
// Created by nvlad on 18.04.2018.
//

#ifndef ASSIGNMENT8_9_CTRL_H
#define ASSIGNMENT8_9_CTRL_H


#include <utility>
#include "../repo/repository.h"
#include "../domain/doglist.h"

class Controller
{
private:
    Repository repo;
    DogList dogs;
    DynamicArray<Dog> adopted;

public:
    /* creates the controller */
    explicit Controller(Repository r) : repo(std::move(r)) {}


    /* returns the repository */
    Repository getRepo() const { return repo; }


    /* returns a view_list in order to view the dogs
     * which might be adopted */
    DogList getDogList() const { return dogs; }


    /* returns an array with the dogs which were adopted */
    DynamicArray<Dog> getAdoptedList() const { return adopted; }


    /* adds a dog with the given data to the shelter,
     * validating the input data first */
    void add_dog_to_shelter(const std::string &breed, const std::string &name, int age,
                            const std::string &photo);

    /* removes the current dog from the shelter
     * removes the current dog from the view_list
     * adds it to the adopted list */
    void adopt_dog();

    /* the view_list will have all the dogs from the repo */
    void view_all_dogs();

    /* the view_list will have the dogs from the shelter
     * which have the given breed, or all the dogs if it is empty
     * then checks if it a smaller age than the given one */
    void view_filtered_dogs(const std::string &breed, int age);

    /* returns an array with all the dogs in the shelter */
    DynamicArray<Dog> get_all_dogs_shelter();

    /* removes a dog with the given data from the shelter,
     * validating the input data first */
    void remove_dog_from_shelter(const std::string &breed, const std::string &name, int age, const std::string &photo);

    /* updates a dog with the given data, with a new dog,
    * validating the input data first */
    void update_dog_shelter(std::string old_breed, std::string old_name, int old_age, std::string old_photo,
                            std::string new_breed, std::string new_name, int new_age, std::string new_photo);

    /* returns an array with the adopted dogs */
    DynamicArray<Dog> get_all_adopted_dogs();

    /* the view_list will be set to start from the beginning */
    void start_view_dogs();

    /* sets the next dog to be viewed */
    void next_dog();

    /* returns an array with the dogs in the view_list */
    DynamicArray<Dog> get_dog_list();

    /* returns the dog which is currently viewed */
    Dog get_current_dog_from_list();
};


#endif //ASSIGNMENT8_9_CTRL_H
