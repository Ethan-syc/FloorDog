import re, csv, os

csv_dir = "/Users/evnw/Documents/GitHub/FloorDog/project316"

men_csv_path = os.path.join(csv_dir, 'men_clothes.csv')
men_csv_comb_path = os.path.join(csv_dir, 'men_clothes_comb.csv')
women_csv_path = os.path.join(csv_dir, 'women_clothes.csv')
women_csv_comb_path =os.path.join(csv_dir, 'women_clothes_comb.csv')

def merge(gender, csv_path, csv_comb_path):
	new_path = os.path.join(csv_dir, gender+'.csv')
	with open(new_path, 'w') as new_file:
		writer = csv.writer(new_file, delimiter = ',')
		with open(csv_path, 'r') as csv_file:
			reader = csv.reader(csv_file, delimiter = ',')
			for row in reader:
				for i in range(8, len(row)):
					new_url = fix_url(row[i])
					row[i] = new_url
				writer.writerow(row)
				print(row[0])
		with open(csv_comb_path, 'r') as csv_comb_file:
			reader = csv.reader(csv_comb_file, delimiter = ',')
			for row in reader:
				for i in range(8, len(row)):
					new_url = fix_url(row[i])
					row[i] = new_url
				writer.writerow(row)
				print(row[0])


def fix_url(s):
	p = re.compile(r"href=\"")
	s = re.sub(p, '', s)
	s = re.sub(r"\"", '', s)
	s = "https://www.ssense.com" + s
	return s

if __name__ == '__main__':
	merge('men', men_csv_path, men_csv_comb_path)
	merge('women', women_csv_path, women_csv_comb_path)