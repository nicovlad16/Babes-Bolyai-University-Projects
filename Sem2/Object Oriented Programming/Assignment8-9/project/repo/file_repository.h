//
// Created by nvlad on 01.05.2018.
//

#ifndef ASSIGNMENT8_9_REPOSITORY_H
#define ASSIGNMENT8_9_REPOSITORY_H

#include "../domain/dog.h"
#include <utility>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>

class RepositoryException : public std::exception
{
private:
    std::string message;
public:
    explicit RepositoryException(const std::string &_message);

    const char *what() const noexcept override;
};

template<typename TElement>
class Repository
{
private:
    std::vector<TElement> elems;
    std::string filename;

    /* reads each element from the file and adds it to the repository */
    void read_from_file();

    /* writes all the elements in the repository to the file */
    void write_to_file();

public:
    /* uses the default constructor to create the repository */
    explicit Repository(std::string filename);

    /* adds a new element to the repository
     * if it exists, exception is thrown */
    void add(const TElement &elem);

    /* returns an array with all the elements in the repository */
    std::vector<TElement> get_all();

    /* returns the number of elements in the repository */
    int get_length();

    /* checks if a given element exists in the repository */
    bool find(const TElement &elem);

    /* removes an existing element from the repository
     * if it doesn't exist, exception is thrown */
    void remove(const TElement &elem);

    /* updates an existing element with a new one
     * if it doesn't exist, exception is thrown */
    void update(TElement old_elem, TElement new_elem);
};


template<typename TElement>
void Repository<TElement>::add(const TElement &elem)
{
    if (find(elem))
        throw RepositoryException("Existing element.");

    elems.push_back(elem);
    write_to_file();
}


template<typename TElement>
std::vector<TElement> Repository<TElement>::get_all()
{
    return elems;
}


template<typename TElement>
int Repository<TElement>::get_length()
{
    return static_cast<int>(elems.size());
}


template<typename TElement>
bool Repository<TElement>::find(const TElement &elem)
{
    auto it = std::find(elems.begin(), elems.end(), elem);
    return it != elems.end();
}


template<typename TElement>
void Repository<TElement>::remove(const TElement &elem)
{
    if (!find(elem))
        throw RepositoryException("Inexisting element.");
    else
    {
        elems.erase(std::remove(elems.begin(), elems.end(), elem), elems.end());
        write_to_file();
    }

}


template<typename TElement>
void Repository<TElement>::update(const TElement old_elem, const TElement new_elem)
{
    if (!find(old_elem))
        throw RepositoryException("Inexisting element.");
    else
    {
        std::replace(elems.begin(), elems.end(), old_elem, new_elem);
        write_to_file();
    }
}


template<typename TElement>
Repository<TElement>::Repository(std::string filename)
{
    this->filename = filename;
    read_from_file();
}


template<typename TElement>
void Repository<TElement>::read_from_file()
{
    std::ifstream file(filename);

    if (!file.is_open())
        throw RepositoryException("The file could not be opened.");

    TElement elem;
    while (file >> elem)
        elems.push_back(elem);

    file.close();
}


template<typename TElement>
void Repository<TElement>::write_to_file()
{
    std::ofstream file(filename);

    if (!file.is_open())
        throw RepositoryException("The file could not be opened.");

    for (auto elem : elems)
        file << elem;

    file.close();
}


#endif //ASSIGNMENT8_9_REPOSITORY_H
