import pyttsx3
import PyPDF2

book = open('OOP.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

audiobook = pyttsx3.init()

for num in range(1, pages):
    page = pdfReader.getPage(1)
    text = page.extractText()
    audiobook.say(text)
    audiobook.runAndWait()