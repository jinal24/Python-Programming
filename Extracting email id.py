import re
count=0
pattern_emailid_extraction=re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-z]+')
print("----------------------------------------")
with open('extract_number.txt','r') as f:
    email_id=f.read()
    matches=pattern_emailid_extraction.findall(email_id)
    for i in matches:
        count=count+1
        print(i)
print("----------------------------------------")
print("Text file contains total %s emails"%count)