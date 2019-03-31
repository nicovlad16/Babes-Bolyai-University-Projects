//
// Created by nvlad on 11.03.2018.
//

#include <printf.h>
#include <stdio.h>
#include <string.h>
#include <malloc.h>
#include "ui.h"


UI *create_ui(Controller *ctrl)
{
    UI *ui;
    ui = (UI *) malloc(sizeof(ui));
    if (ui == NULL)
        return NULL;
    ui->ctrl = ctrl;
    return ui;
}

void destroy_ui(UI *ui)
{
    destroy_controller(ui->ctrl);
    ui->ctrl = NULL;
    free(ui);
}


void ui_add(UI *ui, char *params)
{
    char name[50];
    char supplier[50];
    int quantity = 0;
    int day = 0;
    int month = 0;
    int year = 0;
    char extra[50];
    int add_return_value = -1;

    name[0] = '\0';
    supplier[0] = '\0';
    extra[0] = '\0';

    sscanf(params, " %s %s %d %d %d %d %s", name, supplier, &quantity, &day, &month, &year, extra);

    if (name[0] == '\0' || supplier[0] == '\0' || quantity == 0 || day == 0 || month == 0 || year == 0 ||
        extra[0] != '\0')
    {
        printf("Invalid arguments.\n");
        return;
    }
    add_return_value = add_material(ui->ctrl, name, supplier, quantity, day, month, year);
    if (add_return_value == 0)
        printf("Successfully added.\n");
    else if (add_return_value == 1)
        printf("Invalid data types.\n");
    else
        printf("Some error occured during add.\n");

}

void ui_remove(UI *ui, char *params)
{
    char name[50];
    char supplier[50];
    int day = 0;
    int month = 0;
    int year = 0;
    char extra[50];
    int remove_return_value = -1;

    name[0] = '\0';
    supplier[0] = '\0';
    extra[0] = '\0';

    sscanf(params, " %s %s %d %d %d %s", name, supplier, &day, &month, &year, extra);
    if (name[0] == '\0' || supplier[0] == '\0' || day == 0 || month == 0 || year == 0 || extra[0] != '\0')
    {
        printf("Invalid arguments.\n");
        return;
    }

    remove_return_value = remove_material(ui->ctrl, name, supplier, day, month, year);
    if (remove_return_value == 0)
        printf("Successfully removed.\n");
    else if (remove_return_value == 1)
        printf("Invalid data types.\n");
    else if (remove_return_value == 2)
        printf("Inexisting element.\n");
    else
        printf("Some error occured during remove.\n");

}

void ui_update(UI *ui, char *params)
{
    char old_name[50];
    char new_name[50];
    char old_supplier[50];
    char new_supplier[50];
    int old_quantity = 0;
    int new_quantity = 0;
    int old_day = 0;
    int new_day = 0;
    int old_month = 0;
    int new_month = 0;
    int old_year = 0;
    int new_year = 0;
    char extra[50];
    int update_return_value = -1;

    old_name[0] = '\0';
    new_name[0] = '\0';
    old_supplier[0] = '\0';
    new_supplier[0] = '\0';
    extra[0] = '\0';

    sscanf(params, " %s %s %d %d %d %d %s %s %d %d %d %d %s", old_name, old_supplier, &old_quantity, &old_day,
           &old_month, &old_year, new_name, new_supplier, &new_quantity, &new_day, &new_month, &new_year, extra);
    if (old_name[0] == '\0' || old_supplier[0] == '\0' || old_quantity == 0 || old_day == 0 || old_month == 0 ||
        old_year == 0 || new_name[0] == '\0' || new_supplier[0] == '\0' || new_quantity == 0 || new_day == 0 ||
        new_month == 0 || new_year == 0 || extra[0] != '\0')
    {
        printf("Invalid arguments.\n");
        return;
    }
    update_return_value = update_material(ui->ctrl, old_name, new_name, old_supplier, new_supplier, old_quantity,
                                          new_quantity, old_day, new_day, old_month, new_month, old_year, new_year);
    if (update_return_value == 0)
        printf("Successfully updated.\n");
    else if (update_return_value == 1)
        printf("Invalid data types.\n");
    else if (update_return_value == 2)
        printf("Inexisting element.\n");
    else
        printf("Some error ocurred during update.\n");
}

void print_list(void *elem)
{
    char *str;
    str = (char *) elem;
    printf("%s\n", str);
    free(str);
}

void ui_list_all(UI *ui)
{
    t_list *list;
    t_list *beginning;

    list = get_all(ui->ctrl);
    beginning = list;
    if (list)
    {
        ft_list_foreach(list, &print_list);
        ft_list_clear(&beginning);
    } else
        printf("There are no materials in the bakery.\n");
}

