import csv
import os  
import glob

def get_dict():
    new_dict = {}
    for filenm in glob.glob('./csv/*.csv'):
        with open(filenm, 'rt') as csv_file:
            next(csv_file)        
            data = csv.DictReader(csv_file, delimiter=",")
            for row in data:
                linestr = 'fields c' + row['canid'] + '_' + row['label'] + ' pos(' + row['pbyte'] + ',' +  row['pbit'] + '),' + row['bitlen']
                new_dict.setdefault(row['canid'], []).append(linestr)
    return new_dict

#main:
dict = get_dict()
for k, v in dict.items():
    with open('./groovy/' + k + '.groovy','w') as output:
        output.writelines('package model.jp\n\n')
        output.writelines('import xxx.xx.y\n')
        output.writelines('import xxx.xx.m\n\n')
        output.writelines('can {\n')
        output.writelines('id ' + k + '\n\n')
        output.writelines('\n'.join(v))
        output.writelines('\n\n}')

print(os.listdir('.'))