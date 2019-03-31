#include <wchar.h>
#include <malloc.h>
#include "ui/ui.h"
#include "tests/tests.h"
#include "domain/material.h"

int main()
{
    test_all();

    Repository *repo;

    Controller *ctrl;
    OperationsStack *undo_stack;
    OperationsStack *redo_stack;
    t_list *undo_list;
    t_list *redo_list;

    UI *ui;

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

            ui = create_ui(ctrl);

            if (ui)
            {

                initialise_repository(ui);

                start(ui);

                destroy_ui(ui);
            }
        }
    }
    return 0;
}

