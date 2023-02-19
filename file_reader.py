import PyPDF2
import requests
import io
from urllib.parse import urlparse


text_list = []
prices = []
pdf_content = ''




def extract_text_from_pdf_url(url):
    response = requests.get(url)
    pdf_content = io.BytesIO(response.content)
    pdf_reader = PyPDF2.PdfReader(pdf_content)
    num_pages = len(pdf_reader.pages)

    for page_num in range(num_pages):
        # Get the page object
        page = pdf_reader.pages[page_num]

        # Extract the text from the page
        text = page.extract_text()
        text_list.extend(text.split('\n'))
        symbol = '$'

    for item in text_list:
        if symbol in item:
            # print(f"Symbol '{symbol}' found in '{item}'")
            prices.append(item)




def extract_text_pdf(path):
    # Open the PDF file
    pdf_file = open(path, 'rb')

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Get the number of pages in the PDF file
    num_pages = len(pdf_reader.pages)

    # Iterate through all the pages
    for page_num in range(num_pages):
        # Get the page object
        page = pdf_reader.pages[page_num]

        # Extract the text from the page
        text = page.extract_text()

        text_list.extend(text.split('\n'))

    # Close the PDF file
    pdf_file.close()
    symbol = '$'

    for item in text_list:
        if symbol in item:
            # print(f"Symbol '{symbol}' found in '{item}'")
            prices.append(item)


def print_list(list_to_print):
    print(list_to_print)


def search_list(search_term):
    found = False
    for item in prices:
        if search_term in item:
            print(item)
            found = True
    if not found:
        print("Not found...")


def extract_pdf_name(url):
    parsed_url = urlparse(url)
    filename = parsed_url.path.split("/")[-1]
    if filename.endswith(".pdf"):
        print(filename)
    else:
        print("URL does not point to a pdf file.")
    return pdf_content