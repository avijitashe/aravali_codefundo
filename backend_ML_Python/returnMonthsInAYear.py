import os
import pandas as pd 


dir_path = os.path.dirname(os.path.realpath(__file__))
file_name = "Months.txt"
file_path = os.path.join(dir_path, 'Resources', file_name)
print("Importing Months in a year from: ", file_path)


def monthsInAYear(file_path):
	months_df = pd.read_csv(file_path)
	if months_df.shape[0] == 12 :
		print("Importing Months in a year successful")
		return months_df

#print(monthsInAYear(file_path))
