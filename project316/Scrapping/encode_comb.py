import os, csv, re
csv_dir = "/Users/evnw/Documents/GitHub/FloorDog/project316"

def encode(csv_name):
	csv_path = os.path.join(csv_dir, csv_name)
	new_csv_name = re.sub(r"\.", '_coded.', csv_name)
	new_csv_path = os.path.join(csv_dir, new_csv_name)
	with open(new_csv_path, 'w') as new_csv_file:
		with open(csv_path, 'r') as csv_file:
			url_dict = {}
			writer = csv.writer(new_csv_file, delimiter = ',')
			reader = csv.reader(csv_file, delimiter = ',')
			for row in reader:
				#print(row)
				url_dict[row[1]] = row[0]
			csv_file_2 = open(csv_path, 'r')
			reader_2 = csv.reader(csv_file_2)
			#adjust = 0
			for row in reader_2:
				print(row)
				hasUrl = True
				for i in range(8, len(row)):
					try:
						row[i] = url_dict[row[i]]
					except:
						row[i] = ''
						continue
				'''
				if not hasUrl:
					adjust+=1
					continue
				row[0] = int(row[0]) - adjust
				'''
				new_row = []
				for ele in row:
					if ele != '':
						new_row.append(ele)
				writer.writerow(new_row)
				print(row[0])


if __name__ == '__main__':
	encode('men.csv')
	encode('women.csv')