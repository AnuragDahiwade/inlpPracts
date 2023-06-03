
import re

def pattern1(text):
    pattern = "ab*";
    if re.search(pattern, text):
        print("Pattern Found")
    else:
        print("Not Found")

def pattern2(text):
    pattern = "ab{3}";
    if re.search(pattern, text):
        print("Pattern Found")
    else:
        print("Not Found")

def pattern3(text):
    pattern = "^[a-z]+_[a-z]+";
    if re.search(pattern, text):
        print("Pattern Found")
    else:
        print("Not Found")

def pattern4(text):
    pattern = "^[A-Z]{1}[a-z]+";
    if re.search(pattern, text):
        print("Pattern Found")
    else:
        print("Not Found")

def pattern5(text, list):
    for i in list:
        if re.search(i, text):
            print(i + " - Pattern Found")
        else:
            print(i + " - Not Found")

list = ["atom", "anu", "INLP"]
# text = input()
text = "Atom is here in the INLP lab. The examples of the input strings for this examples are abbb abbbb ab aabb etc. This is Practical_no 3"

print("Output for Q1: ")
pattern1(text)

print("\nOutput for Q2: ")
pattern2(text)

print("\nOutput for Q3: ")
pattern3(text)

print("\nOutput for Q4: ")
pattern4(text)

print("\nOutput for Q5: ")
pattern5(text, list)

