import cherrypy
import os
import sys
from app import application

def main():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
    except:
        current_dir = os.path.dirname(os.path.abspath(sys.executable))


    staticConfig_o = {
        '/':{
            'tools.staticdir.root': current_dir,
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static',
            'tools.staticdir.index': './html/index.html',
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        }
    }
    normalConfig_o = {
        '/':{
            'tools.staticdir.root': current_dir,
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        }
    }
    cherrypy.tree.mount(None, '/', staticConfig_o)

    app_o = application.Application_cl(current_dir)
    cherrypy.tree.mount(app_o.claim, '/claim', normalConfig_o)
    # cherrypy.tree.mount(app_o.projekte, '/projekt', normalConfig_o)

    cherrypy.engine.start()
    cherrypy.engine.block()

if __name__ == "__main__":
	main()
