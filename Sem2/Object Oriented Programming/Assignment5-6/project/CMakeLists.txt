cmake_minimum_required(VERSION 3.10)
project(Assignment8_9)

set(CMAKE_CXX_STANDARD 17)

add_executable(Assignment8_9 main.cpp repo/dynamic_array.cpp repo/dynamic_array.h repo/repository.cpp repo/repository.h domain/dog.cpp domain/dog.h tests/tests.cpp tests/tests.h ui/ui.cpp ui/ui.h service/ctrl.h service/ctrl.cpp domain/doglist.cpp domain/doglist.h domain/DogValidator.cpp domain/DogValidator.h other/Comparator.cpp other/Comparator.h other/ComparatorAscendingByBreed.cpp other/ComparatorAscendingByBreed.h other/ComparatorAscendingByAge.cpp other/ComparatorAscendingByAge.h)