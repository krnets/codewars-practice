using System.Collections.Generic;
using System.Linq;

namespace DictionaryMergerKata
{
    public sealed class DictionaryMerger
    {
        public static Dictionary<TKey, TValue[]> Merge<TKey, TValue>(params Dictionary<TKey, TValue>[] dicts)
        {
            var result = new Dictionary<TKey, List<TValue>>();

            foreach (var dict in dicts)
            {
                foreach (var (key, value) in dict)
                {
                    if (!result.ContainsKey(key))
                        result[key] = new List<TValue>();

                    result[key].Add(value);
                }
            }

            return result.ToDictionary(pair => pair.Key, pair => pair.Value.ToArray());
        }
    }
}