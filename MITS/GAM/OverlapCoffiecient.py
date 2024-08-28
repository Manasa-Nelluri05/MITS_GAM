def overlap_coefficient(str1,str2):
    set1=set(str1)
    set2=set(str2)
    intersection=len(set1.intersection(set2))
    smaller_set_size=min(len(set1), len(set2))
    overlap=intersection / smaller_set_size
    return overlap
str1=input("enter string1:")
str2=input("enter string2:")
overlap_coef=overlap_coefficient(str1, str2)
print(f"The Overlap Coefficient is: {overlap_coef:.2f}")