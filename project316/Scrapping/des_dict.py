import os, csv, re

csv_dir = "/Users/evnw/Documents/GitHub/FloorDog/project316"    # put the directory of all the csv files here


def get_dict(gender):
	# dictionary for description and material, each pair is 'word: number of appearence'
	des_dict = {}
	mat_dict = {}

	# create csv reader for clothes data csv file
	csv_path = os.path.join(csv_dir, gender+'.csv')         
	csv_file = open(csv_path, 'r')
	reader = csv.reader(csv_file, delimiter = ',')

	# create csv writer for the dictionary of description
	des_dict_path = os.path.join(csv_dir, gender+'_des_dict.csv')
	des_dict_file = open(des_dict_path, 'w')
	des_writer = csv.writer(des_dict_file, delimiter = ',')

	# create csv writer for the dictionary of material
	mat_dict_path = os.path.join(csv_dir, gender+'_mat_dict.csv')
	mat_dict_file = open(mat_dict_path, 'w')
	mat_writer = csv.writer(mat_dict_file, delimiter = ',')

	i = 0                      # for test use
	for row in reader:
		print(row[0])          # index
		description = row[6]
		material = row[7]

		# remove unimportant words in material; leaves a list of only the names of materials
		material = re.sub(r"[0-9]+%?", '', material)             # remove percentage
		material = re.sub(r"[A-Z][a-z]+ ?:", '', material)       # remove clothes part such as 'body'
		material = re.sub(r",|\.", '', material)                    # remove ',' and '.'
		material = material.split(' ')                           # split string
		material = list(filter(None, material))                  # remove empty element


		description = re.sub(r",|\.", '', description)           # remove 
		description_single = description.split(' ')              # list for every single word in description

		
		# you can insert some filter here, to remove some words like 'at', 'and', or some words that have 'ing'.
		# If you need to use regular expression to match some word, ask me and I can write it for you.
		# example:
		temp = []
		for ele in description_single:
			jud_1 = ele in ['a', 'at', 'the', 'and', 'in']           
			jud_2 = re.search(r".*ing$", ele)                # check if the word ends with 'ing'
			if not (jud_1 or jud_2):
				temp.append(ele)
		description_single = temp

		description_double = []
		for j in range(0, len(description_single) - 1):
			description_double.append(description_single[j] + ' ' + description_single[j+1])

		'''
		same as above, you can do some fitler here
		'''

		# count appearrance for material
		for ele in material:
			if not ele in mat_dict:
				mat_dict[ele] = 1
			else:
				mat_dict[ele] += 1
		
		# count appearrance for descriptions words
		for ele in description_single:
			if not ele in des_dict:
				des_dict[ele] = 1
			else:
				des_dict[ele] += 1

		for ele in description_double:
			if not ele in des_dict:
				des_dict[ele] = 1
			else:
				des_dict[ele] += 1

		'''
		test use, if you want to print some results in the middle, use this
		i+=1
		if i ==5:
			break
		'''
	for key in mat_dict.keys():
		temp =[key, mat_dict[key]]
		mat_writer.writerow(temp)

	for key in des_dict.keys():
		temp = [key, des_dict[key]]
		des_writer.writerow(temp)

if __name__ == '__main__':
	get_dict('men')
	get_dict('women')