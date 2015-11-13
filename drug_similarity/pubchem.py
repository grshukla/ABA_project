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
CAS_final=set(CAS_final)
CAS_final=list(CAS_final)



data=[]
for i in range(0,len(CAS_final)):
	try:
		page = req.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/'+str(CAS_final[i])+'/cids/JSON')
		content = page.json()
		temp=content['IdentifierList']['CID']
		print temp[0]
		data.append(temp[0])
	except KeyError:
		pass
	#data=data+temp


#####################################################
#Fetching molecular properties from pubchem
#JSON structure file
####################################################
#page=req.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/3672/record/JSON/?record_type=2d&response_type=display')
for i in range(0,len(data)):
	page=req.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/'+str(data[i])+'/record/JSON/?record_type=2d&response_type=display')
	content=page.json()
	#E_complexity
	content['PC_Compounds'][0]['props'][1]['value']['fval']
	#HBA
	content['PC_Compounds'][0]['props'][2]['value']['ival']
	#HBD
	content['PC_Compounds'][0]['props'][3]['value']['ival']
	#Rotatable bonds
	content['PC_Compounds'][0]['props'][4]['value']['ival']
	#InChI
	content['PC_Compounds'][0]['props'][11]['value']['sval']
	#Log(P)
	content['PC_Compounds'][0]['props'][13]['value']['fval']
	#Mass
	content['PC_Compounds'][0]['props'][14]['value']['fval']
	#Molecular Formula 
	content['PC_Compounds'][0]['props'][15]['value']['sval']
	#Simles (Canonical)
	content['PC_Compounds'][0]['props'][17]['value']['sval']
	#Smiles (Isomeric)
	content['PC_Compounds'][0]['props'][18]['value']['sval']
	#Polar surface area
	content['PC_Compounds'][0]['props'][19]['value']['fval']
	#Heavy atom Count
	content['PC_Compounds'][0]['count']['heavy_atom']
	#chiral Atom
	content['PC_Compounds'][0]['count']['atom_chiral']
	#number of tautomers 
	content['PC_Compounds'][0]['count']['tautomers']



key_error=[]
for i in range(0,len(data)):
	try:
        	page=req.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/'+str(data[i])+'/record/JSON/?record_type=2d&response_type=display')
        	content=page.json()
		prop_matrix[i,0]=content['PC_Compounds'][0]['props'][14]['value']['fval']  #MW
		prop_matrix[i,1]=content['PC_Compounds'][0]['props'][13]['value']['fval']  #Log(P)
		prop_matrix[i,2]=content['PC_Compounds'][0]['props'][3]['value']['ival']   #HBD
		prop_matrix[i,3]=content['PC_Compounds'][0]['props'][2]['value']['ival']  #HBA
		prop_matrix[i,4]=content['PC_Compounds'][0]['props'][19]['value']['fval']  #ROTB
		prop_matrix[i,5]=content['PC_Compounds'][0]['props'][4]['value']['ival']  #PSA
	except KeyError:
		#key_error=key_error.append(i)
		print "Key error in %r" %i
		pass
	except IndexError:
		pass

prop_matrix=prop_matrix[~np.all(prop_matrix == 0, axis=1)]




#########Downloading Smile strings########################
smiles=[]
for i in range(0,len(data)):
        try:
                page=req.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/'+str(data[i])+'/record/JSON/?record_type=2d&response_type=display')
                content=page.json()
		smiles.append(str(content['PC_Compounds'][0]['props'][17]['value']['sval']))
	except KeyError:
		pass
	except IndexError:
		pass

g=open('smiles.pkl','wb')
pkl.dump(smiles,g)
g.close()


################# Properties from Smile ####################
from rdkit import Chem
from rdkit.Chem import Descriptors

ar_rings=[]
al_rings=[]
hv_atoms=[]
mw_hv_atoms=[]
ht_atoms=[]
val_elec=[]
rings=[]
sp3_c=[]


for i in range(0,len(smiles)):
	try:
		m = Chem.MolFromSmiles(smiles[i])
		ar_rings.append(Descriptors.NumAromaticRings(m))
		al_rings.append(Descriptors.NumAliphaticRings(m))
		hv_atoms.append(Descriptors.HeavyAtomCount(m))	
		mw_hv_atoms.append(Descriptors.HeavyAtomMolWt(m))
		ht_atoms.append(Descriptors.NumHeteroatoms(m))
		val_elec.append(Descriptors.NumValenceElectrons(m))
		rings.append(Descriptors.RingCount(m))
		sp3_c.append(Descriptors.FractionCSP3(m))
		print i
	except BaseException:
		pass


smiles_matrix=np.zeros((4480,8))
smiles_matrix[:,0]=np.array(ar_rings)
smiles_matrix[:,2]=np.array(hv_atoms)
smiles_matrix[:,3]=np.array(mw_hv_atoms)
smiles_matrix[:,4]=np.array(ht_atoms)
smiles_matrix[:,5]=np.array(val_elec)
smiles_matrix[:,6]=np.array(rings)
smiles_matrix[:,7]=np.array(sp3_c)


import pickle
f = open('smiles_matrix.pkl','wb')
pickle.dump(smiles_matrix,f)
f.close()