void ui_filter_list1(UI *ui, char *params)
{
    t_list *list;
    t_list *beginning;
    char supplier[50];
    int quantity = 0;
    char extra[50];

    supplier[0] = '\0';
    extra[0] = '\0';
    sscanf(params, " %s %d %s", supplier, &quantity, extra);
    if (supplier[0] == '\0' || quantity <= 0 || extra[0] != '\0')
    {
        printf("Invalid arguments.\n");
        return;
    }
    list = filter1(ui->ctrl, supplier, quantity);
    beginning = list;
    if (list)
    {
        ft_list_foreach(list, &print_list);
        ft_list_clear(&beginning);
    } else
        printf("There are no materials in the bakery.\n");
}

void ui_filter_list3(UI *ui, char *params)
{
    t_list *list;
    t_list *beginning;
    char supplier[50];
    int quantity = 0;
    char extra[50];

    supplier[0] = '\0';
    extra[0] = '\0';
    sscanf(params, " %s %d %s", supplier, &quantity, extra);
    if (supplier[0] == '\0' || quantity <= 0 || extra[0] != '\0')
    {
        printf("Invalid arguments.\n");
        return;
    }
    list = filter3(ui->ctrl, supplier, quantity);
    beginning = list;
    if (list)
    {
        ft_list_foreach(list, &print_list);
        ft_list_clear(&beginning);
    } else
        printf("There are no materials in the bakery.\n");
}


void ui_filter_list2(UI *ui, char *params)
{
    t_list *list;
    t_list *beginning;
    char expiration_date[50];
    char extra[50];
    int filter2_return_value = -1;

    expiration_date[0] = '\0';
    extra[0] = '\0';
    sscanf(params, " %s %s", expiration_date, extra);
    if (extra[0] != '\0')
    {
        printf("Invalid arguments.\n");
        return;
    }
    filter2_return_value = filter2(ui->ctrl, &list, expiration_date);
    if (filter2_return_value == 0)
    {
        beginning = list;
        if (list)
        {
            ft_list_foreach(list, &print_list);
            ft_list_clear(&beginning);
        } else
            printf("There are no materials in the bakery.\n");
    } else if (filter2_return_value == 1)
        printf("Invalid date format.\n");
    else
        printf("Some error ocurred during update.\n");

}

void ui_filter_list4(UI *ui, char *params)
{
    t_list *list;
    t_list *beginning;
    int quantity = 0;
    char extra[50];

    extra[0] = '\0';
    sscanf(params, " %d %s", &quantity, extra);
    if (quantity <= 0 || extra[0] != '\0')
    {
        printf("Invalid arguments.\n");
        return;
    }
    list = filter4(ui->ctrl, quantity);
    beginning = list;
    if (list)
    {
        ft_list_foreach(list, &print_list);
        ft_list_clear(&beginning);
    } else
        printf("There are no materials in the bakery.\n");
}


void ui_filter_list5(UI *ui, char *params)
{
    t_list *list;
    t_list *beginning;
    char supplier[50];
    char extra[50];

    supplier[0] = '\0';
    extra[0] = '\0';
    sscanf(params, " %s %s", supplier, extra);
    if (supplier[0] == '\0' || extra[0] != '\0')
    {
        printf("Invalid arguments.\n");
        return;
    }
    list = filter5(ui->ctrl, supplier);
    beginning = list;
    if (list)
    {
        ft_list_foreach(list, &print_list);
        ft_list_clear(&beginning);
    } else
        printf("There are no materials in the bakery.\n");
}

void ui_filter_list6(UI *ui, char *params)
{
    t_list *list;
    t_list *beginning;
    char supplier[50];
    char extra[50];

    supplier[0] = '\0';
    extra[0] = '\0';
    sscanf(params, " %s %s", supplier, extra);
    if (supplier[0] == '\0' || extra[0] != '\0')
    {
        printf("Invalid arguments.\n");
        return;
    }
    list = filter6(ui->ctrl, supplier);
    beginning = list;
    if (list)
    {
        ft_list_foreach(list, &print_list);
        ft_list_clear(&beginning);
    } else
        printf("There are no materials in the bakery.\n");
}

void print_commands()
{
    printf("•list\n\n");
    printf("•add <name> <supplier> <quantity> <expiration_date: \"<day> <month> <year>\">\n\n");
    printf("•remove <name> <supplier> <expiration_date: \"<day> <month> <year>\">\n\n");
    printf("•update <old_name> <old_supplier> <old_quantity> <old_expiration_date: \"<day> <month> <year>\">\n      <new_name> <new_supplier> <new_quantity> <new_expiration_date: \"<day> <month> <year>\">\n\n");
    printf("•filter1 <supplier> <quantity> (ascending, smaller than a value)\n\n");
    printf("•filter2 [<expiration_date: \"dd.mm.yyyy\">]\n\n");
    printf("•filter3 <supplier> <quantity> (descending, smaller than a value)\n\n");
    printf("•filter4 <quantity> (all suppliers, greater than a value) \n\n");
    printf("•filter5 <supplier> (ascending, by name)\n\n");
    printf("•filter6 <supplier> (ascending, by expiration_date)\n\n");
    printf("•undo (list of lists)\n\n");
    printf("•redo (list of lists)\n\n");
    printf("•undo2 (operations stack)\n\n");
    printf("•redo2 (operations stack)\n\n");
    printf("•exit\n\n");
}

