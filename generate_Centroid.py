
import csv

f = open('./Data/taxiTripsPart.csv')
reader = csv.DictReader(f)

res = []
flag = 0
for row in reader:
    if int(row['Pickup Community Area']) > flag:
        res.append([row['Pickup Community Area'], row['Pickup Centroid Latitude'], row['Pickup Centroid Longitude']])
        flag += 1


outfile = open('/home/zanesx/Desktop/Crime_Project/Data/centroid_community.csv','w')
writer = csv.writer(outfile, delimiter=';', quotechar='"')
writer.writerows(res)
print (res)
outfile.close()