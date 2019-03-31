//
// Created by nvlad on 12.03.2018.
//

#include <malloc.h>
#include <string.h>
#include "controller.h"
#include "../domain/dd.mm.yyyy.h"

Controller *create_controller(Repository *repo, OperationsStack *undo_stack, OperationsStack *redo_stack,
                              t_list *undo_list, t_list *redo_list)
{
    /*  creates a controller, having a repository, undo and redo */
    Controller *ctrl;

    ctrl = (Controller *) malloc(sizeof(Controller));

    if (ctrl == NULL)
        return NULL;

    ctrl->repo = repo;

    ctrl->undo_stack = undo_stack;
    ctrl->redo_stack = redo_stack;

    ctrl->undo_list = undo_list;
    ctrl->redo_list = redo_list;

    return ctrl;
}

void destroy_undo_redo_list(t_list **list)
{
    t_list *new;

    new = *list;
    while (new)
    {
        destroy_dynamic_vector(new->data);
        new = new->next;
    }
    ft_list_clear(list);

}

void destroy_controller(Controller *ctrl)
{
    /*  destroys the memory allocated for the repository, undo, redo & controller */
//    t_list *new;

    if (ctrl == NULL)
        return;

    //destroy the repository
    destroy_repository(ctrl->repo);

    //destroy the operations_stacks
    destroy_stack(ctrl->undo_stack);
    destroy_stack(ctrl->redo_stack);

    //destroy the lists
    destroy_undo_redo_list(&ctrl->undo_list);
    destroy_undo_redo_list(&ctrl->redo_list);

    //free the memory allocated to the controller
    free(ctrl);
}

int add_material(Controller *ctrl, char *name, char *supplier, int quantity, int day, int month, int year)
{
/* checks the input data, if it is a valid material
* creates a new material
* adds the material to the repository, if it does not exist,
* else updates the existing material, adding the new quantity
* return: 0 - successfull add/update
*         1 - validation error */
    Material *new_material;
    Material *existing_material;
    char expiration_date[11];
//////    Operation *operation;
    DynamicVector *elements;

    elements = get_vector(ctrl->repo);

    if (valid_date(day, month, year) && quantity > 0)
    {
        sprintf(expiration_date, "%d.%d.%d", day, month, year);
        new_material = create_material(name, supplier, quantity, expiration_date);
        if (add_repo(ctrl->repo, new_material))
        {
            ft_list_add_to_the_beginning(&ctrl->undo_list, elements);
            destroy_undo_redo_list(&ctrl->redo_list);
//////            operation = create_operation(new_material, "add");
//////            push(ctrl->undo_stack, operation);
//////            destroy_operation(operation);
            return 0;
        } else
        {
            existing_material = (Material *) find_element_repo(ctrl->repo, new_material);
            new_material->quantity += existing_material->quantity;
            if (update_repo(ctrl->repo, existing_material, new_material))
            {
                ft_list_add_to_the_beginning(&ctrl->undo_list, elements);
                destroy_undo_redo_list(&ctrl->redo_list);
//////                operation = create_operation(new_material, "add");
//////                push(ctrl->undo_stack, operation);
//////                destroy_operation(operation);
                return 0;
            }
        }
    }
    destroy_dynamic_vector(elements);
    return 1;
}

int remove_material(Controller *ctrl, char *name, char *supplier, int day, int month, int year)
{
/* checks the input data, if it is a valid material
 * creates a new material
 * deletes the material from the repository, if it does exist
 * return: 0 - successfull delete
 *         1 - validation error
 *         2 - inexisting material
 *         3 - some other error*/
    Material *material;
    char expiration_date[11];
    int quantity = 0;
//////    Operation *operation;
    DynamicVector *elements;

    elements = get_vector(ctrl->repo);

    if (valid_date(day, month, year))
    {
        sprintf(expiration_date, "%d.%d.%d", day, month, year);
        material = create_material(name, supplier, quantity, expiration_date);
        if (material)
        {
            if (delete_element_repo(ctrl->repo, material))
            {
                destroy_material(material);
                ft_list_add_to_the_beginning(&ctrl->undo_list, elements);
                destroy_undo_redo_list(&ctrl->redo_list);
//////                operation = create_operation(material, "remove");
//////                push(ctrl->undo_stack, operation);
//////                destroy_operation(operation);
                return 0;
            }
            destroy_material(material);
            destroy_dynamic_vector(elements);
            return 2;
        }
        destroy_dynamic_vector(elements);
        return 3;
    }
    destroy_dynamic_vector(elements);
    return 1;

}

