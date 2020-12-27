from app import database
from app import xmrrpc
from app import subcounter
import cherrypy
import qrcode

@cherrypy.expose
class REST_cl(object):
    def __init__(self, path):
        self.path = path
        self.scounter = subcounter.Subcounter_cl(self.path)
        self.wallet = xmrrpc.Wallet_cl()
        self.db = database.Database_cl()
    def GET(self, subadr=None, destadr=None):
        if subadr == None and destadr == None:
            subadrindex = self.scounter.incr()
            subadr = self.wallet.getsub(int(subadrindex))
            self.db.insertEntry(subadrindex, subadr)
            img = qrcode.make(str(subadr))
            img.save(self.path + "/static/img/" + str(subadr) + ".png")
            return str(subadr)
        elif subadr != None and destadr == None:
            subadrindex = self.db.getID(subadr)
            bolenz = self.wallet.subbolenz(subadrindex)
            print(subadrindex)
            print(bolenz)
            return str(bolenz)
        elif subadr != None and destadr != None:
            subadrindex = self.db.getID(subadr)
            tx_id = self.wallet.sweepsub(subadrindex, destadr)
            return str(tx_id)      
