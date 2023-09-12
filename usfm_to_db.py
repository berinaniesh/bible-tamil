import glob
import psycopg

book_div = {
    "Pentateuch": [
        "Genesis",
        "Exodus",
        "Leviticus",
        "Numbers",
        "Deutronomy",
    ],
    "HistoricalBook": [
        "Joshua",
        "Judges",
        "Ruth",
        "1 Samuel",
        "2 Samuel",
        "1 Kings",
        "2 Kings",
        "1 Chronicles",
        "2 Chronicles",
        "Ezra",
        "Nehemiah",
        "Esther",
    ],
    "WisdomBook": [
        "Job",
        "Psalms",
        "Proverbs",
        "Ecclesiastes",
        "Song of Solomon",
    ],
    "MajorProphet": [
        "Isaiah",
        "Jeremiah",
        "Lamentations",
        "Ezekiel",
        "Daniel",
    ],
    "MinorProphet": [
        "Hosea",
        "Joel",
        "Amos",
        "Obadiah",
        "Jonah",
        "Micah",
        "Nahum",
        "Habakkuk",
        "Zephaniah",
        "Haggai",
        "Zechariah",
        "Malachi",
    ],
    "Gospel": [
        "Matthew",
        "Mark",
        "Luke",
        "John",
    ],
    "History": [
        "Acts",
    ],
    "PaulineEpistle": [
        "Romans",
        "1 Corinthians",
        "2 Corinthians",
        "Galatians",
        "Ephesians",
        "Philippians",
        "Colossians",
        "1 Thessalonians",
        "2 Thessalonians",
        "1 Timothy",
        "2 Timothy",
        "Titus",
        "Philemon",
    ],
    "GeneralEpistle": [
        "Hebrews",
        "James",
        "1 Peter",
        "2 Peter",
        "1 John",
        "2 John",
        "3 John",
        "Jude",
    ],
    "Prophecy": [
        "Revelations",
    ],
}

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
    "வெளிப்படுத்தின விசேஷம்",
]


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


def get_id(text):
    text = text.split("\n")[0]
    return text[4:].strip()


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


def get_testament(i):
    if i < 39:
        return "OldTestament"
    else:
        return "NewTestament"


def get_division(book_name):
    for k, v in book_div.items():
        if book_name in v:
            return k


books = glob.glob("./usfm/*")
books.sort()
book_texts = [read_file(i) for i in books]
book_names = [get_book_name(i) for i in books]
book_full_english_names = [get_full_english_name(i) for i in book_texts]
book_full_tam_names = [get_full_tam_name(i) for i in book_texts]
book_ids = [get_id(i) for i in book_texts]
book_divisions = [get_division(i) for i in book_names]

conn = psycopg.connect(dbname="bible")
cur = conn.cursor()


def add_lang(lang):
    cur.execute("""INSERT INTO "Language" ("name") VALUES (%s)""", (lang,))
    conn.commit()


def add_translation(translation):
    cur.execute(
        """INSERT INTO "Translation" ("language_id", "name", "full_name", "year", "license", "description") VALUES ((SELECT "id" FROM "Language" WHERE "name"=%s), %s, %s, %s, %s, %s)""",
        (
            translation["language"],
            translation["name"],
            translation["full_name"],
            translation["year"],
            translation["license"],
            translation["description"],
        ),
    )
    conn.commit()


def insert_tam_books():
    for i in range(len(book_names)):
        conn.execute(
            """INSERT INTO "Book"
            ( 
            "translation_id", "name", "long_name", 
            "regional_name", "regional_long_name",
            "book_number", "abbreviation", "testament",
            "division"
            ) VALUES 
            (
            (SELECT "id" from "Translation" WHERE "name"=%s),
            %s, %s, %s, %s, %s, %s, %s, %s
            )""",
            (
                "TOVBSI",
                book_names[i],
                book_full_english_names[i],
                book_tam_names[i],
                book_full_tam_names[i],
                i+1,
                book_ids[i],
                get_testament(i),
                book_divisions[i]
            )
        )
    conn.commit()

add_lang("Tamil")
add_translation(
    {
        "language": "Tamil",
        "name": "TOVBSI",
        "full_name": "Tamil Old Version Bible Society of India",
        "year": "1957",
        "license": "Public Domain",
        "description": """Published by "The Bible Society of India and Ceylon".\nDigitization done by The Free Bible Foundation (TFBF) volunteers.\nGitHub source can be found at "https://github.com/tfbf/Bible-Tamil-Sathiyavedam-1957".\nScanned Images can be found at "https://archive.org/details/Tamil-Bible-BSI-OV-1957".""",
    }
)
insert_tam_books()

conn.close()
