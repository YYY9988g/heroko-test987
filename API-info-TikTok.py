import requests,user_agent,json,flask,bs4
from user_agent import generate_user_agent
from flask import Flask,jsonify
from flask import *
from bs4 import BeautifulSoup
from datetime import date

	
app = Flask(__name__)

@app.route('/')

def index():
    return "<h1>WELCOME TO THE API  SIDRAELEZZ TELEGRAM : @SidraTools</h1>"


@app.route('/info/tiktok/', methods=['GET'])
def tiktok():
	username = str(request.args.get('username'))
	url = 'https://www.tiktok.com/@'+str(username)+'?lang=en'
	headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'cookie' : 's_v_web_id=verify_4759e77ec70b30f5809b99b4e83cf170; tt_csrf_token=UnnTT-BD3b77BER0ScMT23x9; tt_webid_v2=6972528352738199042; tt_webid=6972528352738199042; MONITOR_WEB_ID=6972528352738199042; csrf_session_id=33dd9ae2d7064521b1fb68c47fb6e376; ttwid=1%7CwLimK0e14CMaCXiLsX2myGQvJoR3fo915olavJk5Dj8%7C1623418284%7Ce18f90ac79a745872544fd1583a806821d5f6c9158b0d627195c391e1826811a; R6kq3TV7=AMcrRft5AQAAjVJfEPehKE83G62yRxwPcWPaXYFikZR7GX1aQHzgFfgvUVYW|1|0|2b554837c6bb50a519a30dbd9d5993dc6bc9a899; ak_bmsc=81F43ED7B422ED308CE38925766575B825EEFE85C4210000AE65C360177EFA1B~pl1L8RCHdpnfcXaxKe2pz/rrFGQ7AvIDfN7D/22TzpTU+jZhxDJTPJeeBqZzBzFebXtRYd+rf7S7OmBWLe/P+NNTeXnw6pCQxbC3oIFuwYRtUEK/JN2GEhm+/Aft3RoUgU4e/U9MIt7FtXUm521joEAelJCNASPG7sXkCL9Gquc/S7Ss/uOSbUow59iqm/DE20qw90c3qyotU354d2k5uT/ZtjaXyF1fKW5RtVkjiSo2o=; bm_sz=37D69FC94E991FC2E9B16E331298202E~YAAQhf7uJch1QPd5AQAAtjFF+wwIPFmp+JnukUWFwWqe7X7doAuSddcEaF98dBdy4UG5HI0g+qLiAFukmWs9uJR48l9ItBNHUpPwRrW2gnAfasr0c7zqprBzAMgrMT0jqPEG2GenpL5lp6psMYSUW2agxDZY++1VmDyejBjQGqRh/g4VVjEnSpZ1kTrkah0q; _abck=3BB0FC28EA3D19A3D635197B489889C5~-1~YAAQhf7uJcl1QPd5AQAAtjFF+wZF5KnpMJ3JntFWraZlabgy8zYpHCGWOOOlZvd9iDaNjP0aLxrOLfernQM/KlnKVqllWNtTsnVatlXA9uvEtOcTzhLFiEoynT/MfV6GtNEzx54dOdnFXliM7F0ifN4WMqNvlQddCjSTp4ESCxMCZ/wixpiJAj7fhh+lqObndimxpSyFkdDwKKL/2r+zoMxUTUz7vga3x19kWzjEHbFfRsUsKEsq8Kz945ZlHNTbYsGhuLJbYW7sfixqbGe5AnJcU+H/JwGPEgW3fCJiF7lWCaAm9zR6iwUoi6HfM4QlxsM2eNX0hXyFm75mwFrP5GDjVH5PWn9cpsoovHfhXb9cDwjlN2L0gvqUPCU=~-1~-1~-1',
    'referer': 'https://www.tiktok.com/@'+str(username)+'?lang=en',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': generate_user_agent() }

	response = requests.get(url, headers=headers)
	if(response.status_code == 200 and response.text):
		soup = BeautifulSoup(response.text, 'html.parser')
		sidra = soup.find(id="__NEXT_DATA__").string
		data = json.loads(sidra)
		account = data['props']['pageProps']['userInfo']
		
		info_account = {
		"UserID": account["user"]["id"],
		"username": account["user"]["uniqueId"],
		"name":account["user"]["nickname"],
		"bio": account["user"]["signature"],
		"profileImage": account["user"]["avatarLarger"],
		"following": account["stats"]["followingCount"],
		"followers": account["stats"]["followerCount"],
		"videos": account["stats"]["videoCount"],
		"Date": date.fromtimestamp(account['user']['createTime']).year,
		"Telegram": "@SidraTools"}
		return jsonify(200,info_account)
		

	else:
		info_account = {
		"info": "user is not found",
		"Telegram": "@SidraTools"}
		return jsonify(404,info_account)


if __name__ == "__main__":
	app.run()
    
