from math import ceil


class PaginationHelper:
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.item_per_page = items_per_page
        self.n, self.last_page = divmod(self.item_count(), self.item_per_page)

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return self.n + bool(self.last_page)

    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index in range(self.page_count()):
            return (self.last_page, self.item_per_page)[page_index < self.n]
        return -1

    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index in range(self.item_count()):
            return item_index // self.item_per_page
        return -1
