//
// Created by nvlad on 12.03.2018.
//

#include <assert.h>
#include <malloc.h>
#include <string.h>
#include "../domain/material.h"
#include "../repo/dynamic_array.h"
#include "../repo/list.h"
#include "../repo/repository.h"
#include "../ctrl/controller.h"
#include "../domain/operation_stack.h"

void test_material()
{
    Material *m;

    m = create_material("faina", "firma1", 15, "12.34.46");

    assert (strcmp(get_name(m), "faina") == 0);
    assert (strcmp(get_supllier(m), "firma1") == 0);
    assert (strcmp(get_expiration_date(m), "12.34.46") == 0);
    assert(get_quantity(m) == 15);

    set_expiration_date(m, "12.21.32");
    assert(strcmp(get_expiration_date(m), "12.21.32") == 0);

    set_name(m, "m");
    assert (strcmp(get_name(m), "m") == 0);

    set_supplier(m, "dd");
    assert (strcmp(get_supllier(m), "dd") == 0);

    set_quantity(m, 21);
    assert(get_quantity(m) == 21);

    assert(is_equal(m, m) == 1);

    destroy_material(m);
}


void test_list()
{
    t_list *lst;
    t_list *head;

    int a = 5;
    int b = 7;
    int c = 13;

//    printf("%p", &a);

    lst = NULL;

    ft_list_add_to_the_beginning(&lst, &a);
    ft_list_add_to_the_beginning(&lst, &b);
    ft_list_add_to_the_beginning(&lst, &c);

    head = lst;

    assert(*(int *) lst->data == c);
    assert(ft_list_size(lst) == 3);

    lst = lst->next;
    assert(*(int *) lst->data == b);
    assert(ft_list_size(lst) == 2);

    lst = lst->next;
    assert((int *) lst->data == &a);
    assert(ft_list_size(lst) == 1);

    lst = lst->next;
    assert(lst == NULL);

    ft_list_add_to_the_end(&head, &a);

    assert((int *) head->next->next->next->data == &a);
    assert(ft_list_size(head) == 4);

    ft_list_clear(&head);
}

void test_dynamic_array()
{
    DynamicVector *v;
    DynamicVector *cpy;
    Material *m;

    m = create_material("faina", "firma1", 15, "12.34.46");
    v = create_dynamic_vector(1, &destroy_material, &copy_material);
    assert(get_length(v) == 0);

    if (v)
    {
        add(v, m);
        assert(get_length(v) == 1);

        m = create_material("faina", "firma1", 15, "12.34.46");
        add(v, m);
        assert(get_length(v) == 2);

        cpy = copy_vector(v);
        assert(cpy->length == v->length);

        destroy_dynamic_vector(cpy);

        delete(v, 0);
        assert(get_length(v) == 1);

        destroy_dynamic_vector(v);
        v = NULL;
        assert(get_length(v) == -1);
    }

}

void test_operations_stack()
{
    OperationsStack *stack;
    Operation *operation;
    Operation *operation1;
    Operation *operation2;
    Operation *operation3;

    stack = create_stack();

    Material *material1 = create_material("lapte", "ferma", 45, "23.03.2015");
    Material *material2 = create_material("branza", "supermarket", 20, "13.09.2017");

    operation1 = create_operation(material1, "add");
    operation2 = create_operation(material2, "add");
    operation3 = create_operation(material1, "remove");

    destroy_material(material1);
    destroy_material(material2);

    push(stack, operation1);
    push(stack, operation2);
    push(stack, operation3);

    destroy_operation(operation1);
    destroy_operation(operation2);
    destroy_operation(operation3);

    assert(isFull(stack) == 0);
    assert(isEmpty(stack) == 0);

    operation = pop(stack);
    assert(strcmp(operation->operation_type, "remove") == 0);
    destroy_operation(operation);

    operation = pop(stack);
    assert(strcmp(operation->operation_type, "add") == 0);
    destroy_operation(operation);

    operation = pop(stack);
    assert(strcmp(operation->operation_type, "add") == 0);
    destroy_operation(operation);

    assert(isEmpty(stack) == 1);

    destroy_stack(stack);
}

