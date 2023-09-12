import glob
import psycopg

def get_book_name(book):
    return book.split("/")[-1].split("_")[-1].split(".")[0].replace("-", " ").strip()

def read_file(book):
    f = open(book)
    s = f.read()
    f.close()
    return s

def get_full_english_name(text):
    texts = text.split("\n")
    for i in texts:
        if i.startswith(r"\mt3"):
            return i[5:].strip()

def get_full_tam_name(text):
    texts = text.split("\n")
    titles = []
    for i in texts:
        if i.startswith(r"\mt1"):
            titles.append(i[5:].strip())
            break
    for i in texts:
        if i.startswith(r"\mt2"):
            titles.append(i[5:].strip())
    if len(titles) == 3:
        titles[1], titles[0] = titles[0], titles[1]
    if "சாலொமோனின்" in titles:
        return "சாலொமோனின் உன்னதப்பாட்டு"
    if "புலம்பல்" in titles:
        return "எரேமியாவின் புலம்பல்"
    if "யோவானுக்கு" in titles:
        return "யோவானுக்கு வெளிப்படுத்தின விசேஷம்"
    return " ".join(titles).strip()

books = glob.glob("./usfm/*")
books.sort()
book_texts = [read_file(i) for i in books]
book_names = [get_book_name(i) for i in books]
book_full_english_names = [get_full_english_name(i) for i in book_texts]
book_full_tam_names = [get_full_tam_name(i) for i in book_texts]
book_tam_names = [
    "ஆதியாகமம்",
    "யாத்திராகமம்",
    "லேவியராகமம்",
    "எண்ணாகமம்",
    "உபாகமம்",
    "யோசுவா",
    "நியாயாதிபதிகள்",
    "ரூத்",
    "1 சாமுவேல்",
    "2 சாமுவேல்",
    "1 இராஜாக்கள்",
    "2 இராஜாக்கள்",
    "1 நாளாகமம்",
    "2 நாளாகமம்",
    "எஸ்றா",
    "நெகேமியா",
    "எஸ்தர்",
    "யோபு",
    "சங்கீதம்",
    "நீதிமொழிகள்",
    "பிரசங்கி",
    "உன்னதப்பாட்டு",
    "ஏசாயா",
    "எரேமியா",
    "புலம்பல்",
    "எசேக்கியேல்",
    "தானியேல்",
    "ஓசியா",
    "யோவேல்",
    "ஆமோஸ்",
    "ஒபதியா",
    "யோனா",
    "மீகா",
    "நாகூம்",
    "ஆபகூக்",
    "செப்பனியா",
    "ஆகாய்",
    "சகரியா",
    "மல்கியா",
    "மத்தேயு",
    "மாற்கு",
    "லூக்கா",
    "யோவான்",
    "அப்போஸ்தலர்",
    "ரோமர்",
    "1 கொரிந்தியர்",
    "2 கொரிந்தியர்",
    "கலாத்தியர்",
    "எபேசியர்",
    "பிலிப்பியர்",
    "கொலோசெயர்",
    "1 தெசலோனிக்கேயர்",
    "2 தெசலோனிக்கேயர்",
    "1 தீமோத்தேயு",
    "2 தீமோத்தேயு",
    "தீத்து",
    "பிலேமோன்",
    "எபிரேயர்",
    "யாக்கோபு",
    "1 பேதுரு",
    "2 பேதுரு",
    "1 யோவான்",
    "2 யோவான்",
    "3 யோவான்",
    "யூதா",
    "வெளிப்படுத்தின விசேஷம்"
]

print(len(book_tam_names))
