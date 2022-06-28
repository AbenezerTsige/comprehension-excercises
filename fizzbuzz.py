lst = []
for i in range(100):
	if(i%3 == 0 and i%5 == 0):
		lst.append("FizzBuzz")
	elif(i%3 == 0):
		lst.append("Fizz")
	elif(i%5 == 0):
		lst.append("Buzz")
	else:
		pass

print(lst)

lst2 = [("FizzBuzz" if((i%3==0) and (i%5==0)) else("Fizz" if i%3==0 else ("Buzz" if i%5==0 else(str(i)) ))) for i in range(100)]
print(lst2)
