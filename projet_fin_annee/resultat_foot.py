import requests

base = requests.get('https://apiv2.apifootball.com/?action=get_events&from=2020-02-7&to=2020-02-14&league_id=148&APIkey=0628296b0a3128f59906a23df3e1894bec4e9ebb46dc82a5261dc3625682961e')
data = base.json()

for i in range(3):
	print(data[i]["match_hometeam_name"], ": ", data[i]["match_hometeam_score"], " | VS | ", data[i]["match_awayteam_name"], ": ", data[i]["match_awayteam_score"])
	print("---------------------------")




input()

#https://apifootball.com/documentation/#Events