cmake_minimum_required(VERSION 3.10)
project(Assignment8_9)

set(CMAKE_CXX_STANDARD 17)

#SET(liblist boost_program_options)

add_executable(Assignment8_9 main.cpp domain/dog.cpp domain/dog.h domain/file_doglist.cpp domain/file_doglist.h domain/dog_validator.cpp domain/dog_validator.h repo/file_repository.cpp repo/file_repository.h service/ctrl.cpp service/ctrl.h tests/tests.cpp tests/tests.h ui/console.cpp ui/console.h utils/utils.cpp utils/utils.h domain/csv_doglist.cpp domain/csv_doglist.h domain/html_doglist.cpp domain/html_doglist.h)