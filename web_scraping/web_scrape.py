
import requests
from bs4 import BeautifulSoup

classino = requests.get(
    "https://www.classino.com/coursesDetails?id=08fa306d-3805-4160-b06d-e956263bd64c"
)
txt = classino.text

soup = BeautifulSoup(txt, "html.parser")

# عنوان صفحه
print(soup.find("title").text)

# عنوان‌های اصلی
print(soup.find_all(["h1", "h2"]))

# عنوان دوره با استفاده از class
print(soup.find("h1", class_="text-2xl").text)

# استخراج لینک تصاویر
images = soup.find_all("img")

for img in images:
    src = img.get("src")
    if src:
        print(src)
