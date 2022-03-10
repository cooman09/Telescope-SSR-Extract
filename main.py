import json
import base64
import requests
token = 'Token ' + input('请输入token：') #请看抓包教程
endpoint = 'https://alihk.quickg.cc/api/v5/nodes/'
he = {'Host': 'alihk.quickg.cc','Authorization': token, 'channel': 'GW', 'appVersion': '1.0.0', 'Accept-Language': 'en-US,en;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'platform': 'ios', 'imei': '30750a377dab46109a2b27c425ed566f', 'Content-Length': '0', 'User-Agent': 'Telescope/129 CFNetwork/1329 Darwin/21.3.0', 'Connection': 'keep-alive', 'appBuild': '129', 'systemVersion': '15.3.1', 'Accept': 'application/json'}
try:
    r=requests.post(endpoint, headers=he)
except requests.exceptions.ConnectionError:
    print("Cannot connect to API. Please check your internet connection")
apidata = r.text
data = json.loads(apidata)
apinodes = data['data']
nodenum = 0
sublink = ''
for x in apinodes:
    nodeip = apinodes[nodenum]['ip']
    nodeport = apinodes[nodenum]['port']
    nodepass = apinodes[nodenum]['passwd']
    nodemethod = apinodes[nodenum]['method']
    nodename = apinodes[nodenum]['name']
    nodeprotocol = apinodes[nodenum]['protocol']
    nodeparam = apinodes[nodenum]['protoparam']
    obsfucation = apinodes[nodenum]['obfs']
    obfsparam = apinodes[nodenum]['obfsparam']
    nodepass_b64 = base64.b64encode(nodepass.encode('utf8')).decode('utf8')
    nodename_b64 = base64.b64encode(nodename.encode('utf8')).decode('utf8')
    nodeparam_b64 = base64.b64encode(nodeparam.encode('utf8')).decode('utf8')
    obfsparam_b64 = base64.b64encode(obfsparam.encode('utf8')).decode('utf8')
    node_pre_link = str(nodeip)+':'+str(nodeport)+':'+str(nodeprotocol)+':'+str(nodemethod)+':'+str(obsfucation)+':'+str(nodepass_b64)+'/?remarks='+str(nodename_b64)+'&protoparam='+str(nodeparam_b64)+'&obfsparam='+str(obfsparam_b64)
    node_b64 = base64.b64encode(node_pre_link.encode('utf8')).decode('utf8')
    print('ssr://'+str(node_b64))
    sublink = sublink + 'ssr://'+str(node_b64)+'|'
    nodenum+=1
print(sublink)
sub_b64 = base64.b64encode(sublink.encode('utf8')).decode('utf8')
print("\n\n\n"+sub_b64)
