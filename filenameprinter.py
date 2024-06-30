import os

path = input()
txtfile = open("names.txt", "a")

for i in os.listdir(path):
    txtfile.write(f"\n{i}")

txtfile.close()
