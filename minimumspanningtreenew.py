from  geopy.distance import geodesic
def secondmin(dic,ref_dic):
    dist=list(sorted(dic.values()))
    for i in dic:
        if dic[i]==dist[1]:
            return i
def second_min(dic,ref_dic,minimal):
    ref_set={j for i in minimal for j in i}
    minimum_spanning=[]
    # ref_set={i for i in ref_dic if ref_dic[i] in ref_set}
    dist_dic={k for i in ref_set for k in dic if k[0]==i}
    dist_dic={k:geodesic(k[0],k[1]).km for k in dist_dic}
    sorted_values = sorted(dist_dic.values())  # Sort the values
    sorted_dict = {}
    for i in sorted_values:
        for k in dist_dic.keys():
            if dist_dic[k] == i:
                sorted_dict[k] = dist_dic[k]
    min=0
    ref=0
    for i in sorted_dict:
        if i[0]!=i[1] and i not in minimal and  i[1] not in ref_set:
            return i



def minimum_spanning_tree(cluster):
    # print(len(cluster))
    minimal_spanning=[]
    ref_dic={cluster[i]:(i+1) for i in range(len(cluster))}
    dist_dic={(cluster[0],cluster[i]):geodesic(cluster[0],cluster[i]).km for i in range(0,len(cluster))}
    minimal_spanning.append(secondmin(dist_dic,ref_dic))
    dist_dic={(i,j):geodesic(i,j).km for i in cluster for j in cluster}
    # print(minimal_spanning)
    for i in range(len(cluster)-2):
        minimal_spanning.append(second_min(dist_dic, ref_dic, minimal_spanning))
    minimal_spanning=[(ref_dic[i[0]],ref_dic[i[1]]) for i in minimal_spanning]
    print(minimal_spanning)




cluster=[(18.62340716, 73.85221254), (18.5878710821271, 73.7836724147201), (18.5877075931057, 73.7836188543588), (18.5715244850144, 73.7934413552284), (18.5646259272471, 73.8119371142238), (18.45194, 73.87405), (18.5860693, 73.8148318), (18.5841183, 73.823099), (18.4411483333333, 73.86637), (18.45548412, 73.93276042), (18.46044005, 73.93371571), (18.4432483333333, 73.8812566666667), (18.44036252, 73.97479584), (18.4361716666667, 73.8954933333333), (18.4357666666667, 73.8939383333333), (18.4562283333333, 73.8880466666667), (18.48725911, 73.94214004)]

minimum_spanning_tree(cluster)