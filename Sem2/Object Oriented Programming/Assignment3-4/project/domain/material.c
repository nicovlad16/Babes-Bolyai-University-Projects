//
// Created by nvlad on 11.03.2018.
//

#include <string.h>
#include <malloc.h>
#include "material.h"
#include "dd.mm.yyyy.h"

Material *create_material(char *name, char *supplier, int quantity, char *expiration_date)
{
/* create a new material with given name, supplier, quantity and expiration date
 * return: pointer to the material*/
    Material *material;

    material = (Material *) malloc(sizeof(Material));

    material->name = (char *) malloc(sizeof(char) * (strlen(name) + 1));
    strcpy(material->name, name);

    material->supplier = (char *) malloc(sizeof(char) * (strlen(supplier) + 1));
    strcpy(material->supplier, supplier);

    material->quantity = quantity;

    material->expiration_date = (char *) malloc(sizeof(char) * (strlen(expiration_date) + 1));
    strcpy(material->expiration_date, expiration_date);

    return (material);
}

void destroy_material(void *material)
{
/* destroys a material, freeing the memory */

    Material *m;
    m = (Material *) material;
    if (m == NULL)
        return;

    free(m->name);
    free(m->supplier);
    free(m->expiration_date);

    m->name = NULL;
    m->supplier = NULL;
    m->expiration_date = NULL;

    free(material);
}


char *get_name(Material *material)
{
/* return: the name of the material */
    return material->name;
}

char *get_supllier(Material *material)
{
/* return: the supplier of the material */
    return material->supplier;
}

int get_quantity(Material *material)
{
/* return: the quantity of the material */
    return material->quantity;
}

char *get_expiration_date(Material *material)
{
/* return: the expiration date of the material */
    return material->expiration_date;
}

void set_name(Material *material, char *name)
{
/* changes the name of the material with a new one */
    free(material->name);
    material->name = (char *) malloc(sizeof(char) * (strlen(name) + 1));
    strcpy(material->name, name);
}

void set_supplier(Material *material, char *supplier)
{
/* changes the supplier of the material with a new one */
    free(material->supplier);
    material->supplier = (char *) malloc(sizeof(char) * (strlen(supplier) + 1));
    strcpy(material->supplier, supplier);
}

void set_quantity(Material *material, int quantity)
{
/* changes the quantity of the material with a new one */
    material->quantity = quantity;
}

void set_expiration_date(Material *material, char *expiration_date)
{
/* changes the expiration date of the material with a new one */
    free(material->expiration_date);
    material->expiration_date = (char *) malloc(sizeof(char) * (strlen(expiration_date) + 1));
    strcpy(material->expiration_date, expiration_date);
}

int is_equal(void *x, void *y)
{
/* return: 1 - if two materials have the same name, supplier, expiration date
 *         0 - otherwise*/

    Material *m1;
    Material *m2;

    m1 = (Material *) x;
    m2 = (Material *) y;
    if (strcmp(m1->name, m2->name) == 0 && strcmp(m1->supplier, m2->supplier) == 0 &&
        strcmp(m1->expiration_date, m2->expiration_date) == 0)
        return 1;
    return 0;
}


int compare_name(void *x, void *y)
{
    Material *m1;
    char *str;

    m1 = (Material *) x;
    str = (char *) y;
    return (strcmp(m1->name, str) >= 0);

}

int compare_names(void *x, void *y)
{
    Material *m1;
    Material *m2;

    m1 = (Material *) x;
    m2 = (Material *) y;
    return (strcmp(m1->name, m2->name) <= 0);

}

int is_equal_name(void *x, void *y)
{
    Material *m1;
    char *str;

    m1 = (Material *) x;
    str = (char *) y;
    return (strcmp(m1->name, str) == 0);

}

int compare_supplier(void *x, void *y)
{
    Material *material;
    char *str;

    material = (Material *) x;
    str = (char *) y;
    return (strcmp(material->supplier, str) >= 0);

}

int is_equal_supplier(void *x, void *y)
{
    Material *m1;
    char *str;

    m1 = (Material *) x;
    str = (char *) y;
    return (strcmp(m1->supplier, str) == 0);

}


int compare_expiration_date(void *x, void *y)
{
    Material *material;
    char *str;
    int day1;
    int month1;
    int year1;
    int day2;
    int month2;
    int year2;

    material = (Material *) x;
    str = (char *) y;

    sscanf(material->expiration_date, "%d.%d.%d", &day1, &month1, &year1);
    sscanf(str, "%d.%d.%d", &day2, &month2, &year2);

    return (compare_date(day1, month1, year1, day2, month2, year2) >= 0);

}


int compare_expiration_date2(void *x, void *y)
{
    Material *material1;
    Material *material2;
    int day1;
    int day2;
    int month1;
    int month2;
    int year1;
    int year2;


    material1 = (Material *) x;
    material2 = (Material *) y;

    sscanf(material1->expiration_date, "%d.%d.%d", &day1, &month1, &year1);
    sscanf(material2->expiration_date, "%d.%d.%d", &day2, &month2, &year2);

    return (compare_date(day1, month1, year1, day2, month2, year2) >= 0);

}

int is_equal_expiration_date(void *x, void *y)
{
    Material *material;
    char *str;

    material = (Material *) x;
    str = (char *) y;
    return (strcmp(material->expiration_date, str) == 0);
}


int greater_quantity(void *x, void *y)
{
    Material *material;
    int *no;

    material = (Material *) x;
    no = (int *) y;
    return (material->quantity <= *no);

}

int smaller_quantity(void *x, void *y)
{
    Material *material;
    int *no;

    material = (Material *) x;
    no = (int *) y;
    return (material->quantity >= *no);

}

int greater_quantity2(void *x, void *y)
{
    Material *material1;
    Material *material2;

    material1 = (Material *) x;
    material2 = (Material *) y;
    return (material1->quantity <= material2->quantity);
}

int smaller_quantity2(void *x, void *y)
{
    Material *material1;
    Material *material2;

    material1 = (Material *) x;
    material2 = (Material *) y;
    return (material1->quantity >= material2->quantity);
}

int is_equal_quantity(void *x, void *y)
{
    Material *material;
    int *no;

    material = (Material *) x;
    no = (int *) y;
    return (material->quantity == *no);

}


void *copy_material(void *elem)
{
/* return: pointer to the new material, having the same attributes as the existing one */

    Material *material;
    Material *new;

    material = (Material *) elem;
    new = create_material(material->name, material->supplier, material->quantity, material->expiration_date);

    return (void *) new;
}

char *material_to_string(Material *material)
{
/* makes a string of an material, in order to be printed
 * return: the string */

    char *str;
    char *name;
    char *supplier;
    int quantity;
    char *expiration_date;

    name = material->name;
    supplier = material->supplier;
    quantity = material->quantity;
    expiration_date = material->expiration_date;

    str = (char *) malloc(
            sizeof(char) * (strlen(name) + strlen(supplier) + strlen(expiration_date) + 70) + sizeof(int));
    sprintf(str, "The material %s, from the supplier %s, in a quantity of %d, expires in %s.", name,
            supplier, quantity, expiration_date);

    return str;
}

