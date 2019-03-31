cmake_minimum_required(VERSION 3.9)
project(Assignment3_4 C)

set(CMAKE_C_STANDARD 99)

add_executable(Assignment3_4 main.c domain/material.c domain/material.h ui/ui.c ui/ui.h ctrl/controller.c ctrl/controller.h repo/repository.c repo/repository.h repo/dynamic_array.c repo/dynamic_array.h tests/tests.c tests/tests.h domain/dd.mm.yyyy.c domain/dd.mm.yyyy.h repo/list.c repo/list.h domain/operation_stack.c domain/operation_stack.h)