int update_material(Controller *ctrl, char *old_name, char *new_name, char *old_supplier, char *new_supplier,
                    int old_quantity, int new_quantity, int old_day, int new_day, int old_month, int new_month,
                    int old_year, int new_year)
{
/* checks the input data, if they are valid materials
 * creates new materials
 * updates the material from the repository with the new one, if it does exist
 * return: 0 - successfull delete
 *         1 - validation error
 *         2 - inexisting material
 *         3 - some other error*/
    Material *old_material;
    Material *new_material;
    char old_expiration_date[11];
    char new_expiration_date[11];
//////    Operation *operation;
    DynamicVector *elements;

    elements = get_vector(ctrl->repo);

    if (valid_date(old_day, old_month, old_year) && valid_date(new_day, new_month, new_year) && old_quantity > 0 &&
        new_quantity > 0)
    {
        sprintf(old_expiration_date, "%d.%d.%d", old_day, old_month, old_year);
        sprintf(new_expiration_date, "%d.%d.%d", new_day, new_month, new_year);

        old_material = create_material(old_name, old_supplier, old_quantity, old_expiration_date);
        new_material = create_material(new_name, new_supplier, new_quantity, new_expiration_date);

        if (old_material && new_material)
        {
            if (update_repo(ctrl->repo, old_material, new_material))
            {
                destroy_material(old_material);
                ft_list_add_to_the_beginning(&ctrl->undo_list, elements);
                destroy_undo_redo_list(&ctrl->redo_list);
//////                operation = create_operation(new_material, "update");
//////                push(ctrl->undo_stack, operation);
/////                destroy_operation(operation);
                return 0;
            }
            destroy_material(old_material);
            destroy_material(new_material);
            destroy_dynamic_vector(elements);
            return 2;
        }
        destroy_dynamic_vector(elements);
        return 3;
    }
    destroy_dynamic_vector(elements);
    return 1;
}

void convert_all_materials_to_string(t_list *lst)
{
/* converts a list of pointers to materials to strings*/
    while (lst)
    {
        lst->data = material_to_string((Material *) lst->data);
        lst = lst->next;
    }
}

t_list *get_all(Controller *ctrl)
{
/* return: a list with the strings of all the materials in the repository*/
    t_list *lst;

    lst = get_elements(ctrl->repo);
    convert_all_materials_to_string(lst);

    return lst;
}

t_list *filter1(Controller *ctrl, char *supplier, int quantity)
{
/* filters the elements in the repository by having a given supplier,
 * filters the elements again by having a quantity smaller than a given value,
 * sorts the elements by quantity, in ascending order
 * return: a list with the strings of all the materials in the repository */
    t_list *lst;

    lst = get_elements(ctrl->repo);

    ft_list_remove_if(&lst, supplier, &is_equal_supplier);
    ft_list_remove_if(&lst, &quantity, &greater_quantity);
    lst = sort_list(lst, &greater_quantity2);

    convert_all_materials_to_string(lst);

    return lst;
}

t_list *filter3(Controller *ctrl, char *supplier, int quantity)
{
/* filters the elements in the repository by having a given supplier,
 * filters the elements again by having a quantity smaller than a given value,
 * sorts the elements by quantity, in descending order
 * return: a list with the strings of all the materials in the repository */

    t_list *lst;

    lst = get_elements(ctrl->repo);
    ft_list_remove_if(&lst, supplier, &is_equal_supplier);
    ft_list_remove_if(&lst, &quantity, &greater_quantity);
    lst = sort_list(lst, &smaller_quantity2);

    convert_all_materials_to_string(lst);

    return lst;
}

