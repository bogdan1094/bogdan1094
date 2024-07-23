#Lists - unpacking
numbers = [1,2,3,4,5,6,7,8,9]
first, second, *others = numbers
print(first)
print(second)
print(others)

#enumerate
letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print (index,letter)

#sorting
list2=[3,6,8,2,34,22,32,123,23,34,56,44,17]
list2.sort(reverse=True)
print (list2)
print(sorted(list2)) #creates a  new separate list

#sorting function
items =[
     ("Product1", 20),
     ("Product2", 14),
     ("Product3", 45),
     ("Product4", 9),
 ]
def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)

# LAMBDA function
items.sort(key=lambda item:item[1])
print(items)

#MAP function
def price_list(list):
    prices = []
    for item in list:
        prices.append(item[1])
    return prices

print(price_list(items))
#using MAP function

def map_price_list(items):
    prices = list(map(lambda item:item[1], items))
    return prices

print(map_price_list(items))

#FILTER function

def filtered_list(items):
    filtered = list ((filter(lambda item:item[1] >=10, items)))
    return filtered

print (filtered_list(items))

# list comprehensions - preferable alternative to map and filter
new_items =[
    ("Product1", 20),
    ("Product2", 14),
    ("Product3", 45),
    ("Product4", 9),
]
new_prices = [item[1] for item in new_items]
print(new_prices)

new_filtered = [item for item in new_items if item[1] >=10]
print (new_filtered)

# ZIP function

list1 =[1,2,3,]
list2 = [10,20,30]

def zip_function(a,b,*c):
    zip_out = list(zip(a,b,*c))
    return zip_out

print(zip_function(list1,list2,"abcd", "bcd","asl","pls"))

#dictionary comprehension

dict = {x:x*2 for x in range(4)}
print(dict)

# Exercise - find the most repeated character in this sentence
from pprint import pprint
sentence = "This is a common interview question"
char_freq = {}
for char in sentence:
    if char in char_freq:
        char_freq[char] +=1
    else:
        char_freq[char] =1
pprint(char_freq, width=1)

sorted_char_freq_list = sorted(char_freq.items(), key=lambda kv:kv[1], reverse=True)
print(sorted_char_freq_list)
print(f"The most repeated letter in the sentence is {sorted_char_freq_list[0]}")