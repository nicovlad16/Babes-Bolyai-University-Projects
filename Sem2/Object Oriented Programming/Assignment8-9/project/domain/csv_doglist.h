//
// Created by nvlad on 09.05.2018.
//

#ifndef ASSIGNMENT8_9_CSV_DOGLIST_H
#define ASSIGNMENT8_9_CSV_DOGLIST_H

#include "file_doglist.h"

class CSVDogList : public FileDogList
{
public:
    /* writes the adopted dog list to file
       throws: FileException - if it cannot write */
    void write_to_file(std::vector<Dog> adopted_dogs) override;

    /* displays the adopted dogs list using gedit */
    void display_doglist() const override;

    /* changes the current file, for writing and opening with a different program */
    void set_filename(const std::string &filename) override;
};

#endif //ASSIGNMENT8_9_CSV_DOGLIST_H
