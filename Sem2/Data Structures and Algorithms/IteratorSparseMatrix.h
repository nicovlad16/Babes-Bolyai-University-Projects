//
// Created by nvlad on 06.07.2018.
//

#ifndef PROJECT_DSA_ITERATORSPARSEMATRIX_H
#define PROJECT_DSA_ITERATORSPARSEMATRIX_H


#include "SparseMatrix.h"


class IteratorSparseMatrix
{
private:
    SparseMatrix &sparseMatrix;
    HashTable<int>::HashNode *sortedList;
    HashTable<int>::HashNode *currentNode;

    HashTable<int>::HashNode *sortedMerge(HashTable<int>::HashNode *a, HashTable<int>::HashNode *b);

    HashTable<int>::HashNode *mergeLists(HashTable<int>::HashNode *array[], int last);


public:
    explicit IteratorSparseMatrix(SparseMatrix &sparseMatrix);

    int getCurrent();

    void next();

    bool valid();

    virtual ~IteratorSparseMatrix();
};


#endif //PROJECT_DSA_ITERATORSPARSEMATRIX_H