void ui_undo(UI *ui)
{
    if (undo_list(ui->ctrl) == 0)
        printf("Successfull undo.\n");
    else
        printf("Undo cannot be done.\n");
}

void ui_redo(UI *ui)
{
    if (redo_list(ui->ctrl) == 0)
        printf("Successfull redo.\n");
    else
        printf("Redo cannot be done.\n");
}

void ui_undo2(UI *ui)
{
    if (undo_stack(ui->ctrl) == 0)
        printf("Successfull undo.\n");
    else
        printf("Undo cannot be done.\n");
}

void ui_redo2(UI *ui)
{
    if (redo_stack(ui->ctrl) == 0)
        printf("Successfull redo.\n");
    else
        printf("Redo cannot be done.\n");
}

void start(UI *ui)
{
    size_t n;
    ssize_t len;
    char *line;
    char *cmd;
    char *tok;
    const char delim[2] = " ";

    n = 0;
    cmd = NULL;
    printf("\n        Welcome to the Bakery! ^_^\n\n\n");
    print_commands();
    while (1)
    {
        printf(">> ");
        len = getline(&cmd, &n, stdin);
        if (cmd)
            cmd[(int) (len - 1)] = '\0';
        line = (char *) malloc(sizeof(char) * (strlen(cmd) + 1));
        if (line == NULL)
            return;
        strcpy(line, cmd);
        tok = strtok(cmd, delim);
        if (tok == NULL)
            printf("Invalid command.\n");
        else if (strcmp(tok, "exit") == 0 && strtok(NULL, delim) == NULL)
        {
            free(cmd);
            free(line);
            return;
        } else if (strcmp(tok, "add") == 0)
            ui_add(ui, line + strlen("add"));
        else if (strcmp(tok, "remove") == 0)
            ui_remove(ui, line + strlen("remove"));
        else if (strcmp(tok, "update") == 0)
            ui_update(ui, line + strlen("update"));
        else if (strcmp(tok, "list") == 0 && strtok(NULL, delim) == NULL)
            ui_list_all(ui);
        else if (strcmp(tok, "filter1") == 0)
            ui_filter_list1(ui, line + strlen("filter1"));
        else if (strcmp(tok, "filter2") == 0)
            ui_filter_list2(ui, line + strlen("filter2"));
        else if (strcmp(tok, "filter3") == 0)
            ui_filter_list3(ui, line + strlen("filter3"));
        else if (strcmp(tok, "filter4") == 0)
            ui_filter_list4(ui, line + strlen("filter4"));
        else if (strcmp(tok, "filter5") == 0)
            ui_filter_list5(ui, line + strlen("filter5"));
        else if (strcmp(tok, "filter6") == 0)
            ui_filter_list6(ui, line + strlen("filter6"));
        else if (strcmp(tok, "undo") == 0 && strtok(NULL, delim) == NULL)
            ui_undo(ui);
        else if (strcmp(tok, "redo") == 0 && strtok(NULL, delim) == NULL)
            ui_redo(ui);
        else if (strcmp(tok, "undo2") == 0 && strtok(NULL, delim) == NULL)
            ui_undo2(ui);
        else if (strcmp(tok, "redo2") == 0 && strtok(NULL, delim) == NULL)
            ui_redo2(ui);
        else
            printf("Invalid command.\n");
        free(line);
    }
}


void initialise_repository(UI *ui)
{
    add_material(ui->ctrl, "ulei", "panemar", 50, 15, 1, 2019);
    add_material(ui->ctrl, "făină", "simpa", 100, 2, 12, 2022);
    add_material(ui->ctrl, "ciocolată", "milka", 10, 13, 7, 2019);
    add_material(ui->ctrl, "ulei", "panemar", 7, 14, 2, 2018);
    add_material(ui->ctrl, "ulei", "panemar", 13, 15, 1, 2017);
    add_material(ui->ctrl, "ulei", "simpa", 43, 2, 1, 2019);
    add_material(ui->ctrl, "făină", "panemar", 11, 1, 1, 2016);
    add_material(ui->ctrl, "zahăr", "simpa", 10, 3, 4, 2013);
    add_material(ui->ctrl, "zahăr", "simpa", 23, 5, 7, 2020);
    add_material(ui->ctrl, "cacao", "simpa", 42, 17, 3, 2021);
}