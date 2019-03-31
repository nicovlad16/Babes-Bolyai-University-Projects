package domain.adt;


import java.util.*;


public class MyDictionary<TKey, TValue> implements MyDictionaryInterface<TKey, TValue>
{
    private Map<TKey, TValue> hashmap;


    public MyDictionary()
    {
        hashmap = new HashMap<>();
    }


    @Override
    public boolean isDefined(TKey id)
    {
        return hashmap.get(id) != null;
    }


    @Override
    public void update(TKey id, TValue val) throws AdtException
    {
        if (!hashmap.containsKey(id))
            throw new AdtException("Inexistent key.");
        hashmap.put(id, val);
    }


    @Override
    public void add(TKey id, TValue val) throws AdtException
    {
        if (hashmap.containsKey(id))
            throw new AdtException("Existent key.");
        hashmap.put(id, val);
    }


    @Override
    public TValue lookup(TKey id) throws AdtException
    {
        TValue value = hashmap.get(id);
        if (value == null)
            throw new AdtException("Inexistent key.");
        return value;
    }


    public Map<TKey, TValue> getMap()
    {
        return hashmap;
    }


    public void setHashmap(Map<TKey, TValue> hashmap)
    {
        this.hashmap = hashmap;
    }


    @Override
    public MyDictionaryInterface<TKey, TValue> cloneDictionary()
    {
        MyDictionaryInterface<TKey, TValue> dictionary = new MyDictionary<>();
        for (TKey key : keySet())
        {
            try
            {
                dictionary.add(key, hashmap.get(key));
            }
            catch (AdtException ignored)
            {
            }
        }
        return dictionary;
    }


    @Override
    public String toString()
    {
        String str = "";
        for (HashMap.Entry<TKey, TValue> element : hashmap.entrySet())
        {
            str += element.getKey().toString() + " --> "
                    + element.getValue().toString() + "\n";
        }
        return str;
    }


    @Override
    public void remove(TKey key) throws AdtException
    {
        if (!hashmap.containsKey(key))
            throw new AdtException("Inexisting key.");
        hashmap.remove(key);
    }


    @Override
    public TValue get(TKey key) throws AdtException
    {
        if (!hashmap.containsKey(key))
            throw new AdtException("Inexisting key.");
        return hashmap.get(key);
    }


    @Override
    public boolean containsKey(TKey key)
    {
        return hashmap.containsKey(key);
    }


    @Override
    public boolean containsValue(TValue value)
    {
        return hashmap.containsValue(value);
    }


    @Override
    public Set<TKey> keySet()
    {
        return hashmap.keySet();
    }


    @Override
    public Collection<TValue> values()
    {
        return hashmap.values();
    }


    @Override
    public Set<Map.Entry<TKey, TValue>> entrySet()
    {
        return hashmap.entrySet();
    }


    @Override
    public void setContent(Set<Map.Entry<TKey, TValue>> set) throws AdtException
    {
        hashmap.clear();
        for (Map.Entry<TKey, TValue> entry : set)
            this.add(entry.getKey(), entry.getValue());
    }
}
