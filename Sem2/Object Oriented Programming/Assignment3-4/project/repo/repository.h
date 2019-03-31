//
// Created by nvlad on 12.03.2018.
//

#ifndef ASSIGNMENT3_4_REPOSITORY_H
#define ASSIGNMENT3_4_REPOSITORY_H

#include "dynamic_array.h"
#include "list.h"

typedef void (*DestroyElementFuntionType)(void *);

typedef int (*EqualElementsFuntionType)(TElement, TElement);

typedef TElement (*CopyElementFunctionType)(void *);


typedef struct
{
    EqualElementsFuntionType equal;
    DynamicVector *elements;
} Repository;


Repository *create_repository(DestroyElementFuntionType destroy_element, EqualElementsFuntionType equal,
                              CopyElementFunctionType copy_element);

void destroy_repository(Repository *repo);

int size(Repository *repo);

int add_repo(Repository *repo, TElement elem);

TElement find_element_repo(Repository *repo, TElement elem);

int delete_element_repo(Repository *repo, TElement elem);

int find_position_of_element(Repository *repo, TElement elem);

DynamicVector *get_vector(Repository *repo);

int update_repo(Repository *repo, TElement existing, TElement new);

t_list *get_elements(Repository *repo);

void change_elements(Repository *repo, DynamicVector *elems);

#endif //ASSIGNMENT3_4_REPOSITORY_H
