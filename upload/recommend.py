import datetime
import os

def str():
    str = ""
    for i in range(10):
        str = str + "," + i
        i += 1

    print(str)

def main():
    current_time = datetime.datetime.now().strftime('%H_%M')
    current_txt = current_time + '.txt'
    f_path = os.path.join('upload/id_lists/', current_txt)

    f = open(f_path, 'w+')
    f.write(str)
    f.close()

    return 0

