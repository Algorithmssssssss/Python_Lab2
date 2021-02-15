""""
1 Write a program, which will combain two lists x and y into the one and sort the new list in ascending order.
 x = [1, 2, 3, 4, 5, 100, 200, 300, 1000]
 y = [100, 1000, 250, 200, 2, 2]
2 Write a program, which will find all numbers which divide by 7, but not divide by 5, from range 2000 - 4000. Print these digits to the screen.
3 Write a program, which asks to enter a number (n), then a program should generate a dictionary from 0 to n, which key is (i, i*2). Print the dictionary to the screen.
4 Write a program, which will perform a symbol replacement according to the rules described in the dictionary. Print the changed text to the screen.
 rules = {
     ".": "",
     ",": ".",
     "!": "?",
     "a": "A"
 }
5 Edit the third task. If the number from 2 to 4 will be entered, then ValueError should appear.

"""
x = [1, 2, 3, 4, 5, 100, 200, 300, 1000]
y = [100, 1000, 250, 200, 2, 2]

for n in y:
    x.append(n)

x.sort()
print(x)

number_list = []
for x in range(2000, 4000):
    if (x % 7 == 0) and not (x % 5 == 0):
        number_list .append(str(x))
print("Numbers divisible by 7 but not 5: ")
print(','.join(number_list))
print("A total of:", len(number_list), "numbers")


n = int(input("Input a number: "))
d = dict()
if n in range(2, 4):
    raise ValueError("You've entered a number in the range of 2 to 4")
else:
    for x in range(0, n):
        d[x+1] = ((x+1)*(x+1))
    print(d)


input = "the,quick.brown.fox jumps, over. the lazy.dog!"

print("The input character: ")
print(input)

input = input.replace(".", "")
input = input.replace(",", ".")
input = input.replace("!", "?")
input = input.replace("a", "A")
print(input)

