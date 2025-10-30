
from operations import add_book, add_member, borrow_book, return_book, delete_book

# Add sample data
add_book("001", "Python for Everyone", "Dr. Emmanuel", "Fiction")
add_member(10, "Emmanuel Kallon")


assert borrow_book(10, "001") == "Emmanuel Kallon borrowed 'Python for Everyone'."
assert return_book(10, "001") == "Emmanuel Kallon returned 'Python for Everyone'."
assert delete_book("001") == "Book with ISBN 001 deleted."

print("All test is complete")