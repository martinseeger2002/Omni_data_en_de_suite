import base64


##converts image.jpeg to b64 byte string you must copy the image file to the dir.
with open("in.jpeg", "rb") as file_to_string:
    data_b = base64.b64encode(file_to_string.read())
    file_to_string.close
    data = str(data_b)[2:]  ##this removes the "b'" from the begining of the byte string.

##splits b64 bytes into 255 data packets
n = 255
data_list = [data[index : index + n] for index in range(0, len(data), n)]
maddress = input("enter sending m-address\n:")
name = input('Enter the name of the new token.\n:')+'JPEG'
sif_dict = {"address": maddress, "esys": 1, "ttype": 1, "preid": 0, "name": name, "amount": 1}

serial_num = 100001
data_num = 0
max_data_num = (len(data_list)-1)


while data_num <= max_data_num:
    ## if there is enough data to create one data packet. This creates the commmand and adds it to RPCcommands.txt.
    if data_num==max_data_num:
        if len(data_list[data_num]) <= 254:
            sif_dict[str(serial_num)[-5:]+"d1"] = (data_list[data_num][:-1]+'=')
        elif len(data_list[data_num]) == 255:
            sif_dict[str(serial_num)[-5:]+"d1"] = (data_list[data_num])
        break
    ## if there is enough data to create two data packets. This creates the commmand and adds it to RPCcommands.txt.
    elif data_num==max_data_num-1:    
        sif_dict[str(serial_num)[-5:]+"d1"] = (data_list[data_num])
        if len(data_list[data_num+1]) <= 254:
            sif_dict[str(serial_num)[-5:]+"d2"] = (data_list[data_num+1][:-1]+'=')
        elif len(data_list[data_num+1]) == 255:
            sif_dict[str(serial_num)[-5:]+"d2"] = (data_list[data_num+1])
        break
    ## if there is enough data to create three data packets. This creates the commmand and adds it to RPCcommands.txt.
    elif data_num==max_data_num-2:    
        sif_dict[str(serial_num)[-5:]+"d1"] = (data_list[data_num])
        sif_dict[str(serial_num)[-5:]+"d2"] = (data_list[data_num+1])
        if len(data_list[data_num+2]) <= 254:
            sif_dict[str(serial_num)[-5:]+"d3"] = (data_list[data_num+2][:-1]+'=')
        elif len(data_list[data_num+2]) == 255:
            sif_dict[str(serial_num)[-5:]+"d3"] = (data_list[data_num+2]) 
        break
    ## if there is enough data to create four data packets. This creates the commmand and adds it to RPCcommands.txt.
    elif data_num==max_data_num-3:
        sif_dict[str(serial_num)[-5:]+"d1"] = (data_list[data_num])
        sif_dict[str(serial_num)[-5:]+"d2"] = (data_list[data_num+1])
        sif_dict[str(serial_num)[-5:]+"d3"] = (data_list[data_num+2])
        if len(data_list[data_num+2]) <= 254:
            sif_dict[str(serial_num)[-5:]+"d4"] = (data_list[data_num+3][:-1]+'=')
        elif len(data_list[data_num+2]) == 255:
            sif_dict[str(serial_num)[-5:]+"d4"] = (data_list[data_num+3])
        break
    ## if there is enough data to create more than four data packets. This creates the commmand and adds it to RPCcommands.txt.
    elif data_num<=max_data_num-3:
        sif_dict[str(serial_num)[-5:]+"d1"] = (data_list[data_num])
        sif_dict[str(serial_num)[-5:]+"d2"] = (data_list[data_num+1])
        sif_dict[str(serial_num)[-5:]+"d3"] = (data_list[data_num+2])
        sif_dict[str(serial_num)[-5:]+"d4"] = (data_list[data_num+3])
        serial_num += 1
        data_num += 4
f = open('arguments.txt', 'w+')
f.write(str(sif_dict))
f.close()

print('Your jpeg flie has been converted to arguments.txt use the fee calc to see what it will cost to encode.')

