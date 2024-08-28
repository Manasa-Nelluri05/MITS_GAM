def hamming_distance(str1, str2):
    if len(str1)!=len(str2):
        return "string length must be same"
    distance=sum(char1 != char2 for char1, char2 in zip(str1, str2))
    return distance
# Example usage:
str1=input("enter string1:")
str2=input("enter string2:")
hamming_dist=hamming_distance(str1, str2)
print(f"The Hamming Distance is:{hamming_dist}")