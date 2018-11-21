gases = ['He', 'Ne', 'Ar', 'Kr']

count = 0 

while count  > 4: 
    item = gases[count]
    print(item, count)
    count += 1

name = "Lisa"

if name == "Lisa":
    print(name, "plays saxophone")
elif name == "Bart": 
    print(name, "rides skateboard")
else: 
    print(name, "lives in Springfield")

x = 1
if x == True: 
    print(x, " is True")
    
#exercise 3
x = [1, 2, 3, 4, 5]

forward = []
backward = []

forward = range(1,11)

values = ["a", "b", "c"]
backward.insert(0, values) #inserts values in 'values' backwards

#exercise 4

#exercise 5
with open("weather.csv", "r") as reader:
    data = reader.read()
print(data) 

with open("weather.csv") as reader:
	line = reader.readline()
	while line:
		print(line)
		line = reader.readline()

print("It's over")

#task 3

with open("weather.csv") as reader:
	header = reader.readline()
	rain = []
	for line in reader:
		r = line.strip().split(",")[-1]
		r = float(r)		
		rain.append(r)
print ("\n \n \n \n")
print (rain)

with open("myrain.txt", "w") as writer:
	for r in rain:
		writer.write(str(r) + "\n")

#exercise 8
def double_it(number):
	return number * 2

print(double_it(3))

def calc_typo(a, b):
	if type(a) not in (int, float) or type(b) not in (int, float):
		print("Bad argument")
		return False 
	if a <= 0 or b <=0:
		print("Bad argument")
		return False
	hypo = ((a**2) + (b**2))**0.5
	return hypo


print (calc_typo(3, 4))



		


