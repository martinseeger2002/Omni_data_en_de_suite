
import time
import ast
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# rpc_user and rpc_password are set in the litecoin.conf file
rpc_user = 'user'
rpc_password = 'password'

rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:9332"%(rpc_user, rpc_password))


##opens arguments.txt as a dict
f = open('arguments.txt', 'r')
arguments_data = f.read()

sif_dict = ast.literal_eval(arguments_data)
f.close()
user_input = input("Enter 0 for new token series or enter the number of the last token to be succsefully created to continue series.\n:")
serial_num = int(user_input)+100001
num_of_data = (len(sif_dict.keys())-2)
sn = num_of_data//4
snf = num_of_data/4
max_serial_num = 100000+sn-1
sns = (str(snf)[-2:])
address = (sif_dict['address'])
name = (sif_dict['name'])
esys = int(sif_dict['esys'])
ttype = int(sif_dict['ttype'])
preid = int(sif_dict['preid'])
amount = str(sif_dict['amount'])


while serial_num <= max_serial_num:
    if serial_num <= max_serial_num-1:
        data_num = str(serial_num)[-5:]+'d1'
        d1 = (sif_dict[data_num])
        data_num = str(serial_num)[-5:]+'d2'
        d2 = (sif_dict[data_num])
        data_num = str(serial_num)[-5:]+'d3'
        d3 = (sif_dict[data_num])
        data_num = str(serial_num)[-5:]+'d4'
        d4 = (sif_dict[data_num])
        result = rpc_connection.omni_sendissuancefixed(address,esys,ttype,preid,d1,d2,name+str(serial_num)[-5:],d3,d4,amount) #rpc_connection.omni_sendissuancefixed
        print(result)
        if len(result) == 64:
            serial_num += 1
    elif serial_num == max_serial_num:
        data_num = str(serial_num)[-5:]+'d1'
        d1 = (sif_dict[data_num])
        data_num = str(serial_num)[-5:]+'d2'
        d2 = (sif_dict[data_num])
        data_num = str(serial_num)[-5:]+'d3'
        d3 = (sif_dict[data_num])
        data_num = str(serial_num)[-5:]+'d4'
        d4 = (sif_dict[data_num])
        result = rpc_connection.omni_sendissuancefixed(address,esys,ttype,preid,d1,d2,name+str(serial_num)[-5:],d3,d4,amount) #rpc_connection.omni_sendissuancefixed
        print(result)
        break

if sns == '75':
    serial_num = max_serial_num+1
    data_num = str(serial_num)[-5:]+'d1'
    d1 = (sif_dict[data_num])
    data_num = str(serial_num)[-5:]+'d2'
    d2 = (sif_dict[data_num])
    data_num = str(serial_num)[-5:]+'d3'
    d3 = (sif_dict[data_num])
    result = rpc_connection.omni_sendissuancefixed(address,esys,ttype,preid,d1,d2,name+str(serial_num)[-5:],d3,'',amount) #rpc_connection.omni_sendissuancefixed
    print(result)
if sns == '.5':
    serial_num = max_serial_num+1
    data_num = str(serial_num)[-5:]+'d1'
    d1 = (sif_dict[data_num])
    data_num = str(serial_num)[-5:]+'d2'
    d2 = (sif_dict[data_num])
    result = rpc_connection.omni_sendissuancefixed(address,esys,ttype,preid,d1,d2,name+str(serial_num)[-5:],'','',amount)  #rpc_connection.omni_sendissuancefixed
    print(result)
if sns == '25':
    serial_num = max_serial_num+1
    data_num = str(serial_num)[-5:]+'d1'
    d1 = (sif_dict[data_num])
    result = rpc_connection.omni_sendissuancefixed(address,esys,ttype,preid,d1,'',name+str(serial_num)[-5:],'','',amount) #rpc_connection.omni_sendissuancefixed
    print(result)
