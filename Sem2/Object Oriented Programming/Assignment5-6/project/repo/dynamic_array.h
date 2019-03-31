//
// Created by nvlad on 14.04.2018.
//

#ifndef ASSIGNMENT8_9_DYNAMIC_ARRAY_H
#define ASSIGNMENT8_9_DYNAMIC_ARRAY_H

template<typename TElement>
class DynamicArray
{
private:
    int capacity;
    int length;
    TElement *content;

    void resize();


public:
    /* creates an array, of implicit length */
    DynamicArray();

    /* creates an array, of given length */
    explicit DynamicArray(int length);

    /* destroys an array, freeing the used memory */
    virtual ~DynamicArray();

    /* returns the length of the array */
    int get_length() const;

    /* adds a new element to the array */
    void add(const TElement &);

    /* updates the element from a given position with a new one */
    void update(int pos, const TElement &elem);

    /* removes the element from the given position */
    void remove(int pos);

    /* return the element from the given position */
    int get_pos(const TElement &elem);

    /* returns an actual array, of type TElement, with all the elements */
    TElement *get_all() const;

    /* makes the array iterable, overriding the [] operator */
    TElement &operator[](unsigned i);

    /* makes the array iterable, overriding the [] operator */
    const TElement &operator[](unsigned i) const;

    /* overrides the assignment operator */
    DynamicArray &operator=(const DynamicArray &array);

    /* overrides the + operator, adds a new element to the array */
    DynamicArray &operator+(const TElement &elem);

    /* overrides the - operator, removes an element from the array */
    DynamicArray &operator-(const TElement &elem);

    /* overrides the copy operator */
    DynamicArray(const DynamicArray &array);

    /* checks if a given element exists in the array */
    bool find(const TElement &elem);
};


template<typename TElement>
DynamicArray<TElement>::DynamicArray()
{
    capacity = 10;
    length = 0;
    content = new TElement[capacity];
}


template<typename TElement>
DynamicArray<TElement>::DynamicArray(int len)
{
    capacity = len;
    length = 0;
    content = new TElement[capacity];
}


template<typename TElement>
DynamicArray<TElement>::~DynamicArray()
{
    delete[] content;
}


template<typename TElement>
int DynamicArray<TElement>::get_length() const
{
    return length;
}


template<typename TElement>
TElement &DynamicArray<TElement>::operator[](unsigned i)
{
    return content[i];
}


template<typename TElement>
const TElement &DynamicArray<TElement>::operator[](unsigned i) const
{
    return content[i];
}


template<typename TElement>
void DynamicArray<TElement>::add(const TElement &elem)
{
    if (length == capacity)
        resize();
    content[length] = elem;
    length++;
}


template<typename TElement>
void DynamicArray<TElement>::resize()
{
    int i;
    TElement *new_content;

    capacity *= 2;
    new_content = new TElement[capacity];
    i = 0;
    while (i < length)
    {
        new_content[i] = content[i];
        i++;
    }
    delete[] content;
    content = new_content;
}


template<typename TElement>
void DynamicArray<TElement>::remove(int pos)
{
    int i;

    if (pos < 0 || pos >= length)
        return;
    i = pos;
    while (i < length - 1)
    {
        content[i] = content[i + 1];
        i++;
    }
    length--;
}


template<typename TElement>
void DynamicArray<TElement>::update(int pos, const TElement &elem)
{
    if (pos < 0 || pos >= length)
        return;
    content[pos] = elem;
}


template<typename TElement>
TElement *DynamicArray<TElement>::get_all() const
{
    return content;
}


template<typename TElement>
DynamicArray<TElement>::DynamicArray(const DynamicArray<TElement> &array)
{
    int i;

    length = array.length;
    capacity = array.capacity;
    content = new TElement[capacity];

    i = 0;
    while (i < length)
    {
        content[i] = array.content[i];
        i++;
    }
}


template<typename TElement>
DynamicArray<TElement> &DynamicArray<TElement>::operator=(const DynamicArray &array)
{
    int i;

    if (this == &array)
        return *this;

    length = array.length;
    capacity = array.capacity;
    delete[] content;
    content = new TElement[capacity];

    i = 0;
    while (i < length)
    {
        content[i] = array.content[i];
        i++;
    }
    return *this;
}


template<typename TElement>
DynamicArray<TElement> &DynamicArray<TElement>::operator+(const TElement &elem)
{
    add(elem);
    return *this;
}


template<typename TElement>
DynamicArray<TElement> &DynamicArray<TElement>::operator-(const TElement &elem)
{
    int i;
    i = 0;
    while (i < length)
    {
        if (content[i] == elem)
            remove(i);
        i++;
    }
    return *this;
}


template<typename TElement>
bool DynamicArray<TElement>::find(const TElement &elem)
{
    int i = 0;
    while (i < length)
    {
        if (content[i] == elem)
            return true;
        i++;
    }
    return false;
}

//template<typename TElement>
//void DynamicArray<TElement>::remove(const TElement &elem)
//{
//    int pos = get_pos(elem);
//    remove(pos);
//
//}

template<typename TElement>
int DynamicArray<TElement>::get_pos(const TElement &elem)
{

    int i = 0;
    while (i < length)
    {
        if (content[i] == elem)
            return i;
        i++;
    }
    return -1;
}


#endif //ASSIGNMENT8_9_DYNAMIC_ARRAY_H
