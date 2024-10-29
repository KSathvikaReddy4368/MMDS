count = 0
f = open("sample3.txt", "r") 
for line in f:  
    word = line.split(" ") 
    count += len(word) 
print("Total Number of Words: " + str(count)) 
f.close() 
text = open("sample3.txt", "r") 
d = dict() 
for line in text:  
    line = line.strip() 
    line = line.lower() 
    words = line.split(" ") 
    for word in words: 
        if word in d: 
            d[word] = d[word] + 1
        else: 
            d[word] = 1
for key in list(d.keys()):
    #if d[key]>1:
        print(key, ":", d[key])
