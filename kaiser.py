def kaiser():

	import subprocess, sys, os, shutil

	print("""
			-----Welcome to Kaiser-----
		  [D] - Delete a file
		  [M] - Move File
		  [N] - New File
		  [T] - See Current Directory
		  [TR] - See Tree of Directory
		  [X] - Exit""")
	while True:
		maininput = input("> ")

		if maininput == "D":
			delfile = input("Enter File Name to Delete ")
			print("Deleted", delfile)
			os.remove(delfile)

		if maininput == "M":
			mvfile = input("Enter File Name to Delete ")
			directory = input("Move {} Where?".format(mvfile))
			shutil.move(mvfile, directory)
			print("Moved {} to {}".format(mvfile,directory))

		if maininput == "N":
			newfile = input("Enter New File Name ")
			f= open(newfile,"w+")
			print("Created", newfile)

		if maininput == "T":
			dir_path = os.path.dirname(os.path.realpath(__file__))
			print(os.getcwd())

		if maininput == "TR":
			rootDir = input("What Directory would you like to see? ")
			#rootDir = os.path.dirname(os.path.realpath(__file__))
			for dirName, subdirList, fileList in os.walk(rootDir):
				print('%s' % dirName)
				for fname in fileList:
					print('\t%s' % fname)

		if maininput == "X":
			exit()


		else:
			kaiser()
kaiser()

