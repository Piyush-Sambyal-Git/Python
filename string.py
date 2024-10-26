# string 
# type: ignore defination- all things that we mention in ' '/" "/""" """ are strings 
# in single quotes ('') we cannot use 's rest is same
# triple quotes for multiple lines


st="hello ron there is a problem in my computer can you help me"
# len() calculates the length of string 
print(len(st))

# .count-> countes no. of time a letter/ word repeats in String 
print(st.count("e"))

#.upper()-> it converts the lowercase into uppercase
print(st.upper())

#.lower()-> it converts the uppercase into lowercase
print(st.lower())

#.capitalize()->convert 1st letter of string to uppercase
print(st.capitalize())

#.title()-> convert lowercase of each word to uppercase
print(st.title())

#.replace("old_string","new_string")
print(st.replace("hello","bye"))

word="hello how are you, hello I am fine"
print(word.replace("hello","hi",1)) #writinng 1 will replace only the first hello

#.split-> splits sentence from the word/letter specified by user. By default it splits using spaces
print(st.split("problem"))

name="    rushil    "
print(name)

print(name.lstrip()) #removes left side spaces
print(name.rstrip()) #removes right side spaces
print(name.strip())  #removes both side spaces

# .removeprefix-> it removes the staring word of the string 
print(st.removeprefix("hello"))
# .removesuffix-> it removes the last word of the string 
print(st.removesuffix("me"))
#.find-> it gives index of 1st letter of given word
print(st.find("in"))
print(word.find("hello",1)) #comma 1 means 1 index ke baad jo hello aayega uski baat ho rahi

#slicing-> string_name[start:stop:step]
w="0123456789"
print(w[1:6]) #prints from index 1 till 6 excluding 6
print(w[0:])
print(w[:10])
print(w[0:10:2]) #step means skip by 2
print(w[::3])    #starts from 0 till end index but with a gap of 3

#problem
print(st.find("computer"))
print(st.find("me"))

print(st[35:59])

print(st.replace("problem","solution"))
