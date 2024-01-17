# class Dictionary:
#     def __init__(self):
#         self.dictionary = {}

#     def newentry(self, word, definition):
#         self.dictionary[word] = definition

#     # def look(self, key):
#     #     return self.dictionary[key] if key in self.dictionary else f"Can't find entry for {key}"

#     def look(self, key):
#         return self.dictionary.get(key, f"Can't find entry for {key}")


class Dictionary(dict):
    newentry = dict.__setitem__

    def look(self, key):
        return self.get(key, f"Can't find entry for {key}")
