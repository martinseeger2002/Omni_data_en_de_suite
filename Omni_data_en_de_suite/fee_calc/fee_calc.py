import ast
f = open('arguments.txt', 'r')
arguments_data = f.read()

sif_dict = ast.literal_eval(arguments_data)
f.close()
num_of_data = (len(sif_dict.keys())-2)//4*0.0013
print('this image will cost approx',str(num_of_data),'LTC to encoded.')