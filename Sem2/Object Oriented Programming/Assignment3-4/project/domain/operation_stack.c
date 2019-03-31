//
// Created by nvlad on 25.03.2018.
//

#include <malloc.h>
#include <string.h>
#include "operation_stack.h"

Operation *create_operation(Material *material, char *operation_type)
{
/* creates an operation
 * return: pointer to the created operation */

    Operation *operation;

    operation = (Operation *) malloc(sizeof(Operation));
    operation->material = copy_material(material);
    if (operation_type != NULL)
    {
        operation->operation_type = (char *) malloc(sizeof(char) * (strlen(operation_type) + 1));
        strcpy(operation->operation_type, operation_type);
    } else
        operation->operation_type = NULL;
    return operation;
}

void destroy_operation(Operation *operation)
{
/* destoys an operation, freeing the memory */
    if (operation == NULL)
        return;

    destroy_material(operation->material);
    free(operation->operation_type);
    free(operation);
}

Operation *copy_operation(Operation *operation)
{
/* copies an operation
 * return: pointer to the copied operation */

    Operation *new_operation;

    if (operation == NULL)
        return NULL;

    new_operation = create_operation(operation->material, operation->operation_type);
    return new_operation;
}

char *get_operation_type(Operation *operation)
{
/* return: the type of the operation */
    return operation->operation_type;
}

Material *get_material(Operation *operation)
{
/* return: the material of the operation */
    return operation->material;
}

// ---------------------------------------------------------------

OperationsStack *create_stack()
{
/* creates an operation stack
 * return: pointer to the created stack */
    OperationsStack *stack;

    stack = (OperationsStack *) malloc(sizeof(OperationsStack));
    stack->length = 0;

    return stack;
}

void destroy_stack(OperationsStack *stack)
{
/* destroys the operation stack, freeing the memory */
    int i;

    if (stack == NULL)
        return;

    i = 0;
    while (i < stack->length)
    {
        destroy_operation(stack->operations[i]);
        i++;
    }
    free(stack);
}

void push(OperationsStack *stack, Operation *operation)
{
/* adds an operion on the stack */
    if (isFull(stack))
        return;

    stack->operations[stack->length] = copy_operation(operation);
    stack->length += 1;
}

Operation *pop(OperationsStack *stack)
{
/* removes an operion from the stack
 * return: the removed operation
 *         NULL - if the stack has no operations*/

    if (isEmpty(stack))
        return NULL;

    stack->length -= 1;
    return stack->operations[stack->length];
}

int isEmpty(OperationsStack *stack)
{
    return (stack->length == 0);
}

int isFull(OperationsStack *stack)
{
    return (stack->length == 777);
}
