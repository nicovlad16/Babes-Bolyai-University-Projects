//
// Created by nvlad on 25.04.2018.
//

#ifndef ASSIGNMENT8_9_COMPARATOR_H
#define ASSIGNMENT8_9_COMPARATOR_H

template<typename TElement>
class Comparator
{
public:
    virtual bool compare(const TElement &elem1, const TElement &elem2) = 0;
};


#endif //ASSIGNMENT8_9_COMPARATOR_H
