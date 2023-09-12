import glob
import psycopg

def get_book_name(book):
    return book.split("/")[-1].split("_")[-1].split(".")[0].replace("-", " ")

def read_file(book):
    f = open(book)
    s = f.read()
    f.close()
    return s

def get_full_english_name(text):
    texts = text.split("\n")
    for i in texts:
        if i.startswith(r"\mt3"):
            return i[5:]


books = glob.glob("./usfm/*")
books.sort()
book_texts = [read_file(i) for i in books]
book_names = [get_book_name(i) for i in books]
book_full_english_names = [get_full_english_name(i) for i in book_texts]

for i, val in enumerate(book_names):
    print(f"{i+1}: {val}")
