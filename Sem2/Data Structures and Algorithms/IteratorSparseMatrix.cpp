//
// Created by nvlad on 06.07.2018.
//

#include "IteratorSparseMatrix.h"


IteratorSparseMatrix::IteratorSparseMatrix(SparseMatrix &sparseMatrix) : sparseMatrix(sparseMatrix)
{
    // copy the array
    HashTable<int>::HashNode *array[sparseMatrix.hashTable.m];
    HashTable<int>::HashNode *entry = nullptr;
    HashTable<int>::HashNode *current = nullptr;
    int i = 0;
    while (i < sparseMatrix.hashTable.m)
    {
        entry = sparseMatrix.hashTable.htable[i];
        if (entry)
        {
            current = new HashTable<int>::HashNode(entry->key, entry->value);
            array[i] = current;
        } else
        { array[i] = nullptr; }

        while (entry != nullptr)
        {
            auto *newNode = new HashTable<int>::HashNode(entry->key, entry->value);
            current->next = newNode;
            current = current->next;
            entry = entry->next;
        }
        i++;
    }

    // merge lists
    sortedList = mergeLists(array, sparseMatrix.hashTable.m - 1);

    // initialize currentNode
    currentNode = sortedList;

}


HashTable<int>::HashNode *IteratorSparseMatrix::sortedMerge(HashTable<int>::HashNode *a, HashTable<int>::HashNode *b)
{
    HashTable<int>::HashNode *result = nullptr;

    if (a == nullptr)
        return b;
    else if (b == nullptr)
        return a;

    if (a->key <= b->key)
    {
        result = a;
        result->next = sortedMerge(a->next, b);
    } else
    {
        result = b;
        result->next = sortedMerge(a, b->next);
    }

    return result;
}


HashTable<int>::HashNode *IteratorSparseMatrix::mergeLists(HashTable<int>::HashNode **array, int last)
{
    while (last != 0)
    {
        int i = 0;
        int j = last;

        while (i < j)
        {
            array[i] = sortedMerge(array[i], array[j]);

            i++;
            j--;

            if (i >= j)
                last = j;
        }
    }
    return array[0];
}


int IteratorSparseMatrix::getCurrent()
{
    return currentNode->value;
}


void IteratorSparseMatrix::next()
{
    currentNode = currentNode->next;
}


bool IteratorSparseMatrix::valid()
{
    return currentNode != nullptr;
}


IteratorSparseMatrix::~IteratorSparseMatrix()
{
    HashTable<int>::HashNode *current = sortedList;
    HashTable<int>::HashNode *next = nullptr;

    while (current != nullptr)
    {
        next = current->next;
        free(current);
        current = next;
    }
}




