//
// Created by nvlad on 24.05.2018.
//

#include "SparseMatrix.h"


SparseMatrixException::SparseMatrixException(const std::string &_message) : message(_message) {}


const char *SparseMatrixException::what() const noexcept
{
    return message.c_str();
}

int SparseMatrix::computeKey(int i, int j)
{
    return i * numberLines + j;
}


int SparseMatrix::computeHashTableSize(int n)
{
    if (n == 0)
        return 0;
    return 23 * n / 100;
}


int SparseMatrix::numberOfLines()
{
    return numberLines;
}


int SparseMatrix::numberOfColumns()
{
    return numberColumns;
}


const int SparseMatrix::element(int i, int j)
{
    if (i < 0 or j < 0 or i >= numberLines or j >= numberColumns)
        throw "Invalid indeces of the element in the matrix.\n";

    int key = computeKey(i, j);
    try
    {
        int elem = hashTable.getElement(key);
        return elem;
    }
    catch (const char *)
    {
        return (int) NULL;
    }
}


void SparseMatrix::modify(int i, int j, int new_value)
{
    if (i < 0 or j < 0 or i >= numberLines or j >= numberColumns)
        throw "Invalid indeces of the element in the matrix.\n";

    int old_value;
    int key = computeKey(i, j);

    try
    {
        old_value = hashTable.getElement(key);
    }
    catch (const char *)
    {
        old_value = (int) NULL;
    }

    if (new_value and old_value)
        hashTable.update(key, new_value);
    else if (new_value and !old_value)
        hashTable.insert(key, new_value);
    else if (!new_value and old_value)
        hashTable.remove(key);
}

SparseMatrix::SparseMatrix(int numberLines, int numberColumns):
        numberLines(numberLines),
        numberColumns(numberColumns),
        hashTable(SparseMatrix::computeHashTableSize(numberLines * numberColumns), &hashFunction)
{
    if (numberLines <= 0 or numberColumns <= 0)
        throw "Invalid number of elements in the matrix.\n";
}