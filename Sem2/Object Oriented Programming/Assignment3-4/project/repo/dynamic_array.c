//
// Created by nvlad on 12.03.2018.
//

#include <malloc.h>
#include "dynamic_array.h"

DynamicVector *
create_dynamic_vector(int capacity, DestroyElementFuntionType destroy_element, CopyElementFunctionType copy_element)
{
/* creates a new dynamic array, with given capacity, a function to destroy an element and to copy an element
 * return: pointer to the array, if it was created
 *         NULL - in case of some error */
    DynamicVector *vector;
    vector = (DynamicVector *) malloc(sizeof(DynamicVector));
    if (vector == NULL)
        return NULL;

    vector->capacity = capacity;
    vector->length = 0;

    vector->elems = (TElement *) malloc(sizeof(TElement) * capacity);
    if (vector->elems == NULL)
        return NULL;

    vector->destroy_element = destroy_element;
    vector->copy_element = copy_element;

    return vector;
}

void destroy_dynamic_vector(DynamicVector *vector)
{
/* destroys a dynamic vector, by destoying first each element in the repository, freeing the memory */
    int i;

    if (vector == NULL)
        return;

    i = 0;
    while (i < vector->length)
    {
        (vector->destroy_element)(vector->elems[i]);
        i++;
    }
    free(vector->elems);
    vector->elems = NULL;
    free(vector);
}

int get_length(DynamicVector *vector)
{
/* return: the number of elements, if the dynamic vector exists
 *         -1, otherwise */
    if (vector == NULL)
        return -1;
    return vector->length;
}

static int resize(DynamicVector *vector)
{
/* makes a bigger array, in order to have enough space for storing the elements */
    TElement *new_elems;
    int i;

    if (vector == NULL)
        return -1;
    vector->capacity *= 2;
    new_elems = (TElement *) malloc(sizeof(TElement) * vector->capacity);
    if (new_elems == NULL)
        return -1;

    i = 0;
    while (i < vector->length)
    {
        new_elems[i] = vector->elems[i];
        i++;
    }
    free(vector->elems);
    vector->elems = new_elems;
    return 0;
}

void add(DynamicVector *vector, TElement elem)
{
/* adds a new element to the array, resizing the array if there is not enough space*/
    if (vector == NULL)
        return;
    if (vector->elems == NULL)
        return;
    if (vector->length == vector->capacity)
        resize(vector);
    vector->elems[vector->length] = elem;
    vector->length += 1;
}

TElement get_element_from_position(DynamicVector *vector, int i)
{
/* return: the element from the i-th position*/
    return vector->elems[i];
}

void delete(DynamicVector *vector, int pos)
{
/* deletes the element from the i-th position */
    int i;

    if (vector == NULL)
        return;
    if (vector->elems == NULL)
        return;
    if (pos < 0 || pos >= vector->length)
        return;
    vector->destroy_element(vector->elems[pos]);
    i = pos + 1;
    while (i < vector->length)
    {
        vector->elems[i - 1] = vector->elems[i];
        i++;
    }
    vector->length -= 1;
}

DynamicVector *copy_vector(DynamicVector *vector)
{
/* makes a copy of the array, copying each element in the new array */
    DynamicVector *new_vector;
    TElement existing;
    TElement new_element;
    int i;

    new_vector = create_dynamic_vector(10, vector->destroy_element, vector->copy_element);
    i = 0;
    while (i < vector->length)
    {
        existing = get_element_from_position(vector, i);
        new_element = (TElement) (vector->copy_element)(existing);
        add(new_vector, new_element);
        i++;
    }
    return new_vector;
}