int filter2(Controller *ctrl, t_list **list, char *expiration_date)
{
/* filters the elements in the repository by having the expiration date
 * smaller than a given date; if the date is empty, all materials are returned
 * return: a list with the strings of all the materials in the repository */
    t_list *lst;
    int day = 0;
    int month = 0;
    int year = 0;

    if (strlen(expiration_date) != 0)
    {
        sscanf(expiration_date, "%d.%d.%d", &day, &month, &year);
        if (!valid_date(day, month, year))
            return 1;

        lst = get_elements(ctrl->repo);
        ft_list_remove_if(&lst, expiration_date, &compare_expiration_date);

        convert_all_materials_to_string(lst);

        *list = lst;
        return 0;
    }

    lst = get_elements(ctrl->repo);

    convert_all_materials_to_string(lst);

    *list = lst;
    return 0;
}

t_list *filter4(Controller *ctrl, int quantity)
{
/* filters the elements in the repository by having the quantity greater than a given value,
 * sorts the elements by quantity, in ascending order
 * return: a list with the strings of all the materials in the repository */

    t_list *lst;

    lst = get_elements(ctrl->repo);
    ft_list_remove_if(&lst, &quantity, &smaller_quantity);
    lst = sort_list(lst, &greater_quantity2);

    convert_all_materials_to_string(lst);

    return lst;
}

t_list *filter5(Controller *ctrl, char *supplier)
{
/* filters the elements in the repository by having a given supplier,
 * sorts the elements by name, in ascending order
 * return: a list with the strings of all the materials in the repository*/
    t_list *lst;

    lst = get_elements(ctrl->repo);

    ft_list_remove_if(&lst, supplier, &is_equal_supplier);
    lst = sort_list(lst, &compare_names);

    convert_all_materials_to_string(lst);

    return lst;
}


t_list *filter6(Controller *ctrl, char *supplier)
{
/* filters the elements in the repository by having a given supplier,
 * sorts the elements by expiration date, in ascending order
 * return: a list with the strings of all the materials in the repository*/

    t_list *lst;

    lst = get_elements(ctrl->repo);

    ft_list_remove_if(&lst, supplier, &is_equal_supplier);
    lst = sort_list(lst, &compare_expiration_date2);

    convert_all_materials_to_string(lst);

    return lst;
}

int undo_list(Controller *ctrl)
{
/* undoes the previous operation
 * return: 0 - succesfull undo
 *         1 - no changes to be made */

    DynamicVector *elements;
    t_list *first;

    if (ctrl->undo_list)
    {

        elements = get_vector(ctrl->repo);
        first = ctrl->undo_list;

        ft_list_add_to_the_beginning(&ctrl->redo_list, elements);
        change_elements(ctrl->repo, ctrl->undo_list->data);
        ctrl->undo_list = ctrl->undo_list->next;

        first->next = NULL;
        ft_list_clear(&first);

        return 0;
    }
    return 1;
}


int redo_list(Controller *ctrl)
{
/* redoes the previous undo
 * return: 0 - succesfull redo
 *         1 - no changes to be made */

    DynamicVector *elements;
    t_list *first;

    if (ctrl->redo_list)
    {

        elements = get_vector(ctrl->repo);
        first = ctrl->redo_list;

        ft_list_add_to_the_beginning(&ctrl->undo_list, elements);
        change_elements(ctrl->repo, ctrl->redo_list->data);
        ctrl->redo_list = ctrl->redo_list->next;

        first->next = NULL;
        ft_list_clear(&first);

        return 0;
    }
    return 1;
}


int undo_stack(Controller *ctrl)
{
/* undoes the previous operation
 * return: 0 - succesfull undo
 *         1 - no changes to be made */

//    Operation *operation;
//
//    if (isEmpty(ctrl->undo_stack))
//        return 1;
//
//    operation = pop(ctrl->undo_stack);
//
//    if (strcmp(get_operation_type(operation), "add") == 0) {
//
//    } else if (strcmp(get_operation_type(operation), "remove") == 0) {
//
//    } else if (strcmp(get_operation_type(operation), "update") == 0) {
//
//    } else if (strcmp(get_operation_type(operation), "redo") == 0) {
//
//    }
//
//    destroy_operation(operation);
//    return 0;
    return 1;
}

int redo_stack(Controller *ctrl)
{
/* redoes the previous operation
 * return: 0 - succesfull redo
 *         1 - no changes to be made */

    return 1;
}