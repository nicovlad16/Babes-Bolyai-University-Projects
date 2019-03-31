package domain.expression;


import domain.adt.MyDictionaryInterface;


public abstract class Expression
{
    public abstract int eval(MyDictionaryInterface<String, Integer> symbolTable,
                             MyDictionaryInterface<Integer, Integer> heapTable)
            throws ExpressionException;
}
