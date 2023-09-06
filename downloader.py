import requests
import threading

arr = []

ar = range(10)

for a in ar:
    for b in ar:
        for c in ar:
            for d in ar:
                arr.append(f"{a}{b}{c}{d}")

arr = arr[:1166]

urls = [f"https://ia600909.us.archive.org/BookReader/BookReaderImages.php?zip=/12/items/Tamil-Bible-BSI-OV-1957/Tamil-BSI-OV-1957_jp2.tar&file=Tamil-BSI-OV-1957_jp2/Tamil-BSI-OV-1957_{i}.jp2&id=Tamil-Bible-BSI-OV-1957" for i in arr]

def download_image(url, fname):
    print(f"Downloading {fname}")
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"jpeg/{fname}.jpg", "wb") as file:
            file.write(response.content)
    else:
        print(f"Something went wrong when trying {fname}")

arr1 = arr[:146]
arr2 = arr[146:292]
arr3 = arr[292:438]
arr4 = arr[438:584]
arr5 = arr[584:730]
arr6 = arr[730:876]
arr7 = arr[876:1022]
arr8 = arr[1022:]

def download(arrx):
    for i in arrx:
        url = f"https://ia600909.us.archive.org/BookReader/BookReaderImages.php?zip=/12/items/Tamil-Bible-BSI-OV-1957/Tamil-BSI-OV-1957_jp2.tar&file=Tamil-BSI-OV-1957_jp2/Tamil-BSI-OV-1957_{i}.jp2&id=Tamil-Bible-BSI-OV-1957"
        fname = i
        download_image(url, fname)

t1 = threading.Thread(target=download, args=((arr1, )))
t2 = threading.Thread(target=download, args=((arr2, )))
t3 = threading.Thread(target=download, args=((arr3, )))
t4 = threading.Thread(target=download, args=((arr4, )))
t5 = threading.Thread(target=download, args=((arr5, )))
t6 = threading.Thread(target=download, args=((arr6, )))
t7 = threading.Thread(target=download, args=((arr7, )))
t8 = threading.Thread(target=download, args=((arr8, )))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()


t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
