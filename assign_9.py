#!/usr/bin/python                         
import re 							#importing re module for regular expression
ahappy=0							#defining variables 																											
acrook=0
asurprised=0
aneutral=0
asarcastic=0
asad=0
aangry=0
bhappy=0
bcrook=0
bsurprised=0
bneutral=0
bsarcastic=0
bsad=0
bangry=0
chappy=0
ccrook=0
csurprised=0
cneutral=0
csarcastic=0
csad=0
cangry=0
ehappy=0
ecrook=0
esurprised=0
eneutral=0
esarcastic=0
esad=0
eangry=0
ghappy=0
gcrook=0
gsurprised=0
gneutral=0
gsarcastic=0
gsad=0
gangry=0
fw=open("output.txt","w")
fh= open("content.txt","r")						#file opening in read mode
while 1:								#while loop until it is true
	line = fh.readline()						#reading file by line wise
	c= line[:1]							#reading first character of read line
	if c=="A":							#if condition, whether it is A,B,C,E or G.
		
		searchObj = re.search( r':[)]', line, re.M|re.I)	#search for expression :)
		if searchObj:
			
			ahappy=ahappy+1					#if happy, increament happy counter of A by 1
			fw.write("A:Happy\n")
		searchObj = re.search( r':P', line, re.M|re.I)		#search for expression :)
		if searchObj:
			
			asarcastic=asarcastic+1				#if sarcastic, increament sarcastic counter of A by 1
			fw.write("A:Sarcastic\n")
		searchObj = re.search( r':[(]', line, re.M|re.I)	#search for expression :)
		if searchObj:
			
			asad=asad+1					#if sad, increament sad counter of A by 1
			fw.write("A:Sad\n")
		searchObj = re.search( r':-o', line, re.M|re.I)		#search for expression :)
		if searchObj:
		
			asurprised=asurprised+1				#if surprised, increament surprised counter of A by 1
			fw.write("A:Surprised\n")
		searchObj = re.search( r'B-[)]', line, re.M|re.I)	#search for expression :)
		if searchObj:
		
			acrook=acrook+1					#if crook, increament crook counter of A by 1
			fw.write("A:Crook\n")
		searchObj = re.search( r':-/', line, re.M|re.I)		#search for expression :)
		if searchObj:
			
			aneutarl=aneutral+1				#if neutral, increament neutral counter of A by 1
			fw.write("A:Neutral\n")
		searchObj = re.search( r'x-[(]', line, re.M|re.I)	#search for expression :)
		if searchObj:
		
			aangry=aangry+1					#if angry, increament angry counter of A by 1
			fw.write("A:Angry\n")
		searchObj = re.search( r':D', line, re.M|re.I)		#search for expression :)
		if searchObj:
			
			ahappy=ahappy+1					#if happy, increament happy counter of A by 1
			fw.write("A:Happy\n")
		searchObj = re.search( r';[)];[)]', line, re.M|re.I)	#search for expression :)
		if searchObj:
		
			asarcastic=asarcastic+1				#if sarcastic, increament sarcastic counter of A by 1
			fw.write("A:Sarcastic\n")
		searchObj = re.search( r'O_O', line, re.M|re.I)		#search for expression :)
		if searchObj:
		
			asurprised=asurprised+1				#if surprised, increament surprised counter of A by 1
			fw.write("A:Surprised\n")
		searchObj = re.search( r';[)]', line, re.M|re.I)	#search for expression :)
		if searchObj:
		
			acrook=acrook+1					#if crook, increament crook counter of A by 1
			fw.write("A:Crook\n")
		searchObj = re.search( r'=_=', line, re.M|re.I)		#search for expression :)
		if searchObj:
		
			aneutral=aneutarl+1				#if neutarl, increament neutarl counter of A by 1
			fw.write("A:neutral\n")
		searchObj = re.search( r'>_<', line, re.M|re.I)		#search for expression :)
		if searchObj:
			fw.write("A:Angry\n")
			aangry=aangry+1					#if angry, increament angry counter of A by 1	
	if c=="B":							#if condition, whether it is A,B,C,E or G.
		
		searchObj = re.search( r':[)]', line, re.M|re.I)	#search for expression :)
		if searchObj:
			fw.write("B:Happy\n")
			bhappy=bhappy+1					#if happy, increament happy counter of B by 1
		
		searchObj = re.search( r':P', line, re.M|re.I)		#search for expression :)
		if searchObj:
			fw.write("B:Sarcastic\n")
			bsarcastic=bsarcastic+1				#if happy, increament happy counter of B by 1
	
		searchObj = re.search( r':[(]', line, re.M|re.I)	#search for expression :)
		if searchObj:
			
			bsad=bsad+1					#if happy, increament happy counter of B by 1
			fw.write("B:Sad\n")
		searchObj = re.search( r':-o', line, re.M|re.I)		#search for expression :)
		if searchObj:
		
			bsurprised=bsurprised+1				#if happy, increament happy counter of B by 1
			fw.write("B:Surprised\n")
		searchObj = re.search( r'B-[)]', line, re.M|re.I)	#search for expression :)
		if searchObj:
		
			bcrook=bcrook+1					#if happy, increament happy counter of B by 1
			fw.write("B:Crook\n")
		searchObj = re.search( r':-/', line, re.M|re.I)		#search for expression :)
		if searchObj:
			
			bneutarl=bneutral+1				#if happy, increament happy counter of B by 1
			fw.write("B:Neutral\n")
		searchObj = re.search( r'x-[(]', line, re.M|re.I)	#search for expression :)
		if searchObj:
		
			bangry=bangry+1					#if happy, increament happy counter of B by 1
			fw.write("B:Angry\n")
		searchObj = re.search( r':D', line, re.M|re.I)
		if searchObj:
			
			bhappy=bhappy+1
			fw.write("B:Happy\n")
		searchObj = re.search( r';[)];[)]', line, re.M|re.I)
		if searchObj:
			fw.write("B:Sarcastic\n")
			bsarcastic=bsarcastic+1
		
		searchObj = re.search( r'O_O', line, re.M|re.I)
		if searchObj:
			fw.write("B:Surprised\n")
			bsurprised=bsurprised+1
		
		searchObj = re.search( r';[)]', line, re.M|re.I)
		if searchObj:
			fw.write("B:Crook\n")
			bcrook=bcrook+1
		
		searchObj = re.search( r'=_=', line, re.M|re.I)
		if searchObj:
			fw.write("B:neutral\n")
			bneutral=bneutarl+1
		
		searchObj = re.search( r'>_<', line, re.M|re.I)
		if searchObj:
			fw.write("B:Angry\n")
			bangry=bangry+1		
	if c=="C":								#if condition, whether it is A,B,C,E or G.
		
		searchObj = re.search( r':[)]', line, re.M|re.I)
		if searchObj:
			
			chappy=chappy+1
			fw.write("C:Happy\n")
		searchObj = re.search( r':P', line, re.M|re.I)
		if searchObj:
			
			csarcastic=csarcastic+1
			fw.write("C:Sarcastic\n")
		searchObj = re.search( r':[(]', line, re.M|re.I)
		if searchObj:
			
			csad=csad+1
			fw.write("C:Sad\n")
		searchObj = re.search( r':-o', line, re.M|re.I)
		if searchObj:
		
			csurprised=csurprised+1
			fw.write("C:Surprised\n")
		searchObj = re.search( r'B-[)]', line, re.M|re.I)
		if searchObj:
		
			ccrook=ccrook+1
			fw.write("C:Crook\n")
		searchObj = re.search( r':-/', line, re.M|re.I)
		if searchObj:
			
			cneutarl=cneutral+1
			fw.write("C:Neutral\n")
		searchObj = re.search( r'x-[(]', line, re.M|re.I)
		if searchObj:
		
			cangry=cangry+1
			fw.write("C:Angry\n")
		searchObj = re.search( r':D', line, re.M|re.I)
		if searchObj:
			
			chappy=chappy+1
			fw.write("C:Happy\n")
		searchObj = re.search( r';[)];[)]', line, re.M|re.I)
		if searchObj:
		
			csarcastic=csarcastic+1
			fw.write("C:Sarcastic\n")
		searchObj = re.search( r'O_O', line, re.M|re.I)
		if searchObj:
		
			csurprised=csurprised+1
			fw.write("C:Surprised\n")
		searchObj = re.search( r';[)]', line, re.M|re.I)
		if searchObj:
		
			ccrook=ccrook+1
			fw.write("C:Crook\n")
		searchObj = re.search( r'=_=', line, re.M|re.I)
		if searchObj:
		
			cneutral=cneutarl+1
			fw.write("C:Neutral\n")
		searchObj = re.search( r'>_<', line, re.M|re.I)
		if searchObj:
			fw.write("C:Angry\n")
			cangry=cangry+1		
	if c=="E":								#if condition, whether it is A,B,C,E or G.
		
		searchObj = re.search( r':[)]', line, re.M|re.I)
		if searchObj:
			
			ehappy=ehappy+1
			fw.write("E:Happy\n")
		searchObj = re.search( r':P', line, re.M|re.I)
		if searchObj:
			
			esarcastic=esarcastic+1
			fw.write("E:Sarcastic\n")
		searchObj = re.search( r':[(]', line, re.M|re.I)
		if searchObj:
			
			esad=esad+1
			fw.write("E:Sad\n")
		searchObj = re.search( r':-o', line, re.M|re.I)
		if searchObj:
		
			esurprised=esurprised+1
			fw.write("E:Surprised\n")
		searchObj = re.search( r'B-[)]', line, re.M|re.I)
		if searchObj:
		
			ecrook=ecrook+1
			fw.write("E:Crook\n")
		searchObj = re.search( r':-/', line, re.M|re.I)
		if searchObj:
			
			eneutarl=eneutral+1
			fw.write("E:Neutral\n")
		searchObj = re.search( r'x-[(]', line, re.M|re.I)
		if searchObj:
		
			eangry=eangry+1
			fw.write("E:Angry\n")
		searchObj = re.search( r':D', line, re.M|re.I)
		if searchObj:
			
			ehappy=ehappy+1
			fw.write("E:Happy\n")
		searchObj = re.search( r';[)];[)]', line, re.M|re.I)
		if searchObj:
		
			esarcastic=esarcastic+1
			fw.write("E:Sarcastic\n")
		searchObj = re.search( r'O_O', line, re.M|re.I)
		if searchObj:
		
			esurprised=esurprised+1
			fw.write("E:Surprised\n")
		searchObj = re.search( r';[)]', line, re.M|re.I)
		if searchObj:
		
			ecrook=ecrook+1
			fw.write("E:Crook\n")
		searchObj = re.search( r'=_=', line, re.M|re.I)
		if searchObj:
		
			eneutral=eneutarl+1
			fw.write("E:Neutral\n")
		searchObj = re.search( r'>_<', line, re.M|re.I)
		if searchObj:
			fw.write("E:Angry\n")
			eangry=eangry+1		
	if c=="G":									#if condition, whether it is A,B,C,E or G.
		
		searchObj = re.search( r':[)]', line, re.M|re.I)
		if searchObj:
			fw.write("G:Happy\n")
			ghappy=ghappy+1
		
		searchObj = re.search( r':P', line, re.M|re.I)
		if searchObj:
			
			gsarcastic=gsarcastic+1
			fw.write("G:Sarcastic\n")
		searchObj = re.search( r':[(]', line, re.M|re.I)
		if searchObj:
			
			gsad=gsad+1
			fw.write("G:Sad\n")
		searchObj = re.search( r':-o', line, re.M|re.I)
		if searchObj:
		
			gsurprised=gsurprised+1
			fw.write("G:Surprised\n")
		searchObj = re.search( r'B-[)]', line, re.M|re.I)
		if searchObj:
		
			gcrook=gcrook+1
			fw.write("G:Crook\n")
		searchObj = re.search( r':-/', line, re.M|re.I)
		if searchObj:
			
			gneutarl=gneutral+1
			fw.write("G:Neutral\n")
		searchObj = re.search( r'x-[(]', line, re.M|re.I)
		if searchObj:
		
			gangry=gangry+1
			fw.write("G:Angry\n")
		searchObj = re.search( r':D', line, re.M|re.I)
		if searchObj:
			
			ghappy=ghappy+1
			fw.write("G:Happy\n")
		searchObj = re.search( r';[)];[)]', line, re.M|re.I)
		if searchObj:
		
			gsarcastic=gsarcastic+1
			fw.write("G:Sarcastic\n")
		searchObj = re.search( r'O_O', line, re.M|re.I)
		if searchObj:
		
			gsurprised=gsurprised+1
			fw.write("G:Surprised\n")
		searchObj = re.search( r';[)]', line, re.M|re.I)
		if searchObj:
		
			gcrook=gcrook+1
			fw.write("G:Crook\n")
		searchObj = re.search( r'=_=', line, re.M|re.I)
		if searchObj:
		
			gneutral=gneutarl+1
			fw.write("G:Neutral\n")
		searchObj = re.search( r'>_<', line, re.M|re.I)
		if searchObj:
			
			gangry=gangry+1		
			fw.write("G:Angry\n")
		
		

	
	if not line:
 	      break								#if line overs, break the loop


