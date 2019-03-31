//
// Created by nvlad on 09.05.2018.
//

#include <fstream>
#include "csv_doglist.h"
#include "../repo/file_repository.h"


void CSVDogList::display_doglist() const
{
    system(("libreoffice --calc " + filename).c_str());
}


void CSVDogList::write_to_file(std::vector<Dog> adopted_dogs)
{
    std::ofstream file(filename);

    if (!file.is_open())
        throw RepositoryException("The file could not be opened.");

    for (const auto &dog : adopted_dogs)
        file << dog;

    file.close();
}


void CSVDogList::set_filename(const std::string &filename)
{
    this->filename = filename + ".csv";
}
