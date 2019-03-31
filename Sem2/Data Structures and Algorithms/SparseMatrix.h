//
// Created by nvlad on 24.05.2018.
//

#ifndef PROJECT_DSA_SPARSEMATRIX_H
#define PROJECT_DSA_SPARSEMATRIX_H


#include <vector>
#include <cstddef>
#include "HashTable.h"


static int hashFunction(int key, int m)
{
    if (key == 0)
        return 0;
    else
        return key % m;
}


class SparseMatrix
{
protected:
    int numberLines;
    int numberColumns;
    HashTable<int> hashTable;

    int computeKey(int i, int j);

    static int computeHashTableSize(int n);

public:

    SparseMatrix(int numberLines, int numberColumns);

    virtual ~SparseMatrix() = default;

    int numberOfLines();

    int numberOfColumns();

    const int element(int i, int j);

    void modify(int i, int j, int new_value);


    friend class IteratorSparseMatrix;

};


class SparseMatrixException : public std::exception
{
private:
    std::string message;
public:
    explicit SparseMatrixException(const std::string &_message);

    const char *what() const noexcept override;
};


#endif //PROJECT_DSA_SPARSEMATRIX_H
