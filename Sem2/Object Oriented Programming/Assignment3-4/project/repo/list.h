//
// Created by nvlad on 19.03.2018.
//

#ifndef ASSIGNMENT3_4_LIST_H
#define ASSIGNMENT3_4_LIST_H

typedef void (*ForeachElementListFunctionType)(void *);

typedef struct s_list
{
    struct s_list *next;
    void *data;
} t_list;

t_list *ft_create_elem(void *data);

int ft_list_size(t_list *begin_list);

void ft_list_clear(t_list **begin_list);

void ft_list_foreach(t_list *begin_list, void (*f)(void *));

void ft_list_add_to_the_end(t_list **begin_list, void *data);

void ft_list_add_to_the_beginning(t_list **begin_list, void *data);

t_list *sort_list(t_list *lst, int (*cmp)(void *, void *));

void ft_list_remove_if(t_list **begin_list, void *data_ref, int (*cmp)(void *, void *));

#endif //ASSIGNMENT3_4_LIST_H


