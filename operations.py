

books = {}
members = {}


def add_book(isbn, title, author, genre, total_copies=1):
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "available": total_copies
    }
    return f"Book '{title}' added successfully!"


def add_member(member_id, name):
    members[member_id] = {
        "name": name,
        "borrowed": []
    }
    return f"Member '{name}' added successfully!"


def borrow_book(member_id, isbn):
    if member_id not in members:
        return "Member not found!"
    if isbn not in books:
        return "Book not found!"
    if books[isbn]["available"] <= 0:
        return "Book not available right now."

    members[member_id]["borrowed"].append(isbn)
    books[isbn]["available"] -= 1
    return f"{members[member_id]['name']} borrowed '{books[isbn]['title']}'."


def return_book(member_id, isbn):
    if member_id not in members or isbn not in members[member_id]["borrowed"]:
        return "Invalid return!"
    members[member_id]["borrowed"].remove(isbn)
    books[isbn]["available"] += 1
    return f"{members[member_id]['name']} returned '{books[isbn]['title']}'."


def delete_book(isbn):
    if isbn in books:
        del books[isbn]
        return f"Book with ISBN {isbn} deleted."
    return "Book not found!"


def search_book(title):
    for isbn, book in books.items():
        if title.lower() in book["title"].lower():
            return f"Found: {book['title']} by {book['author']} (Genre: {book['genre']})"
    return "No book found with that title."
