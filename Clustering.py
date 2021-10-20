from geopy.distance import geodesic
from math import atanh, ceil
import random
import pandas as pd
import xlsxwriter
from pandas import ExcelWriter
from pandas import ExcelFile

df=pd.read_excel("D:\\SY CS\\CAPSTONE\\Book1.xlsx","Sheet1")
lat=list(df["Latitude"])
long=list(df["Longitude"])
load=list(df["load"])
cord={(lat[i],long[i]):load[i] for i in range(len(lat))}

capicity=int(input("Enter capicity of vechicle :"))
cluster=ceil(sum(load)/capicity)
distance_matrix=[[geodesic(i,j) for i in cord] for j in cord]

count=0
centroid=[]
final_cluster={}
for i in cord:
    centroid.append(i)
    count+=1
    if(count==cluster):
        break
clusters={i:[] for i in centroid}
for i in cord:
    ref_dic={}
    centroid=list(clusters.keys())
    for j in centroid:
        ref_dic[float(geodesic(i,j).km)]=(i,j)
    l=list(sorted(ref_dic))
    ref_dic={i:ref_dic[i] for i in l}
    l1=ref_dic.values()
    for k in l1:
        ref_list=[cord[i] for i in clusters[k[1]]] 
        total=sum(ref_list)+cord[i]
        if(total<capicity):
            c=k[1]
            li=clusters[c]
            del clusters[c]
            newlat=(c[0]+i[0])/2
            newlong=(c[1]+i[1])/2
            clusters[(newlat,newlong)]=li
            clusters[(newlat,newlong)].append(i)
            break
# for i in clusters:
#     print(str(i)+" :"+str(clusters[i]))
a=1
cl={}
maxlen=max([len(clusters[i]) for i in clusters])

for i in clusters:
    cl["C"+str(a)]=[lat.index((j[0])) for j in clusters[i]]
    a+=1
for i in cl:
    l=[0 for i in range(maxlen-len(cl[i]))]
    cl[i]+=l
df1=pd.DataFrame(cl)
writer = pd.ExcelWriter('D:\\SY CS\\CAPSTONE\\Book3.xlsx', engine='xlsxwriter')
df1.to_excel(writer,"Sheet1",index_label=False)
writer.save()
for i in clusters:
    print(str(i)+" :"+str(clusters[i]))
    print('')
    print(" ")


        
        




