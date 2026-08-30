import re

#Checks whether the pattern matches only at the beginning of the string.
text = "python is easy"
res = re.match("python",text)
print(res)
print(res.group())

#Searches for the first occurrence of the pattern anywhere in the string.
text = "python is easy"
res = re.search("python",text)
print(res)
print(res.group())

#Returns all matches as a list.
text = "cat bat rat"
res = re.findall("at",text)
print(res)

#Returns an iterator of Match objects.
text = "cat bat rat"
res = re.finditer("at",text)
#print(res)re.finditer() does not return the matches immediately.
for i in res:
   print(i)

#To get the position of each match
text = "cat bat rat"
res = re.finditer("at",text)
for i in res:   
   print(i.group())

#To get the position of each match
text = "cat bat rat"
res = re.finditer("at",text)
for i in res:
    print(i.group(), i.start(), i.end())   


#Purpose: Replaces matched text.

text = "python is easy"
res = re.sub("python", "java", text)
print(res)


# re.splite() 

text = "apple,banana;,orange"

res = re.split("[,;]",text)
print(res)

#extract all numbers
text = "price: 120, Discount:15"
num  = re.findall(r"\d+", text)
print(num)

#validation an email

email = "bhavna.potphode@gmail.com"
pattern = r""