from  geopy.distance import geodesic

def second_min(dic,l,minimal):
    l=list(sorted(l))
    sec_min=0
    just={ j for i in minimal for j in i}
    for i in range(1,len(l)):
        sec_min=l[i]
        for j in dic:
            if((sec_min==dic[j]) and (j not in minimal) and ((j[1],j[0])) not in minimal and not((j[0]  in just and j[1]  in just))):
                return j
def secondmin(dic,l):
    l=list(sorted(l))
    min=l[1]
    for i in dic:
        if(min==dic[i]):
            return i


def minimal_spanningtree(Cluster):
    distance_matrix = []
    ref_cluster={}
    minimal_tree=[]
    cord={Cluster[i]:(i+1) for i in range(len(Cluster))}
    for i in Cluster:
        l=[]
        for j in Cluster:
            l.append(geodesic(i,j).km)
            ref_cluster[(i,j)]=geodesic(i,j).km
        distance_matrix.append(l)
    minimal_tree.append(secondmin(ref_cluster,distance_matrix[0]))
    for z in range(len(distance_matrix)-2):
        for i in minimal_tree:
            count=0
            min=0
            minimumdist=0
            for j in i:
                l=[ref_cluster[k] for k in ref_cluster if k[0]==j]
                dic={k:ref_cluster[k] for k in ref_cluster if k[0]==j}
                if(count==0):
                    min=second_min(ref_cluster,l,minimal_tree)
                    minimumdist=geodesic(min[0],min[1])
                else:
                    ref=second_min(dic,l,minimal_tree)
                    ref_dist=geodesic(ref[0],ref[1])
                    if(minimumdist>ref_dist):
                        minimumdist=ref_dist
                        min=ref
                count+=1
        minimal_tree.append(min)
    print(minimal_tree)
    minimal_tree=[(cord[i[0]],cord[i[1]]) for i in minimal_tree]
    print(minimal_tree)






l=[(18.6733667, 73.7966341), (18.5878710821271, 73.7836724147201), (18.5877075931057, 73.7836188543588), (18.5297033333333, 73.8530983333333), (18.4565683333333, 73.8685866666667), (18.5715244850144, 73.7934413552284), (18.5646259272471, 73.8119371142238), (18.45263395, 73.90394725), (18.4557716666667, 73.8730166666667), (18.45194, 73.87405), (18.45066445, 73.91587958), (18.4411483333333, 73.86637), (18.45548412, 73.93276042), (18.46044005, 73.93371571), (18.4432483333333, 73.8812566666667), (18.44036252, 73.97479584), (18.4361716666667, 73.8954933333333), (18.4357666666667, 73.8939383333333)]
print(minimal_spanningtree(l))




