import os
import pandas as pd 


dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'Data', 'IMDCyclone')
print("Seeking IMDCyclone Excel files at ", file_path)
file_names = os.listdir(file_path)
print("Seeking IMDCyclone Excel files successful. Found %d files.", len(file_names))


def getAllExcelFileNames():
	if len(file_names) > 0:
		save_path = os.path.join(dir_path, 'Resources')
		os.chdir(save_path)
	#	with open("IMDCyclone Excel file_names.csv", "wb") as f:
	#	    writer = csv.writer(f, delimiter=' ', lineterminator='\n')
	#	    for i in range(len(file_names)):
	#	    	writer.writerows(file_names[i])

		my_df = pd.DataFrame(file_names)
		my_df.to_csv('IMDCyclone Excel file_names.csv', index=False, header=False)		# write_to_csv in Python 3
		print("Excel file_names saved to ", save_path)



def getAllExcelFiles():
	for i in file_names:
		file_path = os.path.join(dir_path, 'Data', 'IMDCyclone', i)
		my_df = pd.read_excel(file_path)
		my_list = list(my_df)

		save_path = os.path.join(dir_path, 'Resources')
		os.chdir(save_path)
		csv_name = i[:-4] + '_Columns.csv'
		my_df1 = pd.DataFrame(my_list)
		my_df1.to_csv(csv_name, index=False, header=False)		# write_to_csv in Python 3
		print("Excel file headers saved.")

	print("Ok")


getAllExcelFileNames()
getAllExcelFiles()