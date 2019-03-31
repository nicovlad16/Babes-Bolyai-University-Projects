//
// Created by nvlad on 12.05.2018.
//

#include <fstream>
#include "html_doglist.h"
#include "../repo/file_repository.h"


void HTMLDogList::write_to_file(std::vector<Dog> adopted_dogs)
{
    std::ofstream file(filename);

    if (!file.is_open())
        throw RepositoryException("The file could not be opened.");

    std::string str = "";
    str += "<!DOCTYPE html>\n";
    str += "<html>\n";
    str += "    <head>\n";
    str += "        <title>Adopted dogs list</title>\n";
    str += "    </head>\n";
    str += "    <body>\n";
    str += "        <table border=\"1\">\n";
    str += "        <tr>\n";
    str += "            <td><strong>Breed</strong></td>\n";
    str += "            <td><strong>Name</strong></td>\n";
    str += "            <td><strong>Age</strong></td>\n";
    str += "            <td><strong>Photo</strong></td>\n";
    str += "        </tr>\n";

    for (const auto &dog : adopted_dogs)
    {
        str += "        <tr>\n";
        str += "            <td>" + dog.get_breed() + "</td>\n";
        str += "            <td>" + dog.get_name() + "</td>\n";
        str += "            <td>" + std::to_string(dog.get_age()) + "</td>\n";
        str += "            <td><a href=\"" + dog.get_photo() + "\">link</a></td>\n";
        str += "        </tr>\n";
    }
    str += "        </table>\n";
    str += "    </body>\n";
    str += "</html>";

    file << str;
    file.close();
}


void HTMLDogList::display_doglist() const
{
    system(("chromium-browser " + filename).c_str());
}


void HTMLDogList::set_filename(const std::string &filename)
{
    this->filename = filename + ".html";
}

