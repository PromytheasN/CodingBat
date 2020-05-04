def cat_dog(str3):
    count_cat = 0
    count_dog = 0
    for i in range(0,len(str3)):
        if str3[i:i+3] == "cat":
            count_cat +=1
        if str3[i:i+3] == "dog":
            count_dog += 1
    if count_dog == count_cat:
    
    return count_cat == count_dog
