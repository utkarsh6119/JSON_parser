import json
from collections import OrderedDict

# This is the input string which is to be parsed and convert to JSON format.

inp="profile|73241234|<Niharika><><Khan>|<Mumbai><<72.872075><19.075606>>|73241234.jpg**followers|54543343|<Amitabh><><>|<Dehradun><<><>>|54543343.jpg@@|22112211|<Piyush><><>||"
# inp="profile|73241232|<Aamir><><Khan>|<Mumbai><<72.872075><19.075606>>|**followers|54543342|<Anil><><Kapoor>|<Delhi><<23.23><12.07>>|54543342.jpg@@|12311334|<Amit><><Bansal>|<Bangalore><<><>>|12311334.jpg"

def process_me(me):
	me=me.split("|")
	del me[0]
	# print me
	me[1]=me[1].replace("<>","$ ")           #represents empty field
	me[1]=me[1].replace("<"," ")
	me[1]=me[1].replace(">"," ")
	me[1]=' '.join(me[1].split()).split(" ")
	me[2]=me[2].replace("<>","$ ")           #represents empty field
	me[2]=me[2].replace("<"," ")
	me[2]=me[2].replace(">"," ")
	me[2]=' '.join(me[2].split()).split(" ")
	# print me
	return me
	
def process_followers(me):
	me=me.split("|")
	# print me
	me[2]=me[2].replace("<>","$ ")           #represents empty field
	me[2]=me[2].replace("<"," ")
	me[2]=me[2].replace(">"," ")
	me[2]=' '.join(me[2].split()).split(" ")
	me[3]=me[3].replace("<>","$ ")           #represents empty field
	me[3]=me[3].replace("<"," ")
	me[3]=me[3].replace(">"," ")
	me[3]=' '.join(me[3].split()).split(" ")
	# print me
	return me

def process_followers2(me):
	me=me.split("|")
	del me[0]
	# print me
	me[1]=me[1].replace("<>","$ ")           #represents empty field
	me[1]=me[1].replace("<"," ")
	me[1]=me[1].replace(">"," ")
	me[1]=' '.join(me[1].split()).split(" ")
	me[2]=me[2].replace("<>","$ ")           #represents empty field
	me[2]=me[2].replace("<"," ")
	me[2]=me[2].replace(">"," ")
	me[2]=' '.join(me[2].split()).split(" ")
	# print me
	return me


utk=OrderedDict()
l1=inp.split("**")   #len(l1) should be 2
me=l1[0]
followers=l1[1].split("@@")
me=process_me(me)

utk["id"]=me[0]
utk["name"]=OrderedDict()
utk["name"]["first"]=me[1][0]
utk["name"]["middle"]=me[1][1]
utk["name"]["last"]=me[1][2]
utk["location"]=OrderedDict()
utk["location"]["name"]=me[2][0]
utk["location"]["coords"]={}
utk["location"]["coords"]["long"]=me[2][1]
utk["location"]["coords"]["lat"]=me[2][2]
utk["imageId"]=me[3]

utk["followers"]=[]

for follower in followers:
	if followers.index(follower)==0:
		foll=process_followers(follower)
		del foll[0]
	else:
		foll=process_followers2(follower)
	temp=OrderedDict()
	temp["id"]=foll[0]
	temp["imageId"]=foll[3]
	temp["name"]=OrderedDict()
	temp["name"]["first"]=foll[1][0]
	temp["name"]["middle"]=foll[1][1]
	temp["name"]["last"]=foll[1][2]
	temp["location"]=OrderedDict()
	if len(foll[2])>1:
		temp["location"]["name"]=foll[2][0]
		temp["location"]["coords"]={}
		temp["location"]["coords"]["long"]=foll[2][1]
		temp["location"]["coords"]["lat"]=foll[2][2]
	else:
		temp["location"]=""
	utk["followers"].append(temp)

json_string = json.dumps(utk,sort_keys=False,indent=4)
json_string= json_string.replace("$","")

print json_string        #This is the final answer

