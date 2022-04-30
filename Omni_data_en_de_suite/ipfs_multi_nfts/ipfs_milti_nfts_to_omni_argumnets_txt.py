import base64




catagory = input("enter catagory\n:")
subcatagory = input("enter subcatagory\n:")
maddress = input("enter sending m-address\n:")
name = input('Enter the name of the new token.\n:')
ipfs_link = input('eneter IPFS URL minus the serial number.\n')
data = input("enter data\n:")
sif_dict = {"address": maddress, "esys": 1, "ttype": 1, "preid": 0, "name": name, "amount": 1}


serial_num = 100001
max_serial_num = int(input('last serial number\n'))+100000


while serial_num <= max_serial_num:

    if serial_num<=max_serial_num:
        ipfs_nums = str(serial_num)[-5:]
        ipfs_num = int(ipfs_nums)
        sif_dict[str(serial_num)[-5:]+"d1"] = (catagory)
        sif_dict[str(serial_num)[-5:]+"d2"] = (subcatagory)
        sif_dict[str(serial_num)[-5:]+"d3"] = (ipfs_link+str(ipfs_num)+'.png')
        sif_dict[str(serial_num)[-5:]+"d4"] = (data)
        serial_num += 1
    elif serial_num==max_serial_num+1:
        break
f = open('arguments.txt', 'w+')
f.write(str(sif_dict))
f.close()

print('done')

