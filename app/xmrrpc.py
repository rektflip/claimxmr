import requests
from requests.auth import HTTPDigestAuth
import json

class Wallet_cl(object):
    def __init__(self):
        self.url = "http://127.0.0.1:18082/json_rpc"
    def mainbolenz(self):
        body = '{"jsonrpc":"2.0","id":"0","method":"get_balance","params":{"account_index":0,"address_indices":[0,1]}}'
        resp = requests.post(self.url, data=body, auth=HTTPDigestAuth("test", "test"))
        a = resp.json()
        bolenz = a["result"]["balance"]/1000000000000
        return bolenz
    def subbolenz(self, idx):
            body = '{"jsonrpc":"2.0","id":"0","method":"get_balance","params":{"account_index":0,"address_indices":[0,' + str(int(idx)) + ']}}'
            resp = requests.post(self.url, data=body, auth=HTTPDigestAuth("test", "test"))
            a = resp.json()
            bolenz = a["result"]["per_subaddress"][1]["unlocked_balance"]/1000000000000
            subadr = a["result"]["per_subaddress"][1]["address"]
            return bolenz
    def getsub(self, idx):
        body = '{"jsonrpc":"2.0","id":"0","method":"get_balance","params":{"account_index":0,"address_indices":[0,' + str(int(idx)) + ']}}'
        resp = requests.post(self.url, data=body, auth=HTTPDigestAuth("test", "test"))
        a = resp.json()
        subadr = a["result"]["per_subaddress"][1]["address"]
        return subadr
    def sweepsub(self, idx, adr):
            body = '{"jsonrpc":"2.0","id":"0","method":"sweep_all","params":{"address":"'+ str(adr) +'","subaddr_indices":['+ str(int(idx)) +'],"ring_size":11,"unlock_time":0,"get_tx_keys":true}}'
            resp = requests.post(self.url, data=body, auth=HTTPDigestAuth("test", "test"))
            a = resp.json()
            try:
                tx_hash = a["result"]["tx_hash_list"][0]
                return str(tx_hash)
            except:
                return a["error"]["message"]
