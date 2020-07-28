import csv

def write_dict_to_csv_file(csv_file, dict_data, csv_columns):
  try:
      with open(csv_file, 'w') as csvfile:
          writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
          writer.writeheader()
          for data in dict_data:
              writer.writerow(data)
  except IOError:
      print("I/O error")