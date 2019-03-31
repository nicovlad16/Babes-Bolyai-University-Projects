using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;

namespace MyInterpreter_CSharp.domain.adt
{
    public class MyDictionary<TKey, TValue> : IMyDictionary<TKey, TValue>
    {
        private Dictionary<TKey, TValue> _dictionary;

        public MyDictionary()
        {
            _dictionary = new Dictionary<TKey, TValue>();
        }

        public bool IsDefined(TKey key)
        {
            return _dictionary.ContainsKey(key);

        }

        public void Update(TKey key, TValue value)
        {
            if (!_dictionary.ContainsKey(key))
                throw new AdtException("Inexistent key.");
            _dictionary.Remove(key);
            _dictionary.Add(key, value);
        }

        public void Add(TKey key, TValue value)
        {
            if (_dictionary.ContainsKey(key))
                throw new AdtException("Existent key.");
            _dictionary.Add(key, value);
        }

        public TValue Lookup(TKey key)
        {
            if (_dictionary.TryGetValue(key, out TValue value))
                return value;
            throw new AdtException("Inexistent key.");
        }

        public void Put(TKey key, TValue value)
        {
            if (_dictionary.ContainsKey(key))
                throw new AdtException("Existent key.");
            _dictionary.Add(key, value);
        }

        public void Remove(TKey key)
        {
            if (!_dictionary.ContainsKey(key))
                throw new AdtException("Inexistent key.");
            _dictionary.Remove(key);
        }

        public TValue Get(TKey key)
        {
            if (_dictionary.TryGetValue(key, out var value))
                return value;
            throw new AdtException("Inexistent key.");
        }

        public HashSet<TKey> GetKeys()
        {
            return new HashSet<TKey>(_dictionary.Keys);
        }

        public List<TValue> GetValues()
        {
            return new List<TValue>(_dictionary.Values);
        }

        public override string ToString()
        {
            string str = "";
            foreach (var element in _dictionary)
            {
                str += element.Key + " --> " + element.Value + "\n";
            }
            return str;
        }
    }
}