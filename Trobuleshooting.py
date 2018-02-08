import sys

import subprocess
output = subprocess.check_output("jps", shell=True)

f = open("/home/ayush/python/project/pyqt/Maintanance/a.xml","r")
contents = f.readlines()
f.close()
print "----------------------------------------------------------"
print "report of",sys.argv[1]
if("datanode" in output or "Datanode" in output):
	print "Datanode is in active state"
else:
	print "Datanode is in Down"
	open_count = 0
	close_count = 0
	terminator_count = 0
	count = 0
	line_count = 1
	lock=0
	end=999999
	#print output
	for j in contents:
		counter=0
		first = 0
		#print j
		if(j=="</configuration>" or j=="</configuration>\n" ):
			end=line_count
			#print "conf"
		if(1==1):
			for i in j:
				if(i=="<" and j[counter+1]=="?"):
					break
				if(i=="<" and j[counter+1]=="!" and j[counter+2]=="-" and j[counter+3]=="-"):
					count = 1
					#print "start"
				if(i=="-" and j[counter+1]=="-" and j[counter+2]==">"):
					count = 0
					#print "end"
					break
			
				if(count==0):	
					if(i=="<"):
						open_count = open_count + 1
						first = 1
					elif(i=='\n'):
						pass
					elif(first==0):
						print "Error in", line_count
						lock=1
						break
					
					if(i==">"):
						close_count = close_count + 1
					if(i=="/"):
						terminator_count = terminator_count + 1
						if(j[counter-1]!="<"):
							print "Error in",line_count
							lock=1
							break
					counter=counter+1
	
			
		line_count = line_count + 1
		if(line_count>end):
			if(j=="\n"):
				pass
			else:
				pass#print j
	
		
	#print open_count
	#print close_count
	#print terminator_count

	if (open_count!=close_count or open_count%2!=0 or close_count%2!=0):
		print "Error"
	elif (terminator_count!=(open_count/2)):
		print "Error"
	elif(end+2!=line_count):
		print "Error--Input should be inside <configuration> tag"
	elif(lock==0):
		print "Could not find problem contact vimal sir"

print "----------------------------------------------------------"
