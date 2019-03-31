//
// Created by nvlad on 24.05.2018.
//

#include "HashTable.h"

HashTableException::HashTableException(const std::string &_message) : message(_message) {}


const char *HashTableException::what() const noexcept
{
    return message.c_str();
}
