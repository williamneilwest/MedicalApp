import file_reader

url = 'https://healthy.kaiserpermanente.org/content/dam/kporg/final/documents/health-education-materials/fact-sheets/sample-fee-list-siganture-mas-en-2022.pdf'

file_reader.extract_text_from_pdf_url(url)
file_reader.search_list("Urine")