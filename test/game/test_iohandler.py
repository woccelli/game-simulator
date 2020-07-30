from .context import write_dict_to_csv_file
import os

def test_write_dict_to_csv_file():
  csv_columns = ['No','Name','Country']
  csv_file = "Names.csv"
  dict_data = [
  {'No': 1, 'Name': 'Alex', 'Country': 'India'},
  {'No': 2, 'Name': 'Ben', 'Country': 'USA'},
  {'No': 3, 'Name': 'Shri Ram', 'Country': 'India'},
  {'No': 4, 'Name': 'Smith', 'Country': 'USA'},
  {'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
  ]
  write_dict_to_csv_file(csv_file, dict_data, csv_columns)
  fileobj = open(csv_file, "r")
  content = fileobj.read()
  assert content == 'No,Name,Country\n1,Alex,India\n2,Ben,USA\n3,Shri Ram,India\n4,Smith,USA\n5,Yuva Raj,India\n'
  os.remove(csv_file)

