import sys
args = sys.argv[1:]
with open( sys.argv[1],'r') as f:
	contents = f.readline()
list1 = contents.split(',')
with open('/home/ansible/ansible-patching/OSPatching/Suse/patchListSuse.csv','w+') as f2:
	for item in list1:
		f2.write("%s\n" %item)
