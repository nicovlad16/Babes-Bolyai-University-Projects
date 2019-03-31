package domain.adt;


import java.util.Collection;
import java.util.Map;
import java.util.Set;


public interface MyDictionaryInterface<TKey, TValue>
{
    boolean isDefined(TKey id);

    void update(TKey id, TValue val) throws AdtException;

    void add(TKey id, TValue val) throws AdtException;

    TValue lookup(TKey id) throws AdtException;

    String toString();

    void remove(TKey key) throws AdtException;

    TValue get(TKey key) throws AdtException;

    boolean containsKey(TKey key);

    boolean containsValue(TValue value);

    Collection<TValue> values();

    Set<TKey> keySet();

    Set<Map.Entry<TKey, TValue>> entrySet();

    void setContent(Set<Map.Entry<TKey, TValue>> set) throws AdtException;

    Map<TKey, TValue> getMap();

    void setHashmap(Map<TKey, TValue> hashmap);

    MyDictionaryInterface<TKey, TValue> cloneDictionary();

    Iterable<? extends Map.Entry<TKey, TValue>> getAll();
}
