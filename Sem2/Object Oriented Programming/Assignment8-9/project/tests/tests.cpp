//
// Created by nvlad on 01.05.2018.
//

#include "tests.h"
#include <cassert>
#include <cstring>
#include <cstdlib>
#include "tests.h"
#include "../domain/dog.h"
#include "../service/ctrl.h"
#include "../domain/dog_validator.h"


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
    DogValidator::validate(dog2);

    Dog dog3("", "cuțu", 3, "https://bit.ly/2q2SM2e");
    try
    {
        DogValidator::validate(dog3);
    }
    catch (std::exception &e)
    {
        assert(strcmp(e.what(), "Invalid breed. ") == 0);
    }
    assert(dog != dog3);

    Dog dog4("câine-lup", "", 3, "https://bit.ly/2q2SM2e");
    try
    {
        DogValidator::validate(dog4);
    }
    catch (std::exception &e)
    {
        assert(strcmp(e.what(), "Invalid name. ") == 0);
    }

    Dog dog5("câine-lup", "cuțu", 450, "https://bit.ly/2q2SM2e");
    try
    {
        DogValidator::validate(dog5);
    }
    catch (std::exception &e)
    {
        assert(strcmp(e.what(), "Invalid age. ") == 0);
    }

//    dog.view_photo();
}


void Tests::test_repo()
{
    Repository<Dog> repo("../tests/dogs_tests");

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
    catch (std::exception &e)
    {
        assert(strcmp(e.what(), "Existing element.") == 0);
    }

    repo.remove(dog2);
    try
    {
        repo.remove(dog2);
    }
    catch (std::exception &e)
    {
        assert(strcmp(e.what(), "Inexisting element.") == 0);
    }
    assert(repo.get_length() == 1);

    repo.update(dog, dog2);
    try
    {
        repo.update(dog, dog2);
    }
    catch (std::exception &e)
    {
        assert(strcmp(e.what(), "Inexisting element.") == 0);
    }
    assert(!repo.find(dog));
    assert(repo.find(dog2));
    assert(repo.get_length() == 1);
    repo.remove(dog2);
}


void Tests::test_ctrl()
{
    Repository<Dog> repo("../tests/dogs_tests");
    Controller ctrl(repo);

    ctrl.add_dog_to_shelter("câine-lup", "cuțu", 3, "https://bit.ly/2q2SM2e");
    ctrl.add_dog_to_shelter("câine-lup", "cuțu", 21, "https://bit.ly/2q2SM2e");
    try
    {
        ctrl.add_dog_to_shelter("câine-lup", "cuțu", 3, "https://bit.ly/2q2SM2e");
    }
    catch (std::exception &e)
    {
        assert(strcmp(e.what(), "Existing dog.") == 0);
    }

    ctrl.remove_dog_from_shelter("câine-lup", "cuțu", 21, "https://bit.ly/2q2SM2e");
    try
    {
        ctrl.remove_dog_from_shelter("câine-lup", "cuțu", 21, "https://bit.ly/2q2SM2e");
    }
    catch (std::exception &e)
    {
        assert(strcmp(e.what(), "Inexisting dog.") == 0);
    }

    ctrl.update_dog_shelter("câine-lup", "cuțu", 3, "https://bit.ly/2q2SM2e", "câine-lup", "Laika", 7, "www.google.ro");
    try
    {
        ctrl.update_dog_shelter("câine-lup", "cuțu", 3, "https://bit.ly/2q2SM2e",
                                "câine-lup", "Laika", 7, "www.google.ro");
    }
    catch (std::exception &e)
    {
        assert(strcmp(e.what(), "Inexisting dog.") == 0);
    }
    ctrl.remove_dog_from_shelter("câine-lup", "Laika", 7, "www.google.ro");
}


void Tests::test_all()
{
    test_dog();
    test_repo();
    test_ctrl();
}