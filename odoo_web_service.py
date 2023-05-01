# Visit https://www.youtube.com/watch?v=brlgfZkR-LM
import xmlrpc.client

url_db1 = "https://hr.bincom.net"
db_1 = 'odoo'
username_db_1 = 'michaelorukpe.bincom@gmail.com'
password_db_1 = 'michael@123!'

common_1 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_db1))
models_1 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_db1))
version_db1 = common_1.version()
print("Details ....." , version_db1)


url_db2 = "http://52.90.187.115:8082"
db_2 = 'odoo-16'
username_db_2 = 'michaelorukpe.bincom@gmail.com'
password_db_2 = 'michael@123!'

common_2 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_db2))
models_2 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_db2))
version_db2 = common_2.version()
print("Details ....." , version_db2)

uid_db1 = common_1.authenticate(db_1, username_db_1, password_db_1, {})
uid_db2 = common_2.authenticate(db_2, username_db_2, password_db_2, {})
print("uid_db1" , uid_db1)
print("UID2 ......" , uid_db2)

db_1_leads = models_1.execute_kw(db_1, uid_db1, password_db_1, 'res.partner', 'search_read', [[]], {'fields': ['name', 'comment']})
total_count = 0
for lead in db_1_leads:
         print ("lead ....." , lead)
         total_count += 1
         new_lead = models_2.execute_kw(db_2, uid_db2, password_db_2, 'res.partner', 'create', [lead])
print("Total created...." , total_count)
