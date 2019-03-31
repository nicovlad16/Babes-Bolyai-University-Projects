//
// Created by nvlad on 25.03.2018.
//

#ifndef ASSIGNMENT3_4_OPERATION_STACK_H
#define ASSIGNMENT3_4_OPERATION_STACK_H

#include "material.h"

typedef struct
{
    Material *material;
    char *operation_type;
} Operation;

Operation *create_operation(Material *material, char *operation_type);

void destroy_operation(Operation *operation);

Operation *copy_operation(Operation *operation);

char *get_operation_type(Operation *operation);

Material *get_material(Operation *operation);

// ---------------------------------------------------------------

typedef struct
{
    Operation *operations[777];
    int length;
} OperationsStack;

OperationsStack *create_stack();

void destroy_stack(OperationsStack *stack);

void push(OperationsStack *stack, Operation *operation);

Operation *pop(OperationsStack *stack);

int isEmpty(OperationsStack *stack);

int isFull(OperationsStack *stack);


#endif //ASSIGNMENT3_4_OPERATION_STACK_H
