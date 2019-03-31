//
// Created by nvlad on 18.03.2018.
//

#include "dd.mm.yyyy.h"

int valid_date(int day, int month, int year)
{
/* return: 1- the date is valid
 *         0 - otherwise */
    if (day < 1 || day > 31)
        return 0;
    if (month < 1 || month > 12)
        return 0;
    if (year < 1900 || year > 2100)
        return 0;
    if (month == 2 && day == 29 && year % 4 != 0)
        return 0;
    if (month == 2 && day > 29)
        return 0;
    if ((month == 4 || month == 6 || month == 9 || month == 11) && day == 31)
        return 0;
    return 1;
}

int compare_date(int day1, int month1, int year1, int day2, int month2, int year2)
{
/* compares two dates
 * return: 1 - the first date is smaller than the second one
 *         -1 - the first date is greater than the second one
 *         0 - they are equal */
    if (year1 > year2)
        return -1;
    else if (year1 < year2)
        return 1;
    else if (month1 > month2)
        return -1;
    else if (month1 < month2)
        return 1;
    else if (day1 > day2)
        return -1;
    else if (day1 < day2)
        return 1;
    else
        return 0;
}