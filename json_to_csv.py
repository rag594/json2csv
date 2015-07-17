__author__ = 'raghavrastogi'

import json
import csv
import os

path = "/Users/raghavrastogi/Desktop/json2csv/data/data"

csv_file = open('/Users/raghavrastogi/Desktop/out.csv','wb')


#inside data directory
data_dir = os.listdir(path)
print data_dir


def read_dir_to_csv(hid_dir,new_path,hid):
    for j in range(len(hid_dir)):
        #print hid_dir[j]
        if (hid_dir[j] == '.DS_Store') or (hid_dir[j] == '._.DS_Store') or hid_dir[j] == '.DS_Store':
            continue
        else:
            #print hid_dir[j]
            file_read = open(new_path+"/"+hid_dir[j],'rb')
            data = json.load(file_read)
            #print data
            typ = hid_dir[j].split('.')[0][11:]
            #print typ
            writer = csv.writer(csv_file)
            name = (data[0]['name']).encode('ascii', 'ignore').decode('ascii')
            writer.writerow([hid,typ,name,data[0]['geometry']['location']['lat'],data[0]['geometry']['location']['lng'],data[0]['place_id']])

#inside each directory
for i in range(1,len(data_dir)):
    print i
    if i == 28648 or i == 28649 or i == 32347:
        continue
    else:
        new_path = path+"/"+data_dir[i]
        #print new_path
        hid_dir = os.listdir(new_path)
        #print hid_dir
        print data_dir[i]
        print path+"/"+data_dir[i]
        read_dir_to_csv(hid_dir,new_path,data_dir[i])