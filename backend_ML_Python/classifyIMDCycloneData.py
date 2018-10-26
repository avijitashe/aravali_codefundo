import os
import pandas as pd 
from sklearn import ensemble, model_selection, preprocessing, tree

# import readIMDCycloneData
# import extractColumnNamesFromIMDCyclone

print("All ok...")

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'Inter1')
file_names = os.listdir(file_path)
print("Importing IMDCyclone processed files successful. Found %d files.", len(file_names))


full_file_path = os.path.join(file_path, file_names[0])

cyc_df = pd.read_csv(full_file_path)
print("Working on file ", full_file_path)

cyc_df = cyc_df.set_index('1891')
#print(cyc_df)
#print(list(cyc_df))

cat = []
for i in cyc_df.C:
	if i == 'C':
		cat.append(0)
	elif i == 'SC':
		cat.append(1)
	else:
		cat.append(2)

#print(cat)
cyc_df['cat'] = cat
#print(cyc_df)


"""
RANDOM FOREST
------ ------
"""

ignore = ["cat", "C"]
cols = [c for c in cyc_df.columns if c not in ignore] # Gets only the column names, not the columns

X = cyc_df[cols] 			# Gets the columns using the names
y = cyc_df.cat

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state=45)

print(X_train.shape)
print(X_test.shape)

randomForestModel_1 = ensemble.RandomForestClassifier(random_state=45)
randomForestModel_1.fit(X_train, y_train)
print("Model Score: ", randomForestModel_1.score(X_test, y_test))

"""
Model Score:  0.9824561403508771
----- -----   ------------------
"""