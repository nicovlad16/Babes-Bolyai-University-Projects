//
// Created by nvlad on 01.05.2018.
//

#include "file_repository.h"


RepositoryException::RepositoryException(const std::string &_message) : message(_message) {}


const char *RepositoryException::what() const noexcept
{
    return message.c_str();
}
