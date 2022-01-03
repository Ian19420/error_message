def main():
	import random
	random_num = [random.randint(1,100) for i in range(10)]
	while True:
		value = input("position[q to quit]:")
		if value == "q":
			print("see u")
			break
		try:
			position = int(value)
			print(f"{random_num[position]} is in the position, what else?", end = "\t")
		except IndexError as err:
			print(f"It is a bad position {position}, input again?", end = "\t")
		except Exception as others:
			print("someting wrong:", others, "input again?", end = "\t")	

main()