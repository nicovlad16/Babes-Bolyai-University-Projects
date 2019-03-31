//
// Created by nvlad on 01.05.2018.
//

#ifndef ASSIGNMENT8_9_CONSOLE_H
#define ASSIGNMENT8_9_CONSOLE_H

#include <utility>
#include "../service/ctrl.h"

class UI
{
public:
    explicit UI(Controller c) : ctrl(std::move(c)) {}

    void run();

    void initialize_repo();

    void choose_output_filetype();

private:
    Controller ctrl;

    void run_administrator_mode();

    static void print_menu();

    void add_dog_shelter();

    void show_all_dogs_shelter();

    static void print_user_mode_menu();

    static void print_view_mode_menu();

    static void print_admin_mode_menu();

    void run_user_mode();

    void remove_dog_shelter();

    void update_dog_shelter();

    void view_all_dogs();

    void view_dogs_by_age_and_breed();

    void see_adopted_dogs();

    int read_number();

    std::string read_string(const char txt[]);

    void show_dog_list();

    void save_doglist_to_file();

    void see_adopted_dogs_file();
};

#endif //ASSIGNMENT8_9_CONSOLE_H
