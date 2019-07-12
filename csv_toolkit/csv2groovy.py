import csv
import os  

def file_list(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.csv':  
                L.append(os.path.join(root, file))
    return L  

def get_dict(file_list, key):
    new_dict = {}
    for filenm in file_list:
        with open(filenm, 'rt') as csv_file:
            next(csv_file)        
            data = csv.DictReader(csv_file, delimiter=",")
            for row in data:
                linestr = 'fields c' + row[key] + '_' + row['label'] + ' pos(' + row['pbyte'] + ',' +  row['pbit'] + '),' + row['bitlen']
                new_dict.setdefault(row[key], []).append(linestr)
    return new_dict


#main:
dict = get_dict(file_list('./csv/'), 'canid')
for k, v in dict.items():
    with open('./groovy/' + k + '.groovy','w') as output:
        output.writelines('package model.jp\n\n')
        output.writelines('import xxx.xx.y\n')
        output.writelines('import xxx.xx.m\n\n')
        output.writelines('can {\n')
        output.writelines('id ' + k + '\n\n')
        output.writelines('\n'.join(v))
        output.writelines('\n\n}')

