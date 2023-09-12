import glob
import psycopg

def get_book_number_and_name(book):
    return book.split("/")[-1].split("_")[-1].split(".")[0].replace("-", " ")

def read_file(book):
    f = open(book)
    s = f.read()
    f.close()
    return s

books = glob.glob("./usfm/*")
book_names = [get_book_number_and_name(i) for i in books]
book_texts = [read_file(i) for i in books]

