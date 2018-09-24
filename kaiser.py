def kaiser():

	import subprocess, sys, os, shutil, time

	print("""Welcome to Kaiser
		  [R] - Delete a file
		  [N] - New File
		  [X] - Exit
		  What would you like to do?""")

	while True:
		kaisernull = input("> ")

		if kaisernull == "R":
			delfile = input("Enter File Name ")
			print("Removed", file)
			os.remove(file)
	

		if kaisernull == "X":
			exit()

		else:
			kaiser()
kaiser()
