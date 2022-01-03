def main():
	import random
	import colorama
	from colorama import Fore, Style, init
	init(autoreset = True)
	random_num = [random.randint(1,100) for i in range(10)]
	moods = 0
	while True:
		if moods == 0:
			value = input("position?[q to quit]:")
		if moods == 1:
			print(Fore.YELLOW + Style.DIM + "give u a chance")
			value = input("what's the position?[q to quit]:")
		if moods == 2:
			print(Fore.YELLOW + Style.DIM + "... are u on purpose?")
			value = input("position!! :( [q to quit]:")
		if moods == 3 or moods == 4:
			print(Fore.YELLOW + Style.DIM + "I hate u (-∩-#)")
			value = input("position[q to quit]:")
		if moods == 5:
			import time
			print(Fore.RED + Style.DIM + "get out!!!")
			time.sleep(2)
			print(Fore.RED + Style.DIM + "I just ask u the position, but u r too full :)")
			time.sleep(2)
			break
		try:
			if value == "q":
				print("see u")
				break
			position = int(value)
			print(f"{random_num[position]} is in the position")
			moods = 0
		except IndexError as err:
			print(f"It is a bad position {position}")
			moods += 1
		except Exception as others:
			moods += 1
			print("someting wrong:", others)	
main()