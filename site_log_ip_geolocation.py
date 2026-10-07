import os, requests, csv, json

api_key = os.getenv("IPGEOLOCATION_API_KEY", "")

def open_log(filename):
	a = open(filename, "r")
	return [b for b in a]


def remove_bot_hack_ips(dataset):
	ban_list 	= ["googlebot", "spyder", "crawler", "spider", "nimbostratus", "petalbot", "bingbot", "seznambot", "ahrefsbot", "adsbot", "slackbot", "mj12bot", "barkrowler", "ru_bot", "semrushbot", "gowikibot", "blexbot", "serpstatbot", "domainsbot", "pandalytics", "crawlson", ".php", ".xml", ".env", "\"post"]
	a 			= []
	for b in dataset:
		c = b.split(" - -")[0]
		if not any(word in str(b).lower() for word in ban_list) and c not in a:
			a.append(c)
	return a


def get_ip(ip_address):
	if not api_key:
		raise RuntimeError("Set IPGEOLOCATION_API_KEY before running this script")
	a = "https://api.ipgeolocation.io/ipgeo?apiKey={}&ip={}".format(api_key, ip_address)
	b = requests.get(a)
	return json.loads(b.content)


def write_csv(filename):
	a = open(filename+".csv", "w", errors="ignore", newline="")
	return csv.writer(a)


def whois_call(ip_list):
	a = write_csv("12_17_2020")
	a.writerow(["ip", "continent_code", "continent_name", "country_code2", "country_code3", "country_name", "country_capital", "state_prov", "district", "city", "zipcode", "latitude", "longitude", "is_eu", "calling_code", "country_tld", "languages", "country_flag", "geoname_id", "isp", "connection_type", "organization", "currency", "time_zone"])
	for b in ip_list:
		c = get_ip(b)
		d = []
		for e in c:
			d.append(c[e])
			print(c[e])
		print("*"*50)
		a.writerow(d)


def init():
	a = open_log("shanelessa.com-Dec-2020")
	b = remove_bot_hack_ips(a)
	whois_call(b)

	# test = "2a03:2880:10ff:23::face:b00c"
	# get_ip(test)
	# shit = {"ip":"2a03:2880:10ff:23::face:b00c","continent_code":"NA","continent_name":"North America","country_code2":"US","country_code3":"USA","country_name":"United States","country_capital":"Washington, D.C.","state_prov":"New York","district":"Chelsea","city":"New York","zipcode":"10011","latitude":"40.74330","longitude":"-74.00790","is_eu":False,"calling_code":"+1","country_tld":".us","languages":"en-US,es-US,haw,fr","country_flag":"https://ipgeolocation.io/static/flags/us_64.png","geoname_id":"5128581","isp":"Facebook, Inc.","connection_type":"","organization":"Facebook, Inc.","currency":{"code":"USD","name":"US Dollar","symbol":"$"},"time_zone":{"name":"America/New_York","offset":-5,"current_time":"2020-12-17 15:06:23.254-0500","current_time_unix":1608235583.254,"is_dst":False,"dst_savings":1}}

init()