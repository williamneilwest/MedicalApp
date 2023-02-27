import file_reader

url = 'https://healthy.kaiserpermanente.org/content/dam/kporg/final/documents/health-education-materials/fact-sheets/sample-fee-list-siganture-mas-en-2022.pdf'
path = 'CSVs/640303091_stdominichospital_shoppableservices.csv'
url2 = 'https://www.stdom.com/patients-and-visitors/patient-guide/pricing'
url3 = 'https://www.denverhealth.org/patients-visitors/billing-insurance/price-transparency'
url4 = 'https://search.hospitalpriceindex.com/hpi2/hospital/denverhealthmaincampus/7840or?page=1'
url5 = 'https://search.hospitalpriceindex.com/hpi2/machineReadable/denverhealthmaincampus/7840or'
url6 = 'https://www.kindredhospitals.com/locations/ltac/kindred-hospital-denver/patient-experience/what-to-expect#StandardCharges'
file_reader.list_tags(url4)