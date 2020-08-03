import csv

def write_dict_to_csv_file(csv_file, dict_data, csv_columns):
  """Exports a python's dict_data to a csv_file with columns set by csv_columns.

  ...
  Example
  -----------
  csv_columns=['Col1', 'Col2', 'Col3']
  dict_data = [{'Col1':1,'Col2':2,'Col3':3},
                'Col1':11,'Col2':22,'Col3':33}]
  csv_file = "myFile.csv"

  write_dict_to_csv_file(csv_file, dict_data, csv_columns)

  The content of myFile.csv is the following :
  Col1,Col2,Col3
  1,2,3
  11,22,33
  """
  try:
      with open(csv_file, 'w') as csvfile:
          writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
          writer.writeheader()
          for data in dict_data:
              writer.writerow(data)
  except IOError:
      print("I/O error")