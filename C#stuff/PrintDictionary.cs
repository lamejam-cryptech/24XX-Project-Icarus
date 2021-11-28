public Class PrintDictionary<K,V>(Dictionary<K,V> dict){
    for (int i = 0; i < dict.Count; i++) {
        KeyValuePair<K, V> entry = dict.ElementAt(i);
        Console.WriteLine(entry.Key + " : " + entry.Value);
    }
}