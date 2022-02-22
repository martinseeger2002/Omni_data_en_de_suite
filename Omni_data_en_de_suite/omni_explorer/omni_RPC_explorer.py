import time 
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# rpc_user and rpc_password are set in the litecoin.conf file
rpc_user = 'user'
rpc_password = 'password'

rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:9332"%(rpc_user, rpc_password))
data = rpc_connection.omni_listproperties() 
#test = rpc_connection.omni_getactivedexsells()

#print(test)


prop_num = 0
max_prop_num = (len(data))-1


while prop_num <= max_prop_num:  
    #if(data[prop_num]['name'][:5]) == str('Plana'):
        #print(data[prop_num]['name'][:-5])
        #print(data[prop_num]['url'])
    print(data[prop_num]['name'])
    print(data[prop_num]['propertyid'])
    time.sleep(0)      
    prop_num += 1
