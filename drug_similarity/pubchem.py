#####################################################
#This is a script to download structures from PubChem
#based on their CAS numbers
####################################################
import urllib2
from bs4 import BeautifulSoup as BS
import requests as req     # requests and urllib2 do the same things. 
import re

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



####################################################
#Script for extracting info from PPTB Database
####################################################
html=urllib2.urlopen('http://sitem.herts.ac.uk/aeru/ppdb/en/atoz.htm')

soup=BS(html)

links=[]

for link in soup.find_all('a'):
    links.append(str(link.get('href')))

links=[s for s in links if "Reports/" in s]

CAS2=[]
for i in range(0,len(links)):
	try:
		html2=urllib2.urlopen('http://sitem.herts.ac.uk/aeru/ppdb/en/'+str(links[i]))
		soup2=BS(html2)
		temp2=[a.parent.next_sibling.next_sibling.get_text() for a in soup2.find_all('font') if a.string==u'             CAS RN        ']
		temp2=[str(x).strip() for x in temp2]
		CAS2=CAS2+temp2
	except UnicodeEncodeError:
		pass



#####################################################
#This is a script to download structures from PubChem
#based on their CAS numbers
####################################################
CAS_final=CASs+CAS2


data=[]
for i in range(0,len(CAS_final)):
	try:
		page = req.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/'+str(CASs[i])+'/cids/JSON')
		content = page.json()
		temp=content['IdentifierList']['CID']
		print temp
		data = data +temp
	except KeyError:
		pass
	#data=data+temp


#####################################################
#Fetching molecular properties from pubchem
#JSON structure file
####################################################
page=req.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/3672/record/JSON/?record_type=2d&response_type=display')

page=req.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/'+str(CID[i])+'/record/JSON/?record_type=2d&response_type=display')

content=page.json()

#E_complexity
content['PC_Compounds'][0]['props'][1]['value']['fval']

#HBA
content['PC_Compounds'][0]['props'][2]['value']['ival']

#HBD
content['PC_Compounds'][0]['props'][3]['value']['ival']

#Rotatable bonds
content['PC_Compounds'][0]['props'][4]['value']['ival']


