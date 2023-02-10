link = 'https://www.codewars.com/kata/515bb423de843ea99400000a/python'

from math import ceil, floor


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection: list, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return ceil(len(self.collection) / self.items_per_page)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index + 1 < self.page_count():
            return self.items_per_page
        elif page_index + 1 == self.page_count():
            return len(self.collection) - floor(len(self.collection) / self.items_per_page) * self.items_per_page
        return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index in range(len(self.collection)):
            return floor(item_index/self.items_per_page)
        return -1


page = PaginationHelper(list(range(1, 25)), 10)
print(page.page_index(23))
