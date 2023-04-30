# Installation-and-Database-Migration-of-Odoo
Installation of Odoo:
Visit https://www.digitalocean.com/community/tutorials/how-to-install-odoo-on-ubuntu-20-04-with-docker for installation.

Database Migration From On Odoo Version to Another.
1. Visit https://www.odoo.com/documentation/16.0/developer/reference/external_api.html
2. Create a file on terminal known as odoo_web_service.py
3. Go to the link in 1. and copy the python script:
	url = <insert server URL>
      db = <insert database name>
      username = 'admin'
      password = <insert password for your admin user (default: admin)>

   So, we will fill it like this:
      url = "https://hr.bincom.net"
      db = 'odoo'
      username = 'admin'
      password = 'admin'

4. Scroll down on the documentation and you will see "logging in". Copy teh python script. 
      common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
      common.version()

5. Just at the top we will see a "test database". We will copy the import (import the library) and add it to 4.
      import xmlrpc.client
      common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
      common.version()

6. We will do some editting so we can print the version:
      import xmlrpc.client
      common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
      version = common.version()
      print ("details ....." , version)
##############################################################################################################################################
7. Open your terminal to were you have odoo_web_service.py directory and run the following command:
      $ python3.5 -m odoo_web_service
   And we will see the version of the odoo.
####################################################################################################################################################

8. The next thing we are going to do is that we will fetch the data from database. We do this by going to "List records" on the odoo documentation and copying its commands:
      models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])
   But we have to call the model by going to "call method" in the documentation and we copy the first line:
      models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
   So it will look like this:
      models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
      models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])
   Remove : ['is_company', '=', True] and print partners using:
      models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
      partners = models.execute_kw(db, uid, password, 'res.partner', 'search', [[]])
      print ("Partners .....", partners)

9. We will scroll up and copy from the "Logging in" authentication.:
      uid = common.authenticate(db, username, password, {})

10. Below is how the odoo_web_service.py script will look like before running: 
     ####################################################################################################################################
                                        			odoo_web_service.py
     #####################################################################################################################################
      url = "https://hr.bincom.net"
      db = 'odoo'
      username = 'admin'
      password = 'admin'

      import xmlrpc.client
      common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
      version = common.version()
      print ("details ....." , version)

      uid = common.authenticate(db, username, password, {})
      print ("UID ....." , uid)
    
      models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
      partners = models.execute_kw(db, uid, password, 'res.partner', 'search', [[]])
      print ("Partners .....", partners)

      #######################################################################################################################################      

      
