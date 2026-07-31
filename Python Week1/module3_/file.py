# .csv = comma separated value
# .txt = text file

with open('message.txt','w') as file:
    file.write("I Love Python")
with open('message.txt','a') as file:
    file.write("I Love Python2")
with open('message.txt','a') as file:
    file.write("I Love Python3")


with open('message.txt','r') as file:
    text = file.read()
    print(text)