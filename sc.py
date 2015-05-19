#!/usr/bin/python
import sys
import os
import re
class Bad(Exception):pass

def fun(input1,high):
	den=[False for i in range(high)]
	num=[False for i in range(high)]
	v=[False for i in range(high)]
	a=[[False for i in range(high)] for j in range(high)]
	aT=[[False for i in range(high)] for j in range(high)]
	
	for i in range(len(input1)):
		a[input1[i][0]-1][input1[i][1]-1]=True
		aT[input1[i][1]-1][input1[i][0]-1]=True
	
	c=0
	
	for i in range(high):
		if v[i]==False:
			c+=1
			items=[]
			items.append(i)
			v[items[-1]]=True
			num[items[-1]]=c
			keepGoing=True
			while keepGoing:
				for j in range(high):
					if a[items[-1]][j]==True and v[j] != True:
						c+=1
						items.append(j)
						v[items[-1]]=True
						num[items[-1]]=c
						break
				else:
					c+=1
					den[items[-1]]=c
					tmp=items.pop()
					
					if items==[]:keepGoing=False
					
		
	den2=den
	den=tuple(den)
	den2.sort(reverse=True)			
	result1=[den.index(den2[i]) for i in range(len(den2))]
	v=[False for i in range(high)]
	result=0
	for i in range(len(result1)):
		if v[result1[i]]==False:
			#print "[ S C C ] : ",
			v[result1[i]]=True
			c=result1[i]
			result+=1
			#print c+1,
			keepGoing=True
			while keepGoing:
				for j in range(high):
					if aT[c][j]==True and v[j]!=True:
						v[j]=True
						c=j
						#print c+1,
						break
				else:
					keepGoing=False
					#print ""
	return result

def fun1():
	f=open(sys.argv[1],'r')
	result=[]
	high=0
	for l in f:
		tmp=re.split('\t+|\s+|\n+',l)
		if len(tmp)!=3:raise Bad()
		a,b=(int(tmp[0]),int(tmp[1]))
		if a>high:high=a
		if b>high:high=b
		result.append((a,b))
	if result==[]:raise Bad()	
	return (result,high)
if __name__ == '__main__':
	#input1=[(1,2),(1,6),(2,3),(2,6),(3,4),(3,7),(5,1),(6,5),(6,7),(7,3),(8,7)]
	try:
		result=fun1()
	except TypeError:
		print "file contain non numerical content"
		exit(1)
	except Bad:
		print "undefine format"
		exit(1)
	except:
		print "problem in reading file"
		exit(1)
	print fun(result[0],result[1])
	
	
