//
// Created by nvlad on 12.03.2018.
//

#ifndef ASSIGNMENT3_4_DYNAMIC_ARRAY_H
#define ASSIGNMENT3_4_DYNAMIC_ARRAY_H

typedef void *TElement;

typedef void (*DestroyElementFuntionType)(void *);

typedef TElement (*CopyElementFunctionType)(void *);


typedef struct
{
    TElement *elems;
    int length;
    int capacity;
    DestroyElementFuntionType destroy_element;
    CopyElementFunctionType copy_element;
} DynamicVector;

DynamicVector *
create_dynamic_vector(int capacity, DestroyElementFuntionType destroy_element, CopyElementFunctionType copy_element);

void destroy_dynamic_vector(DynamicVector *vector);

int get_length(DynamicVector *vector);

void add(DynamicVector *vector, TElement elem);

void *get_element_from_position(DynamicVector *vector, int index);

void delete(DynamicVector *vector, int pos);

DynamicVector *copy_vector(DynamicVector *vector);


#endif //ASSIGNMENT3_4_DYNAMIC_ARRAY_H
