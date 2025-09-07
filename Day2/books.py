books = ["Python Basics", "Data Science", "AI Fundamentals"]

print("Initial Books:", books)

new_book = "Machine Learning"
books.append(new_book)  

remove_book = "Data Science"
if remove_book in books:   
    books.remove(remove_book)

print("Current Books:", books)

print("Total Books:", len(books))