import PyPDF2
import requests
import io
from urllib.parse import urlparse
import csv
from bs4 import BeautifulSoup


text_list = []
prices = []
csv_list = []
pdf_content = ''
page_links = []




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


def search_list(search_list):
    search_term = get_user_search()
    found = False
    for item in search_list:
        if search_term in item:
            print(item)
            found = True
    if not found:
        print("Not found...")


def extract_pdf_name(url):
    parsed_url = urlparse(url)
    filename = parsed_url.path.split("/")[-1]
    if filename.endswith('.pdf'):
        print(filename)
    else:
        print("URL does not point to a pdf file.")
    return pdf_content

def get_user_search():
    search = input("What would you like to search for?: ")
    return search

def read_csv_file(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip the header row
        for row in reader:
            procedure_name = row[5]
            self_pay_cost = row[12]
            csv_list.append(procedure_name + ": "+self_pay_cost)

def search_for_link(url):
    extension = '.csv'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        page_links.append(href)

    for i in page_links:
        if i and i.endswith('.csv') or i and i.endswith('.pdf'):
            print(f'Found a download link to a file: {i}')


def read_page(url):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    print(text)

def read_table(url):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    container = soup.find('div', {'class': 'col-description'})
    print(container)

    #table = container.find('table')
    #print(table)
    #rows = table.find_all('tr')



