//
// Created by nvlad on 11.03.2018.
//

#ifndef ASSIGNMENT3_4_UI_H
#define ASSIGNMENT3_4_UI_H

#include "../ctrl/controller.h"

typedef struct
{
    Controller *ctrl;
} UI;

UI *create_ui(Controller *ctrl);

void destroy_ui(UI *ui);

void start(UI *ui);

void initialise_repository(UI *ui);

#endif //ASSIGNMENT3_4_UI_H


