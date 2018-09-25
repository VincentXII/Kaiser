def kaiser():

	import subprocess, sys, os, shutil

	print("""
			-----Welcome to Kaiser-----
		  [D] - Delete a file
		  [N] - New File
		  [X] - Exit""")
	while True:
		maininput = input("> ")

		if maininput == "D":
			delfile = input("Enter File Name to Delete ")
			print("Deleted", delfile)
			os.remove(delfile)

		if maininput == "N":
			newfile = input("Enter New File Name ")
			f= open(newfile,"w+")
			print("Created", newfile)

		if maininput == "X":
			exit()



		else:
			kaiser()
kaiser()

