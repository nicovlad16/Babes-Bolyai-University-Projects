//
// Created by nvlad on 12.03.2018.
//

#include <malloc.h>
#include "repository.h"


Repository *create_repository(DestroyElementFuntionType destroy_element, EqualElementsFuntionType equal,
                              CopyElementFunctionType copy_element)
{
/* creates a new repository, having: a function to destroy an element
 *                                   a function to copy an element
 *                                   a function to check if two elements are equal
 *                                   as storage a new created dynamic array
 * return: pointer to the new repository */
    Repository *repo;

    repo = (Repository *) malloc(sizeof(Repository));
    if (repo == NULL)
        return NULL;
    repo->equal = equal;
    repo->elements = create_dynamic_vector(10, destroy_element, copy_element);
    if (repo->elements == NULL)
        return NULL;
    return repo;
}

void destroy_repository(Repository *repo)
{
/* destroys the repository, destroying the storage first, and freeing the memory */

    if (repo == NULL)
        return;

    destroy_dynamic_vector(repo->elements);
    repo->elements = NULL;
    repo->equal = NULL;
    free(repo);
}

int size(Repository *repo)
{
/* returns the number of elements in the repository */
    if (repo == NULL)
        return -1;
    return get_length(repo->elements);
}

int add_repo(Repository *repo, TElement elem)
{
/* adds an element to the repository, if it does not exist
 * return: 1 - successfull add
 *         0 - the element exists */

    if (find_element_repo(repo, elem))
        return 0;
    add(repo->elements, elem);
    return 1;
}

TElement find_element_repo(Repository *repo, TElement elem)
{
/* finds an element in the repository
 * return: the element - if it exists
 *         NULL - otherwise */
    int i;
    TElement elem_from_pos;

    i = 0;
    while (i < get_length(repo->elements))
    {
        elem_from_pos = (TElement) get_element_from_position(repo->elements, i);
        if ((repo->equal)(elem_from_pos, elem))
            return elem_from_pos;
        i++;
    }
    return NULL;
}

int delete_element_repo(Repository *repo, TElement elem)
{
/* deletes an element from the repository, if it does exist
 * return: 1 - successfull delete
 *         0 - the element does not exist */
    TElement existing;
    int pos;

    existing = find_element_repo(repo, elem);
    if (existing)
    {
        pos = find_position_of_element(repo, elem);
        if (pos != -1)
        {
            delete(repo->elements, pos);
            return 1;
        }
    }
    return 0;
}

int find_position_of_element(Repository *repo, TElement elem)
{
/* finds the position of an element in the repository
 * return: the position - if it exists
 *         -1 - otherwise */
    int i;
    TElement elem_from_pos;

    i = 0;
    while (i < get_length(repo->elements))
    {


        elem_from_pos = (TElement) get_element_from_position(repo->elements, i);
        if ((repo->equal)(elem_from_pos, elem))
            return i;
        i++;
    }
    return -1;

}

int update_repo(Repository *repo, TElement existing, TElement new)
{
/* updates an element from the repository, if it exists
 * the existing element is deleted and the new one is added
 * return: 1 - the element was updated
 *         0 - the element does not exist */
    if (delete_element_repo(repo, existing))
        if (add_repo(repo, new))
            return 1;
    return 0;
}

DynamicVector *get_vector(Repository *repo)
{
/* return: a copy of the elements in the repository */
    return copy_vector(repo->elements);
}

t_list *get_elements(Repository *repo)
{
/* return: a list with the elements in the repository */
    int i;
    int len;
    TElement elem;
    t_list *lst;

    i = 0;
    lst = NULL;
    len = get_length(repo->elements);
    while (i < len)
    {
        elem = get_element_from_position(repo->elements, i);
        ft_list_add_to_the_beginning(&lst, elem);
        i++;
    }
    return lst;
}

void change_elements(Repository *repo, DynamicVector *elems)
{
/* change all the elements in the repository, with other elements */
    destroy_dynamic_vector(repo->elements);
    repo->elements = elems;
}

