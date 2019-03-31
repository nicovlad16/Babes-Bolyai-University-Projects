//
// Created by nvlad on 19.03.2018.
//

#include <malloc.h>
#include "list.h"

t_list *ft_create_elem(void *data)
{
/* creates a new node in the list, with the given data
 * return: pointer to the node */
    t_list *list;

    list = (t_list *) malloc(sizeof(t_list));
    if (list)
    {
        list->data = data;
        list->next = 0;
    }
    return (list);
}

void ft_list_add_to_the_end(t_list **begin_list, void *data)
{
/* adds a new node at the end of the list, with the given data
 * the new node is being created then added */
    t_list *list;

    if (*begin_list == 0)
        *begin_list = ft_create_elem(data);
    else
    {
        list = *begin_list;
        while (list->next != 0)
            list = list->next;
        list->next = ft_create_elem(data);
    }
}

void ft_list_add_to_the_beginning(t_list **begin_list, void *data)
{
/* adds a new node at the beginning of the list, with the given data
 * the new node is being created then added */

    t_list *list;

    if (*begin_list == 0)
        *begin_list = ft_create_elem(data);
    else
    {
        list = ft_create_elem(data);
        list->next = *begin_list;
        *begin_list = list;
    }
}

int ft_list_size(t_list *begin_list)
{
/* return: the number of nodes in the list */
    int i;
    t_list *list;

    i = 0;
    list = begin_list;
    if (begin_list == 0)
        return (0);
    else
    {
        while (list->next != 0)
        {
            i++;
            list = list->next;
        }
        return (i + 1);
    }
}

void ft_list_clear(t_list **begin_list)
{
/* deletes all the nodes in the list, and frees the used memory */
    t_list *list;
    t_list *next;

    list = *begin_list;
    while (list != 0)
    {
        next = list->next;
        free(list);
        list = next;
    }
    *begin_list = 0;
}

void ft_list_foreach(t_list *begin_list, void (*f)(void *))
{
/* applies a function on the data of the each node in the list*/
    t_list *list_ptr;

    list_ptr = begin_list;
    while (list_ptr)
    {
        (*f)(list_ptr->data);
        list_ptr = list_ptr->next;
    }
}

t_list *sort_list(t_list *lst, int (*cmp)(void *, void *))
{
/* sorts the nodes by a given function */
    t_list *new;
    t_list *temp;
    void *aux;

    new = lst;
    while (new)
    {
        temp = new->next;
        while (temp)
        {
            if ((*cmp)(new->data, temp->data) == 0)
            {
                aux = new->data;
                new->data = temp->data;
                temp->data = aux;
            }
            temp = temp->next;
        }
        new = new->next;
    }
    return (lst);
}

void ft_list_remove_if(t_list **begin_list, void *data_ref, int (*cmp)(void *, void *))
{
/* filters the list by a given function */

    t_list *current;
    t_list *previous;

    current = *begin_list;
    previous = *begin_list;
    while (current)
    {
        if ((*cmp)(current->data, data_ref) == 0)
        {
            if (current == *begin_list)
            {
                *begin_list = current->next;
                free(current);
                current = *begin_list;
                previous = *begin_list;
            } else
            {
                previous->next = current->next;
                free(current);
                current = previous->next;
            }
        } else
        {
            previous = current;
            current = current->next;
        }
    }
}



