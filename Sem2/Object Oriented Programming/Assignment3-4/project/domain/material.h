//
// Created by nvlad on 11.03.2018.
//

#ifndef ASSIGNMENT3_4_MATERIAL_H
#define ASSIGNMENT3_4_MATERIAL_H


typedef struct
{
    char *name;
    char *supplier;
    int quantity;
    char *expiration_date;
} Material;

Material *create_material(char *name, char *supplier, int quantity, char *expiration_day);

void destroy_material(void *material);

char *get_name(Material *material);

char *get_supllier(Material *material);

int get_quantity(Material *material);

char *get_expiration_date(Material *material);

void set_name(Material *material, char *name);

void set_supplier(Material *material, char *supplier);

void set_quantity(Material *material, int quantity);

void set_expiration_date(Material *material, char *expiration_date);

int is_equal(void *x, void *y);

int compare_names(void *x, void *y);

void *copy_material(void *elem);

char *material_to_string(Material *material);

int compare_name(void *x, void *y);

int is_equal_name(void *x, void *y);

int compare_supplier(void *x, void *y);

int is_equal_supplier(void *x, void *y);


int compare_expiration_date(void *x, void *y);

int compare_expiration_date2(void *x, void *y);

int is_equal_expiration_date(void *x, void *y);

int greater_quantity(void *x, void *y);

int smaller_quantity(void *x, void *y);


int greater_quantity2(void *x, void *y);

int smaller_quantity2(void *x, void *y);

int is_equal_quantity(void *x, void *y);

#endif //ASSIGNMENT3_4_MATERIAL_H





