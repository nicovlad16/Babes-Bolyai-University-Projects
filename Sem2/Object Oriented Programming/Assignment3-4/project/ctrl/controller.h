//
// Created by nvlad on 12.03.2018.
//

#ifndef ASSIGNMENT3_4_CONTROLLER_H
#define ASSIGNMENT3_4_CONTROLLER_H

#include "../repo/repository.h"
#include "../domain/operation_stack.h"

typedef struct
{
    Repository *repo;
    OperationsStack *undo_stack;
    OperationsStack *redo_stack;
    t_list *undo_list;
    t_list *redo_list;
} Controller;

Controller *create_controller(Repository *repo, OperationsStack *undo_stack, OperationsStack *redo_stack,
                              t_list *undo_list, t_list *redo_list);

void destroy_controller(Controller *ctrl);

int add_material(Controller *ctrl, char *name, char *supplier, int quantity, int day, int month, int year);

int remove_material(Controller *ctrl, char *name, char *supplier, int day, int month, int year);

int update_material(Controller *ctrl, char *old_name, char *new_name, char *old_supplier, char *new_supplier,
                    int old_quantity, int new_quantity, int old_day, int new_day, int old_month, int new_month,
                    int old_year, int new_year);

t_list *get_all(Controller *ctrl);

t_list *filter1(Controller *ctrl, char *supplier, int quantity);

int filter2(Controller *ctrl, t_list **list, char *expiration_date);

t_list *filter3(Controller *ctrl, char *supplier, int quantity);

t_list *filter4(Controller *ctrl, int quantity);

t_list *filter5(Controller *ctrl, char *supplier);

t_list *filter6(Controller *ctrl, char *supplier);

int undo_list(Controller *ctrl);

int redo_list(Controller *ctrl);

int undo_stack(Controller *ctrl);

int redo_stack(Controller *ctrl);


#endif //ASSIGNMENT3_4_CONTROLLER_H
