#####################################################
#This is a script to download structures from PubChem
#based on their CAS numbers
####################################################
import urllib2
from bs4 import BeautifulSoup as BS
import requests as req     # requests and urllib2 do the same things. 


####################################################
#Script for extracting info from a html table
####################################################

#Database contains multiple tables based on intial letter of drug. Making an array
alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)] #List of elements from A to Z
numbers=[str(i) for i in range(1,10)]                      # List of numbers from 1 to 9
page_index= alphabet + numbers   #Array of alphabets and numerals 

CASs=[]

#Opening the URL by URLLIB2 and imporitng it to brautifulsoup
for i in range(0, len(page_index)):
	html=urllib2.urlopen('http://www.pesticideinfo.org/List_ChemicalsAlpha.jsp?ChemName='+page_index[i])
	soup = BS(html)

#Reading CAS numbers from the HTML table in the webpage. 
	CAS=[]
	for i in range(2,1000):
        	try:
                	temp=soup.contents[1].contents[1].contents[5].contents[2*i-1].contents[1].renderContents()
                	CAS.append(temp)
        	except IndexError:
                	break

	CAS = filter(None,CAS)                 #For deleting empty columns of lists
	CAS =[x for x in CAS if "," not in x]  # Deleting entries having multiple CAS numbers
	CASs=CASs + CAS                        


   # ######################################################################
  #CASs contain the CAS numbers of the compounds in the PAN database #####
 ## "http://www.pesticideinfo.org/List_ChemicalsAlpha.jsp?ChemName=A"####
########################################################################



#####################################################
#This is a script to download structures from PubChem
#based on their CAS numbers
####################################################

data=[]
for i in range(0,len(CASs)):
	try:
		page = req.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/'+str(CASs[i])+'/cids/JSON')
		content = page.json()
		temp=content['IdentifierList']['CID']
		print temp
		data = data +temp
	except KeyError:
		pass
	#data=data+temp
