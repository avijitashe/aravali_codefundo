import os
import pandas as pd 

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'Data', 'IMDCyclone')
file_names = os.listdir(file_path)
print("Seeking IMDCyclone Excel files successful. Found %d files.", len(file_names))

"""
fields = ['year', 'from_mon', 'to_mon', 'from_da', 'to_da', 'from_hr', 'to_hr', 'wind_sp', 'press', 'cat']

C is Cyclone 34 knots
SC is Super Cyclone 48 knots and higher
CD Cyclonic Depression - to be cyclonic conditions
"""

def parse_Frequency_of_files():
	prefix = 'Frequency of'
	new_list = [i for i in file_names if i.startswith(prefix)]
	print(new_list)
	print("Found %d file", len(new_list))

	# Empty pandas dataframe
	new_df = pd.DataFrame()

	# Find it's columns and start extracting data
	for i in new_list:
		this_path = os.path.join(dir_path, 'Data', 'IMDCyclone', i)
		my_df = pd.read_excel(this_path)
		colm_names = list(my_df)
		print("Found %d columns", len(colm_names)) 


		if '34 knots' in i:
			wind_speed = [34]*len(my_df)
			my_df['wind_sp'] = wind_speed
			category = ['C']*len(my_df) 
			my_df['cat'] = category


		if '48 knots' in i:
			wind_speed = [48]*len(my_df)
			my_df['wind_sp'] = wind_speed
			category = ['SC']*len(my_df)
			my_df['cat'] = category


		if 'depressions' in i:
			wind_speed = [20]*len(my_df)
			my_df['wind_sp'] = wind_speed
			category = ['CD']*len(my_df)
			my_df['cat'] = category

		#print(my_df)

		new_df = new_df.append(my_df)


	print("New dataframe of shape %d formed", new_df.shape)

	# Save it in Inter1
	save_path = os.path.join(dir_path, 'Inter1')
	csv_name = 'parse_Frequency_of_files.csv'
	os.chdir(save_path)
	new_df.to_csv(csv_name, index=False, header=False)
	print("Modified dataframe saved to ", save_path)


parse_Frequency_of_files()