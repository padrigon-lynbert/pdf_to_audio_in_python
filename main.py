import pyttsx3 # pyttsx3 library (pip install pyttsx3)
import fitz  # PyMuPDF library (pip install PyMuPDF)

#it will automatically create a playable file

try:
    full_text = ""

    pdf_file_path = r'D:\\manualCDmanagement\\files\\This is a test pdf.3.pdf' #add the path after the r (only pdf)

    with fitz.open(pdf_file_path) as pdf_document:
        total_pages = pdf_document.page_count
        audio_reader = pyttsx3.init()
        audio_reader.setProperty("rate", 170)

        for page_num in range(total_pages):
            page = pdf_document[page_num]
            text = page.get_text()
            full_text += text

        audio_reader.save_to_file(full_text, "audobookToMP3.mp3")
        audio_reader.runAndWait()

except Exception as error:
    print("An error occurred:", error)