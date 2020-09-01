import requests as re
import json as js

	"""
	Monster information as follows:
	{
	"_id": "5e4ca3380b1bb138c5896748",
	"index": "aboleth",
	"name": "Aboleth",
	"size": "Large",
	"type": "aberration",
	"subtype": null,
	"alignment": "lawful evil",
	"armor_class": 17,
	"hit_points": 135,
	"hit_dice": "18d10",
	"speed": {
	"walk": "10 ft.",
	"swim": "40 ft."
	},
	"strength": 21,
	"dexterity": 9,
	"constitution": 15,
	"intelligence": 18,
	"wisdom": 15,
	"charisma": 18
	 }"""

debug = False
maxAmount = 5

if __name__ == "__main__":
	url = "https://www.dnd5eapi.co" 
	
	try:
		info = re.get(url+"/api/").json()
	except:
		print(url, " Could not be accessed: ")
		exit()

	#print(js.dumps(info, indent=2))



	print("Getting Monsters")
	monsterRes = re.get(url+info["monsters"])

	print("Converting Response to JSON")
	monsters = monsterRes.json()
	#print(js.dumps(monsters["results"],indent=2))


	easyMonsters = dict()
	easyMonsters["count"] = 0
	easyMonsters["monsters"] = list()
	stop = 0
	print("Finding Monsters")
	for monster in monsters["results"]:
		monsterData = re.get(url+monster["url"]).json()
		if (stop >= maxAmount and debug == True):
			break		

		#Change to refine monsters however you want. Monster data is as follows:
		if (monsterData["hit_points"]  < 50):
			easyMonster = dict()
			stop+=1
			#print(js.dumps(monsterData,indent=2))
			easyMonster["name"] = monsterData["name"]
			easyMonster["hp"] = monsterData["hit_points"]
			easyMonsters["monsters"].append(easyMonster)

			if stop % 10 == 0:
				print("Read {} Monsters".format(stop))
			
	#classes with hitPoints 
	print("Exporting Monsters")
	easyMonsters["count"] = stop
	with open("easyMonster.json",'w') as fout:
		js.dump(easyMonsters, fout,indent = 2)