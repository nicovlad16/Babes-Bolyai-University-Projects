//
// Created by nvlad on 09.06.2018.
//

#include <cassert>
#include <cstring>
#include "Tests.h"
#include "HashTable.h"
#include "SparseMatrix.h"
#include "IteratorSparseMatrix.h"


void Tests::test_all()
{
    test_hash_table();
    test_sparse_matrix();
    test_iterator();
}

//
//int hFunc(int key, int m)
//{
//    if (key == 0)
//        return 0;
//    else
//        return key % m;
//}

void Tests::test_hash_table()
{

    HashTable<int> hashTable(10, &hashFunction);

//    tests for the insert and getElement functions

    try
    {
        hashTable.getElement(45645);
    }
    catch (const char *str)
    {
        assert(strcmp(str, "Inexisting key.\n") == 0);
    }

    int key = 1;
    int value = 6;
    hashTable.insert(key, value);
    assert(hashTable.getElement(key) == value);

    key = 6;
    value = 34;
    hashTable.insert(key, value);
    assert(hashTable.getElement(key) == value);

    key = 21;
    value = 13;
    hashTable.insert(key, value);
    assert(hashTable.getElement(key) == value);

    key = 11;
    value = 55;
    hashTable.insert(key, value);
    assert(hashTable.getElement(key) == value);

    key = 16;
    value = 34;
    hashTable.insert(key, value);
    assert(hashTable.getElement(key) == value);

    try
    {
        hashTable.insert(key, value);
    }
    catch (const char *str)
    {
        assert(strcmp(str, "Existing key.\n") == 0);
    }

//    tests for the update function

    key = 16;
    value = 1;
    hashTable.update(key, value);
    assert(hashTable.getElement(key) == value);

    key = 6;
    value = 115;
    hashTable.update(key, value);
    assert(hashTable.getElement(key) == value);

    key = 11;
    value = 7;
    hashTable.update(key, value);
    assert(hashTable.getElement(key) == value);

    key = 3818932;
    try
    {
        hashTable.update(key, value);
    }
    catch (const char *str)
    {
        assert(strcmp(str, "Inexisting key.\n") == 0);
    }

//    tests for the remove function

    key = 16;
    hashTable.remove(key);
    try
    {
        hashTable.getElement(key);
    }
    catch (const char *str)
    {
        assert(strcmp(str, "Inexisting key.\n") == 0);
    }

    key = 6;
    hashTable.remove(key);
    try
    {
        hashTable.getElement(key);
    }
    catch (const char *str)
    {
        assert(strcmp(str, "Inexisting key.\n") == 0);
    }

    key = 11;
    hashTable.remove(key);
    try
    {
        hashTable.getElement(key);
    }
    catch (const char *str)
    {
        assert(strcmp(str, "Inexisting key.\n") == 0);
    }

    key = 21;
    hashTable.remove(key);
    try
    {
        hashTable.getElement(key);
    }
    catch (const char *str)
    {
        assert(strcmp(str, "Inexisting key.\n") == 0);
    }

    try
    {
        hashTable.remove(key);
    }
    catch (const char *str)
    {
        assert(strcmp(str, "Inexisting key.\n") == 0);
    }

    key = 831839;
    try
    {
        hashTable.remove(key);
    }
    catch (const char *str)
    {
        assert(strcmp(str, "Inexisting key.\n") == 0);
    }
}


void Tests::test_sparse_matrix()
{
    int rows = 5;
    int columns = 6;
    SparseMatrix sparseMatrix(rows, columns);

    assert(sparseMatrix.numberOfLines() == rows);
    assert(sparseMatrix.numberOfColumns() == columns);

    try
    {
        rows = 0;
        columns = 0;
        SparseMatrix sparseMatrix1(rows, columns);
    }
    catch (const char *str)
    {
        assert(strcmp(str, "Invalid number of elements in the matrix.\n") == 0);
    }

//    tests for the element function

    assert(sparseMatrix.element(0, 0) == 0);
    assert(sparseMatrix.element(2, 3) == 0);
    assert(sparseMatrix.element(1, 5) == 0);
    assert(sparseMatrix.element(4, 5) == 0);

    try
    {
        sparseMatrix.element(-1, 5);
    }
    catch (const char *str)
    {
        assert(strcmp(str, "Invalid indeces of the element in the matrix.\n") == 0);
    }

    try
    {
        sparseMatrix.element(2, 6);
    }
    catch (const char *str)
    {
        assert(strcmp(str, "Invalid indeces of the element in the matrix.\n") == 0);
    }

    try
    {
        sparseMatrix.element(6, 4);
    }
    catch (const char *str)
    {
        assert(strcmp(str, "Invalid indeces of the element in the matrix.\n") == 0);
    }

    try
    {
        sparseMatrix.element(6, -1);
    }
    catch (const char *str)
    {
        assert(strcmp(str, "Invalid indeces of the element in the matrix.\n") == 0);
    }

//    tests for the modify function

    sparseMatrix.modify(3, 4, 0);
    sparseMatrix.modify(1, 1, 54);
    sparseMatrix.modify(1, 1, 488);
    sparseMatrix.modify(1, 4, 73);
    sparseMatrix.modify(1, 4, 0);

    try
    {
        sparseMatrix.modify(6, -1, 45);
    }
    catch (const char *str)
    {
        assert(strcmp(str, "Invalid indeces of the element in the matrix.\n") == 0);
    }
}


void Tests::test_iterator()
{
    int rows = 5;
    int columns = 6;
    SparseMatrix sparseMatrix(rows, columns);

    sparseMatrix.modify(1, 0, 31);
    sparseMatrix.modify(3, 0, 71);
    sparseMatrix.modify(0, 1, 23);
    sparseMatrix.modify(3, 2, 43);
    sparseMatrix.modify(1, 3, 13);
    sparseMatrix.modify(2, 3, 17);
    sparseMatrix.modify(3, 3, 53);
    sparseMatrix.modify(4, 3, 61);
    sparseMatrix.modify(4, 4, 79);

//    IteratorSparseMatrix iteratorSparseMatrix(sparseMatrix);
//    int array[10];
//    int count = 0;
//
//    while (iteratorSparseMatrix.valid())
//    {
//        int elem = iteratorSparseMatrix.getCurrent();
//        array[count] = elem;
//        count++;
//        iteratorSparseMatrix.next();
//    }
//
//    assert(count == 9);
//
//    int i = 0;
//    while (i < count)
//    {
//        printf("%d ", array[i]);
//        i++;
//    }
//
//    assert(array[0] == 23);
//    assert(array[1] == 31);
//    assert(array[2] == 13);
//    assert(array[3] == 17);
//    assert(array[4] == 71);
//    assert(array[5] == 43);
//    assert(array[6] == 53);
//    assert(array[7] == 61);
//    assert(array[8] == 79);
}