void test_repository()
{
    Material *m;
    Material *upd;
    t_list *lst;
    Repository *repo;
    DynamicVector *elems;

    repo = create_repository(&destroy_material, &is_equal, &copy_material);
    if (repo)
    {
        assert(size(repo) == 0);
        m = create_material("faina", "firma1", 15, "12.34.46");
        assert(add_repo(repo, m) == 1);
        assert(size(repo) == 1);

        assert((Material *) find_element_repo(repo, m) == m);

        m = create_material("faina", "firma1", 10, "12.34.46");
        assert(add_repo(repo, m) == 0);
        destroy_material(m);
        assert(size(repo) == 1);

        m = create_material("lapte", "firma2", 20, "12.34.46");
        assert(add_repo(repo, m) == 1);
        assert(size(repo) == 2);

        assert(delete_element_repo(repo, m) == 1);
        assert(size(repo) == 1);

        m = create_material("lapte", "firma3", 20, "12.34.46");
        assert(add_repo(repo, m) == 1);
        assert(size(repo) == 2);

        upd = create_material("orez", "china", 25, "12.02.1999");
        assert(update_repo(repo, m, upd) == 1);
        assert(size(repo) == 2);

        m = create_material("orez", "ch", 25, "12.02.1999");
        assert(update_repo(repo, m, upd) == 0);
        assert(size(repo) == 2);
        destroy_material(m);

        lst = get_elements(repo);
        assert(ft_list_size(lst) == size(repo));

        ft_list_clear(&lst);

        elems = get_vector(repo);
        assert(get_length(elems) == size(repo));
        destroy_dynamic_vector(elems);

        destroy_repository(repo);
        repo = NULL;
        assert(size(repo) == -1);
    }
}

void test_ctrl()
{
    Controller *ctrl;
    Repository *repo;
    OperationsStack *undo_stack;
    OperationsStack *redo_stack;
    t_list *undo_list;
    t_list *redo_list;

    repo = create_repository(&destroy_material, &is_equal, &copy_material);

    if (repo)
    {

        undo_stack = create_stack();
        redo_stack = create_stack();

        undo_list = NULL;
        redo_list = NULL;

        ctrl = create_controller(repo, undo_stack, redo_stack, undo_list, redo_list);

        if (ctrl)
        {

            assert(size(ctrl->repo) == 0);

            assert(add_material(ctrl, "ulei", "firma1", 46, 12, 10, 1999) == 0);
            assert(size(ctrl->repo) == 1);

            assert(add_material(ctrl, "sare", "firma1", 20, 12, 10, 1999) == 0);
            assert(size(ctrl->repo) == 2);

            assert(add_material(ctrl, "sare", "firma1", 30, 12, 10, 1999) == 0);
            assert(size(ctrl->repo) == 2);

            assert(add_material(ctrl, "sare", "firma1", 12, 12, 10, 1999) == 0);
            assert(size(ctrl->repo) == 2);

            assert(update_material(ctrl, "sare", "zahar", "firma1", "blabla", 30, 250, 12, 15, 10, 10, 1999, 2005) ==
                   0);
            assert(size(ctrl->repo) == 2);

            assert(update_material(ctrl, "sare", "zahar", "firma1", "blabla", 30, 250, 12, 15, 10, 10, 1999, 2005) ==
                   2);
            assert(size(ctrl->repo) == 2);

            assert(update_material(ctrl, "sare", "zahar", "firma1", "blabla", 30, 250, 12, 15, 10, 10, 1999,
                                   205555505) == 1);
            assert(size(ctrl->repo) == 2);

            assert(add_material(ctrl, "faina", "firma", 12, 1, 1, 2000) == 0);
            assert(size(ctrl->repo) == 3);

            assert(add_material(ctrl, "ulei", "firma2", 46, 1000002, 45, 1999) == 1);
            assert(size(ctrl->repo) == 3);

            assert(remove_material(ctrl, "ulei", "firma1", 12, 10, 1999) == 0);
            assert(size(ctrl->repo) == 2);

            assert(remove_material(ctrl, "ulei", "firma1", 12, 10, 1999) == 2);
            assert(size(ctrl->repo) == 2);

            assert(remove_material(ctrl, "ulei", "firma2", 12, 45, 1999999) == 1);
            assert(size(ctrl->repo) == 2);

            destroy_controller(ctrl);
        }
    }
}

void test_all()
{
    test_material();
    test_list();
    test_dynamic_array();
    test_operations_stack();
    test_repository();
    test_ctrl();
}