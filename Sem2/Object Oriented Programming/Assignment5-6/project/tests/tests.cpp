//
// Created by nvlad on 15.04.2018.
//

#include <cassert>
#include <cstring>
#include <zconf.h>
#include <cstdlib>
#include "tests.h"
#include "../domain/dog.h"
#include "../repo/dynamic_array.h"
#include "../service/ctrl.h"
#include "../domain/DogValidator.h"
#include "../other/ComparatorAscendingByAge.h"
#include "../other/ComparatorAscendingByBreed.h"


void Tests::test_dog()
{

    Dog dog("câine-lup", "cuțu", 3, "https://bit.ly/2q2SM2e");
    assert(dog.get_breed() == "câine-lup");
    assert(dog.get_name() == "cuțu");
    assert(dog.get_age() == 3);
    assert(dog.get_photo() == "https://bit.ly/2q2SM2e");

    Dog dog2("câine-lup", "cuțu", 3, "https://bit.ly/2q2SM2e");
    assert(dog == dog2);

    DogValidator::validate(dog);

    Dog dog3("", "cuțu", 3, "https://bit.ly/2q2SM2e");
    try
    {
        DogValidator::validate(dog3);
    }
    catch (std::string &e)
    {
        assert(e == "Invalid breed. ");
    }
    assert(dog != dog3);

    Dog dog4("câine-lup", "", 3, "https://bit.ly/2q2SM2e");
    try
    {
        DogValidator::validate(dog4);
    }
    catch (std::string &e)
    {
        assert(e == "Invalid name. ");
    }

    Dog dog5("câine-lup", "cuțu", 450, "https://bit.ly/2q2SM2e");
    try
    {
        DogValidator::validate(dog5);
    }
    catch (std::string &e)
    {
        assert(e == "Invalid age. ");
    }

    Dog dog6("câine-lup", "cuțu", -5, "https://bit.ly/2q2SM2e");
    try
    {
        DogValidator::validate(dog6);
    }
    catch (std::string &e)
    {
    }

    Dog dog7("câine-lup", "cuțu", 45, "hello world");
    try
    {
        DogValidator::validate(dog7);
    }
    catch (std::string &e)
    {
    }

    Dog dog8("câine", "cuțu", 45, "hello world");

    ComparatorAscendingByAge comparator_age;
    ComparatorAscendingByBreed comparator_breed;

    assert(comparator_age.compare(dog6, dog7));
    assert(!comparator_age.compare(dog5, dog6));
    assert(comparator_breed.compare(dog8, dog7));
    assert(!comparator_breed.compare(dog6, dog7));

//    dog.view_photo();
}


void Tests::test_dynamic_array()
{
    DynamicArray<int> v1(2);

    assert(v1.get_length() == 0);
    v1.add(57);
    assert(v1.get_length() == 1);
    v1.add(3);
    assert(v1.get_length() == 2);

    int a = 3;
    assert(v1.find(a));
    a = 100;
    assert(!v1.find(a));
    assert(!v1.find(155));

    DynamicArray<int> v2 = v1;

    assert(v2.get_length() == 2);
    assert(v1[0] == 57);
    assert(v2[1] == 3);

    int *v3;

    v3 = v1.get_all();
    assert(v3[1] == 3);

    v1 = v1 + 5;
    assert(v1.get_length() == 3);

    v1 = v1 - 57;
    assert(v1.get_length() == 2);
    assert(v1[0] == 3);

    v1.remove(0);
    assert(v1.get_length() == 1);
    assert(v1[0] == 5);

    v1.update(0, 23);
    assert(v1.get_length() == 1);
    assert(v1[0] == 23);

}


void Tests::test_repo()
{
    Repository repo;
    Dog dog("câine-lup", "cuțu", 3, "https://bit.ly/2q2SM2e");
    Dog dog2("câine-lup", "cuțu", 55, "https://bit.ly/2q2SM2e");

    assert(repo.get_length() == 0);
    repo.add(dog);
    assert(repo.find(dog));
    assert(!repo.find(dog2));
    repo.add(dog2);
    assert(repo.get_length() == 2);


    try
    {
        repo.add(dog);
    }
    catch (char const *e)
    {
        assert(strcmp(e, "Existing dog.") == 0);
    }

    repo.remove(dog2);
    try
    {
        repo.remove(dog2);
    }
    catch (char const *e)
    {
        assert(strcmp(e, "Inexisting dog.") == 0);
    }
    assert(repo.get_length() == 1);

    repo.update(dog, dog2);
    try
    {
        repo.update(dog, dog2);
    }
    catch (char const *e)
    {
        assert(strcmp(e, "Inexisting dog.") == 0);
    }
    assert(!repo.find(dog));
    assert(repo.find(dog2));
    assert(repo.get_length() == 1);
}


void Tests::test_ctrl()
{
    Repository repo;
    Controller ctrl(repo);

    ctrl.add_dog_to_shelter("câine-lup", "cuțu", 3, "https://bit.ly/2q2SM2e");
    ctrl.add_dog_to_shelter("câine-lup", "cuțu", 21, "https://bit.ly/2q2SM2e");
    try
    {
        ctrl.add_dog_to_shelter("câine-lup", "cuțu", 3, "https://bit.ly/2q2SM2e");
    }
    catch (char const *e)
    {
        assert(strcmp(e, "Existing dog.") == 0);
    }

    ctrl.remove_dog_from_shelter("câine-lup", "cuțu", 21, "https://bit.ly/2q2SM2e");
    try
    {
        ctrl.remove_dog_from_shelter("câine-lup", "cuțu", 21, "https://bit.ly/2q2SM2e");
    }
    catch (char const *e)
    {
        assert(strcmp(e, "Inexisting dog.") == 0);
    }

    ctrl.update_dog_shelter("câine-lup", "cuțu", 3, "https://bit.ly/2q2SM2e", "câine-lup", "Laika", 7, "www.google.ro");
    try
    {
        ctrl.update_dog_shelter("câine-lup", "cuțu", 3, "https://bit.ly/2q2SM2e", "câine-lup", "Laika", 7,
                                "www.google.ro");
    }
    catch (char const *e)
    {
        assert(strcmp(e, "Inexisting dog.") == 0);
    }

}


void Tests::test_all()
{
    test_dog();
    test_dynamic_array();
    test_repo();
    test_ctrl();
}