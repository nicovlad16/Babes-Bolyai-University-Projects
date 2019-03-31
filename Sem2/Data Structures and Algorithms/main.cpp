#include <iostream>
#include "Tests.h"
#include "SparseMatrix.h"


#define numberPages 10


void show_all_links(SparseMatrix &matrix);

void show_links_of_a_page(SparseMatrix &matrix);

void change_links_of_a_page(SparseMatrix &matrix);

void show_pagerank_of_a_page(SparseMatrix &matrix);

std::string read_string(const char *txt);

int read_number();

void initialize_links(SparseMatrix &matrix);

void print_menu();


int main()
{
    Tests::test_all();

    SparseMatrix sparseMatrix(numberPages, numberPages);

    initialize_links(sparseMatrix);

    while (true)
    {
        print_menu();
        std::string command = read_string(">> ");
        if (command == "exit")
        { exit(0); }
        if (command.length() != 1)
        {
            printf("Invalid command.\n");
            continue;
        }
        if (command[0] == '0')
        { show_all_links(sparseMatrix); }
        else if (command[0] == '1')
        { show_links_of_a_page(sparseMatrix); }
        else if (command[0] == '2')
        { change_links_of_a_page(sparseMatrix); }
        else if (command[0] == '3')
        { show_pagerank_of_a_page(sparseMatrix); }
        else
        { printf("Invalid command.\n"); }
    }
}


void print_menu()
{
    printf("0 - www.google.com\n");
    printf("1 - www.facebook.com\n");
    printf("2 - www.twitter.com\n");
    printf("3 - www.amazon.com\n");
    printf("4 - www.wikipedia.com\n");
    printf("5 - www.youtube.com\n");
    printf("6 - www.instagram.com\n");
    printf("7 - www.etsy.com\n");
    printf("8 - www.eventbrite.com\n");
    printf("9 - www.medium.com\n");
    printf("\nCommands:\n");
    printf("0.Show all links.\n");
    printf("1.Show links of a page to another one.\n");
    printf("2.Change number of links of a page to another one.\n");
    printf("3.Show the page rank of a page.\n");
}


void initialize_links(SparseMatrix &matrix)
{
    matrix.modify(1, 5, 1);
    matrix.modify(2, 7, 3);
    matrix.modify(3, 5, 4);
    matrix.modify(1, 4, 16);
    matrix.modify(1, 7, 12);
    matrix.modify(3, 4, 6);
    matrix.modify(1, 2, 1);
    matrix.modify(8, 6, 3);
    matrix.modify(9, 9, 12);
    matrix.modify(7, 1, 1);
    matrix.modify(6, 4, 13);
}


std::string read_string(const char *txt)
{
    std::string command;
    std::cout << txt;
    getline(std::cin, command);
    return std::__cxx11::string(command);
}


void show_pagerank_of_a_page(SparseMatrix &matrix)
{
    printf("Page.\n");
    int page = read_number();
    if (page < 0 or page >= numberPages)
    {
        printf("Invalid input.\n");
        change_links_of_a_page(matrix);
    }

    int i = 0;
    int sum = 0;
    while (i < numberPages)
    {
        sum += matrix.element(i, page);
        i++;
    }
    printf("Page%d has %d incoming links from the other pages.\n\n", page, sum);
}


void change_links_of_a_page(SparseMatrix &matrix)
{
    printf("Starting page.\n");
    int page1 = read_number();
    printf("Landing page.\n");
    int page2 = read_number();
    printf("Number of links.\n");
    int links = read_number();

    if (page1 < 0 or page1 >= numberPages or page2 < 0 or page2 >= numberPages or links < 0)
    {
        printf("Invalid input.\n");
        change_links_of_a_page(matrix);
    }

    matrix.modify(page1, page2, links);
    printf("Number of links successfully modified.\n\n");
}


void show_links_of_a_page(SparseMatrix &matrix)
{
    printf("Starting page.\n");
    int page1 = read_number();
    printf("Landing page.\n");
    int page2 = read_number();

    if (page1 < 0 or page1 >= numberPages or page2 < 0 or page2 >= numberPages)
    {
        printf("Invalid input.\n");
        change_links_of_a_page(matrix);
    }

    printf("Page%d has %d links to Page%d.\n\n", page1, matrix.element(page1, page2), page2);
}


void show_all_links(SparseMatrix &matrix)
{
    int i = 0;
    int j = 0;
    while (i < matrix.numberOfLines())
    {
        while (j < matrix.numberOfColumns())
        {
            printf("%d ", matrix.element(i, j));
            j++;
        }
        printf("\n");
        i++;
    }
    printf("\n");
}


int read_number()
{
    while (true)
        try
        {
            std::string line;
            getline(std::cin, line);
            char str1[2];
            str1[0] = '\0';
            char str2[2];
            str2[0] = '\0';
            int n = stoi(line);
            int number = 0;
            sscanf(line.c_str(), "%d%s %s", &number, str1, str2);
            if (n != number || str1[0] != '\0' || str2[0] != '\0')
            {
                printf("Invalid number.\n>> ");
                continue;
            }
            return n;
        }
        catch (std::invalid_argument &)
        {
            printf("Invalid number.\n>> ");
            continue;
        }
        catch (std::out_of_range &)
        {
            printf("Invalid number.\n>> ");
            continue;
        }
}
