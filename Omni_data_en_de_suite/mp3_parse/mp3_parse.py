
import base64

from bitcoinrpc.authproxy import AuthServiceProxy #you need to install bitcoinRPC for this to work. "pip install python-BitcoinRPC"

# set rpc_user and rpc_password in the litecoin.conf file settings-options-open configuratoin file and enter the text below.
"""

rpcuser=user
rpcpassword=password

server=1
rpcport=9332
rpcbind=9332

"""
rpc_user = 'user'
rpc_password = 'password'
user_def_name = input('Enter prop name\n:')


rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:9332"%(rpc_user, rpc_password))
data = rpc_connection.omni_listproperties() 
num_of_props = (len(data))-1
token_dict = {}



def add_to_dict():
    prop_num = 0
    while prop_num <= num_of_props:
        if data[prop_num]['name'][:-5] == user_def_name:
        
            num = data[prop_num]['name'][-5:]
            d1 = data[prop_num]['category']
            d2 = data[prop_num]['subcategory']
            d3 = data[prop_num]['url']
            d4 = data[prop_num]['data']
            
            if len(d1) == 255:
                token_dict[num+'d1'] = d1
            if len(d1) >= 1 and d1[-1] == '=':
                token_dict[num+'d1'] = d1
            if len(d1) >= 2 and d1[-2] == '=':
                token_dict[num+'d1'] = d1

            if len(d2) == 255:
                token_dict[num+'d2'] = d2
            if len(d2) >= 1 and d2[-1] == '=':
                token_dict[num+'d2'] = d2
            if len(d2) >= 2 and d2[-2] == '=':
                token_dict[num+'d2'] = d2

            if len(d3) == 255:
                token_dict[num+'d3'] = d3
            if len(d3) >= 1 and d3[-1] == '=':
                token_dict[num+'d3'] = d3
            if len(d3) >= 2 and d3[-2] == '=':
                token_dict[num+'d3'] = d3

            if len(d4) == 255:
                token_dict[num+'d4'] = d4
            if len(d4) >= 1 and d4[-1] == '=':
                token_dict[num+'d4'] = d4
            if len(d4) >= 2 and d4[-2] == '=':
                token_dict[num+'d4'] = d4
        prop_num += 1
    return(token_dict)

add_to_dict()


token_dict_pre_sort = token_dict.items()
sorted_token = str(sorted(token_dict_pre_sort))

print('The mp3 file is saved as out.mp3 in the omni_data_suite folder.')




sorted_token_str = sorted_token
token_list = sorted_token_str[2:-2].split(",")
data_list = str(token_list[1::2])
data2 = data_list.replace(')", " ','')
data3 = data2.replace("''","")
data = (data3[4:-3])       
       

decodeit = open('out.mp3', 'wb')
decodeit.write(base64.b64decode((data)))
decodeit.close()

