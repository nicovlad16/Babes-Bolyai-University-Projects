using System.Collections.Generic;

namespace MyInterpreter_CSharp.domain.adt
{
    public interface IMyDictionary<TKey, TValue>
    {
        bool IsDefined(TKey key);
        void Update(TKey key, TValue value);
        void Add(TKey key, TValue value);
        TValue Lookup(TKey key);
        string ToString();
        void Put(TKey key, TValue value);
        void Remove(TKey key);
        TValue Get(TKey key);
        HashSet<TKey> GetKeys();
        List<TValue> GetValues();
    }
}