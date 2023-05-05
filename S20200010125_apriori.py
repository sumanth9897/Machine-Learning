from csv import reader
import sys

def load(filename):
    temp = list()
    with open(filename,'r') as file:
        csv = reader(file)
        for rox in csv:
            if not rox:
                continue
            for i in range(len(rox)):
                rox[i] = rox[i].lstrip(" ")
            rox.sort()
            temp.append(rox)
    return temp

def associt_rules(transac):
    Infer_Rules = []
    k = len(transac)
    for j in range(1,k):
        item_sets = []
        recfunction(item_sets,transac,[],0,j)
        for item in item_sets:
            Infer_Rules.append(item)
    return Infer_Rules


def recfunction(item_sets, it_ems, ki, indeex, g):
    if len(ki) == g:
        item_sets.append(ki)
    if indeex < len(it_ems) and len(ki) != g:
        temp_ki = ki.copy()
        ki.append(it_ems[indeex])
        recfunction(item_sets, it_ems, ki, indeex+1, g)
        recfunction(item_sets, it_ems, temp_ki, indeex+1, g)

def item_sets(transac,k):
    item_sets = []
    it_ems = set()
    for i in range(len(transac)):
        for j in range(len(transac[i])):
            it_ems.add(transac[i][j])
    it_ems = list(it_ems)
    it_ems.sort()
    if k == 1:
        for i in range(len(it_ems)):
            it_ems[i] = [it_ems[i]]
        return it_ems
    if len(it_ems) < k:
        return item_sets
    recfunction(item_sets,it_ems,[],0,k)
    return item_sets


    
def Gen_str_Associ_rules(Frequent_It_em_sets,Frequent_It_em_sets_count):
    str_Associ_rules = []
    for i in range(1,len(Frequent_It_em_sets)):
        for j in range(len(Frequent_It_em_sets[i])):
            transac = Frequent_It_em_sets[i][j]
            count = Frequent_It_em_sets_count[i][j]
            associationrules_list = associt_rules(transac)
            for associ_rule in associationrules_list:
                [p,q] = check_strassoci_rule(transac,associ_rule,Frequent_It_em_sets,Frequent_It_em_sets_count,count)
                if p == -1:
                    continue
                else:
                    str_Associ_rules.append([associ_rule,p,count,q])
    return str_Associ_rules



def frequent_itemsets(transac,itemsets,k,supp_count):
    supp_count *= len(transac)
    freq_Itemsets = []
    frequ = []
    for i in itemsets:
        count = 0
        for j in transac:
            temp = 0
            for z in range(k):
                if i[z] in j:
                    temp += 1
                else:
                    break
            if temp == k:
                count += 1
        if count >= supp_count:
            freq_Itemsets.append(i)
            frequ.append(count)
    return [freq_Itemsets,frequ]

def check_strassoci_rule(transa,associ_rule,Frequent_Item_sets,Frequent_Item_sets_count,n):
    a = len(associ_rule)
    if associ_rule in Frequent_Item_sets[a-1]:
        indeex = Frequent_Item_sets[a-1].index(associ_rule)
        arr = []
        for i in transa:
            if i in associ_rule:
                continue
            else:
                arr.append(i)
        if n/Frequent_Item_sets_count[a-1][indeex] >= sys.argv[2]:
            return [arr,Frequent_Item_sets_count[a-1][indeex]]
        else:
            return [-1,-1]
    else:
        return [-1,-1]

def print_str_associ_rules(str_associ_rules,n):
    for str_associ_rule in str_associ_rules:
        s1 = set(str_associ_rule[0])
        s2 = set(str_associ_rule[1])
        supp = round(str_associ_rule[2]/n,4)
        confi = round(str_associ_rule[2]/str_associ_rule[3],4)
        arr = [supp,confi]
        str_1 = str(s1)+str(s2)+str(arr)
        str_1 = str_1.replace("'","")
        str_1=str_1.replace(" ","")
        print(str_1)

sys.argv.pop(0)
sys.argv[1] = float(sys.argv[1])
sys.argv[2] = float(sys.argv[2])

data = load(sys.argv[0])
Frequent_Item_sets = []
Frequent_Item_sets_count = []
indeex = 1
while True:
    if len(Frequent_Item_sets) == 0:
        [x,y] = frequent_itemsets(data,item_sets(data,indeex),indeex,sys.argv[1])
        if len(x) == 0:
            break
        else:
            Frequent_Item_sets.append(x)
            
            Frequent_Item_sets_count.append(y)
    else:
        [x,y] = frequent_itemsets(data,item_sets(Frequent_Item_sets[len(Frequent_Item_sets)-1],indeex),indeex,sys.argv[1])
        if len(x) == 0:
            break
        else:
            Frequent_Item_sets.append(x)
            Frequent_Item_sets_count.append(y)
    indeex += 1

print_str_associ_rules(Gen_str_Associ_rules(Frequent_Item_sets,Frequent_Item_sets_count),len(data))