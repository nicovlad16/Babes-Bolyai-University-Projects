#include <iostream>
#include "tests/tests.h"
#include "repo/repository.h"
#include "service/ctrl.h"
#include "ui/ui.h"


int main()
{
    Tests::test_all();

    Repository repo;
    Controller ctrl(repo);
    UI ui(ctrl);

    ui.initialize_repo();
    ui.run();
}