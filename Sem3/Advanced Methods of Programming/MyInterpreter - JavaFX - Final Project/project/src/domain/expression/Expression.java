package domain.expression;


import domain.adt.MyDictionaryInterface;


public abstract class Expression
{
    public abstract int evaluate(MyDictionaryInterface<String, Integer> symbolTable,
                                 MyDictionaryInterface<Integer, Integer> heapTable)
            throws ExpressionException;
}
