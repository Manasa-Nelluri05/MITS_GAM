def jaccard_coefficient(str1, str2):
    set1=set(str1)
    set2=set(str2)
    intersection=len(set1.intersection(set2))
    union=len(set1.union(set2))
    jaccard=intersection / union
    return jaccard
str1=input("enter str1:")
str2=input("enter str2:")
jaccard_index=jaccard_coefficient(str1,str2)
print(f"The Jaccard Coefficient is:{jaccard_index:.2f}")

