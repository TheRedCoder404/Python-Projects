height = int(input("This little Script builds you a little Christmas Tree depending on the height you specify.\nHow big should the tree be?: ")) + 1

print()
for i in range(height):
    if i == height - 1:
        print((height) * " " + "#" + (height) * " ")
    else:
        print((int(((height - i) * 2) / 2) * " ") + (((i * 2) + 1) * "+") + (int(((height - i) * 2) / 2) * " "))