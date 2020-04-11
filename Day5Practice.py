#set
#they always hold unique values

s1 = {1,2,3,4,5}
type(s1)

s1 = {1,2,3,2,3,4}
print (s1)


list1 = [1,2,3,1,2,3,5,6,2]
set(list1)

str1 = "aaabbbccc"
set(str1)

s1[0] #indexing not allowed


s1 = {1, 2.3, 'Ram'}


s1 = {1,2,3,4}
s2 = {3,4,5,6}



#union
s1.union(s2)

#intersection
s1.intersection(s2)

#difference
s1.difference(s2)
s2.difference(s1)

s1.add(7)
s1.remove(7)

a1 = {'Ram', 'Shyam','Rahim','Anto'}
a2 = {'Ram', 'Anto', 'Rahul'}

a1.intersection(a2)

a1.difference(a2)
a2.difference(a1)



#dictionary
country = ['India', 'China', 'USA']

capital = ['Delhi', 'Beijing','DC']


country.index('China')

capital[1]

dict1 = {'India':'Delhi',
         "China":'Beijing',
         "USA":"DC"
         }

type(dict1)
len(dict1)


dict1.keys()
dict1.values()
dict1.items()

dict1['India']
dict1['China']


dict1['India'] = 'New Delhi'
dict1['India']

dict1['Russia'] = 'Moscow'


del dict1['USA']


#File Handling
#readng
#writing data to file

fp = open("words.txt",'r')
fp.read()
fp.close()

fp = open("words.txt", 'r')
print (fp.read())


#readline
fp  = open("words.txt",'r')
print (fp.readline())
print (fp.readline())


#readlines
fp  = open("words.txt",'r')
print (fp.readlines())


BANANA FRIES 12
POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30


dict1 = {"BANANA FRIES" : 12,
         "POTATO CHIPS": 60,
         "APPLE JUICE": 20,
         "CANDY":20,
         }


str1 = "BANANA FRIES 12"
list1 = str1.split()

value = int(list1[-1])

key = " ".join(list1[:-1])

dict1= {}
dict1[key] = value



#read
#readline
#readlines

fp = open("words.txt",'r')

print (fp.read())
fp.close()


fp = open("words.txt",'r')

print (fp.readline())
print (fp.readline())
fp.close()

fp = open("words.txt",'r')
fp.readlines()
fp.close()


fp = open("newstp.txt",'a')
fp.write("Hi from fine folks in Forsk"
)
fp.close()

#tuple relatd discussion

x, y, z = divmod(23, 5)


data = (x, y)

dict1[key] = dict1[key] + value
