//
// Created by nvlad on 24.05.2018.
//

#ifndef PROJECT_DSA_HASHTABLE_H
#define PROJECT_DSA_HASHTABLE_H

#include <clocale>
#include <exception>
#include <string>
#include <utility>


template<typename TElement>
class HashTable
{
private:

    class HashNode
    {
    public:
        int key;
        TElement value;
        HashNode *next;
    public:
        HashNode(int key, TElement value) : key(key), value(value), next(nullptr)
        {}
    };


    HashNode **htable;
    int m{};

    int (*hfunction)(int, int){};

    int hashFunc(int key);

public:
    HashTable() = default;

    HashTable(int m, int (*hfunction)(int, int));

    ~HashTable();

    void remove(int key);

    TElement getElement(int key);

    void update(int key, TElement value);

    void insert(int key, TElement value);


    friend class IteratorSparseMatrix;


    friend class SparseMatrix;

};


template<typename TElement>
void HashTable<TElement>::remove(int key)
{
    int hash_val = hashFunc(key);
    HashNode *entry = htable[hash_val];
    HashNode *prev = nullptr;

    while (entry != nullptr and entry->key < key)
    {
        prev = entry;
        entry = entry->next;
    }

    if (entry == nullptr)
        throw "Inexisting key.\n";
    if (entry->key != key)
        throw "Inexisting key.\n";

    if (prev != nullptr)
        prev->next = entry->next;
    else
        htable[hash_val] = entry->next;

    delete entry;
}


template<typename TElement>
TElement HashTable<TElement>::getElement(int key)
{
    int hash_val = hashFunc(key);
    HashNode *entry = htable[hash_val];

    while (entry and entry->key < key)
    { entry = entry->next; }

    if (entry and entry->key == key)
        return entry->value;
    else
        throw "Inexisting key.\n";
}


template<typename TElement>
void HashTable<TElement>::update(int key, TElement value)
{
    int hash_val = hashFunc(key);
    HashNode *entry = htable[hash_val];

    while (entry != nullptr && entry->key < key)
        entry = entry->next;

    if (entry and entry->key == key)
        entry->value = value;
    else
        throw "Inexisting key.\n";
}


template<typename TElement>
void HashTable<TElement>::insert(int key, TElement value)
{
    int hash_val = hashFunc(key);
    HashNode *entry = htable[hash_val];
    auto *new_node = new HashNode(key, value);

    if (entry == nullptr)
        htable[hash_val] = new_node;
    else if (key < entry->key)
    {
        new_node->next = entry;
        htable[hash_val] = new_node;
    } else
    {
        while (entry->next and entry->next->key < key)
        { entry = entry->next; }

        if (entry->key == key)
            throw "Existing key.\n";
        else
        {
            new_node->next = entry->next;
            entry->next = new_node;
        }
    }
}


template<typename TElement>
HashTable<TElement>::~HashTable()
{
    int i = 0;
    while (i < m)
    {
        HashNode *entry = htable[i];
        HashNode *prev = NULL;
        while (entry != NULL)
        {
            prev = entry;
            entry = entry->next;
            delete prev;
        }
        i++;
    }
    delete[] htable;
}


template<typename TElement>
int HashTable<TElement>::hashFunc(int key)
{
    return hfunction(key, m);
}


template<typename TElement>
HashTable<TElement>::HashTable(int m, int (*hfunction)(int, int)):m(m), hfunction(hfunction)
{
    htable = new HashNode *[m];
    int i = 0;
    while (i < m)
    {
        htable[i] = NULL;
        i++;
    }
}


class HashTableException : public std::exception
{
private:
    std::string message;
public:
    explicit HashTableException(const std::string &_message);

    const char *what() const noexcept override;

};


#endif //PROJECT_DSA_HASHTABLE_H
