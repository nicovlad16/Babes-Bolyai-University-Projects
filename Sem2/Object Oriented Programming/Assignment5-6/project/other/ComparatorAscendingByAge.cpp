//
// Created by nvlad on 26.04.2018.
//

#include "ComparatorAscendingByAge.h"


bool ComparatorAscendingByAge::compare(const Dog &dog1, const Dog &dog2)
{
    return dog1.get_age() < dog2.get_age();
}
