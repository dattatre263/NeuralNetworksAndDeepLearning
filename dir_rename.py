import os, sys

def recursiveClean(dirPath):
	for dirName in os.listdir(dirPath):
		if dirName.startswith("."):
			continue
		if os.path.isdir(os.path.join(dirPath, dirName)):
			recursiveClean(os.path.join(dirPath, dirName))
		os.rename(os.path.join(dirPath, dirName), os.path.join(dirPath, dirName.replace(r'[ :]', '')))

if len(sys.argv) < 2:
	print("Usage: dir_rename.py path/to/directories/to/rename")
	sys.exit(2)
else:
	dirPath = sys.argv[1]
	recursiveClean(dirPath)
	sys.exit(0)



	