atotal=0
atotal=ahappy+acrook+asurprised+aneutral+asarcastic+asad+aangry			#calculating the total of A's expression
print"percentage of happy mood of A",(ahappy*100.0)/atotal
print "percentage of sad mood of A",(asad*100.0)/atotal
print "percentage of Sarcastic mood of A",(asarcastic*100.0)/atotal
print "percentage of Neutral mood of A",(aneutral*100.0)/atotal
print "percentage of angry mood of A",(aangry*100.0)/atotal
print "percentage of Surprised mood of A",(asurprised*100.0)/atotal
print "percentage of Crook mood of A",(acrook*100.0)/atotal
btotal=0
btotal=bhappy+bcrook+bsurprised+bneutral+bsarcastic+bsad+bangry			#calculating the total of B's expression
print "percentage of happy mood of B",(bhappy*100.0)/btotal
print "percentage of sad mood of b",(bsad*100.0)/btotal
print "percentage of Sarcastic mood of b",(bsarcastic*100.0)/btotal
print "percentage of Neutral mood of b",(bneutral*100.0)/btotal
print "percentage of angry mood of B",(bangry*100.0)/btotal
print "percentage of Surprised mood of B",(bsurprised*100.0)/btotal
print "percentage of Crook mood of B",(bcrook*100.0)/btotal
ctotal=0
ctotal=chappy+ccrook+csurprised+cneutral+csarcastic+csad+cangry			#calculating the total of C's expression
print "percentage of happy mood of C",(chappy*100.0)/ctotal
print "percentage of sad mood of C",(csad*100.0)/ctotal
print "percentage of Sarcastic mood of C",(csarcastic*100.0)/ctotal
print "percentage of Neutral mood of C",(cneutral*100.0)/ctotal
print "percentage of angry mood of C",(cangry*100.0)/ctotal
print "percentage of Surprised mood of C",(csurprised*100.0)/ctotal
print "percentage of Crook mood of C",(ccrook*100.0)/ctotal
etotal=0
etotal=ehappy+ecrook+esurprised+eneutral+esarcastic+esad+eangry			#calculating the total of E's expression
print "percentage of happy mood of E",(ehappy*100.0)/etotal
print "percentage of sad mood of E",(esad*100.0)/etotal
print "percentage of Sarcastic mood of E",(esarcastic*100.0)/etotal
print "percentage of Neutral mood of E",(eneutral*100.0)/etotal
print "percentage of angry mood of E",(eangry*100.0)/etotal
print "percentage of Surprised mood of e",(esurprised*100.0)/etotal
print "percentage of Crook mood of E",(ecrook*100.0)/etotal
gtotal=0
gtotal=ghappy+gcrook+gsurprised+gneutral+gsarcastic+gsad+gangry			#calculating the total of G's expression
print "percentage of happy mood of G",(ghappy*100.0)/gtotal
print "percentage of sad mood of G",(gsad*100.0)/gtotal
print "percentage of Sarcastic mood of G",(gsarcastic*100.0)/atotal
print "percentage of Neutral mood of G",(gneutral*100.0)/gtotal
print "percentage of angry mood of G",(gangry*100.0)/gtotal
print "percentage of Surprised mood of G",(gsurprised*100.0)/gtotal
print "percentage of Crook mood of G",(gcrook*100.0)/gtotal




