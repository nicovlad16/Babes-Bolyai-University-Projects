//
// Created by nvlad on 25.04.2018.
//

#include "ComparatorAscendingByBreed.h"


bool ComparatorAscendingByBreed::compare(const Dog &dog1, const Dog &dog2)
{
    return dog1.get_breed() < dog2.get_breed();
}
