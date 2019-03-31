//
// Created by nvlad on 18.04.2018.
//

#ifndef ASSIGNMENT8_9_UI_H
#define ASSIGNMENT8_9_UI_H

#include <utility>
#include "../service/ctrl.h"

class UI
{
public:
    explicit UI(Controller c) : ctrl(std::move(c)) {}


    void run();

    void initialize_repo();

private:
    Controller ctrl;

    void run_administrator_mode();

    static void print_menu();

    void add_dog_shelter();

    void show_all_dogs_shelter();

    void print_user_mode_menu();

    void print_view_mode_menu();

    void print_admin_mode_menu();

    void run_user_mode();

    void remove_dog_shelter();

    void update_dog_shelter();

    void view_all_dogs();

    void view_dogs_by_age_and_breed();

    void see_adopted_dogs();

    int read_number();

    std::string read_string(const char txt[]);

    void show_dog_list();
};

#endif //ASSIGNMENT8_9_UI_H
