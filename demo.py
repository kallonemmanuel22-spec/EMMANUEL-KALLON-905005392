
from operations import add_book, add_member, borrow_book, return_book, delete_book, search_book


print(add_book("001", "Python for Everyone", "Dr. Emmanuel", "Fiction"))
print(add_book("002", "World History", "John Smith", "History"))
print(add_book("003", "Narrative Writing", "Jane Ray", "Narrative"))
print(add_book("004", "The Great Novel", "Peter Kane", "Novel"))


print(add_member(10, "Emmanuel Kallon"))
print(add_member(41, "Samuel Siaka"))
print(add_member(25, "Abu"))


print(borrow_book(10, "001"))
print(return_book(10, "001"))


print(search_book("Python"))


print(delete_book("004"))
