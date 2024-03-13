from collections import defaultdict


# def build_trie(*words, depth=1):
#     trie = defaultdict(set)

#     for word in words:
#         if len(word) >= depth:
#             trie[word[:depth]].add(word)

#     return {k: build_trie(*v, depth=depth + 1) or None for k, v in trie.items()}


def build_trie(*words):
    trie = {}

    for word in words:
        node = trie

        for i in range(len(word)):
            prefix = word[: i + 1]
            node[prefix] = node.get(prefix) or (None if prefix == word else {})
            node = node[prefix]

    return trie
