package domain.statement.HeapStatements;


import domain.adt.AdtException;
import domain.adt.MyStack;
import domain.adt.MyStackInterface;


public class HeapAddressBuilder
{
    private Integer address = 0;
    private MyStackInterface<Integer> freeAddresses = new MyStack<>();


    public Integer getFreeAddress()
    {
        try
        {
            return freeAddresses.pop();
        }
        catch (AdtException ignored)
        {
            address++;
            return address;
        }
    }
}