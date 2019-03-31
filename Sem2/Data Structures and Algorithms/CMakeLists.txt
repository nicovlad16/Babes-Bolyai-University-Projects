cmake_minimum_required(VERSION 3.10)
project(Project_DSA)

set(CMAKE_CXX_STANDARD 11)

add_executable(Project_DSA main.cpp SparseMatrix.cpp SparseMatrix.h HashTable.cpp HashTable.h Tests.cpp Tests.h IteratorSparseMatrix.cpp IteratorSparseMatrix.h)