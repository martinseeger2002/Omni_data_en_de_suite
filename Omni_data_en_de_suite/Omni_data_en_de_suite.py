



print('Welcome to the Omni File Suite.\n\nIf you have any questions or suggestions\nfeel free to reach out to me on twitter @martinseeger2.\
\nIf you find this program intresting or useful\nsend ltc to MD3dviJcZjZ1gFJFdSqwtnq6nWrdNyoB4r\nhelp support the creator.\n')
user_input = input\
('Input the action you would like to execute.\n\nRead commands:\nvp = view props.\nip = Image parse.\nmp3 = mp3 parse\n\nWrite commands:\niga = Generate omni arguments from in.jpeg image file.\nmp3ga = Generate omni arguments from in.mp3 mp3 file.\
\nfc = fee calulator.\nsif = Sendissuancefixed creats tokens from the arguments.txt. This will cost fees.\nsifs = Creats singal token if one is missing. Wait 13 min before you do this the transaction may still be verified.\n\nInput command:')


def fee_calc():
    import fee_calc.fee_calc
if user_input == 'fc':
    fee_calc()

def image_parse():
    import rpc_image_parse.image_parse
if user_input == 'ip':
    image_parse()

def mp3_parse():
    import mp3_parse.mp3_parse
if user_input == 'mp3':
    mp3_parse()

def gen_jpeg_argumnets():
    import file_to_omni_argumnets_txt.jpeg_file_to_omni_argumnets_txt
if user_input == 'iga':
    gen_jpeg_argumnets()

def gen_mp3_argumnets():
    import file_to_omni_argumnets_txt.mp3_file_to_omni_argumnets_txt
if user_input == 'mp3ga':
    gen_mp3_argumnets()

def omni_sendissuancefixed():
    import arguments_txt_to_rpc.omni_sendissuancefixed #be carful this one creates transactions.
if user_input == 'sif':
    omni_sendissuancefixed()

def omni_explorer():
    import omni_explorer.omni_RPC_explorer
if user_input == 'vp':
    omni_explorer()

def sendissuancefixed_singal():
    import sifs.sendissuancefixed_singal
if user_input == 'sifs':
    sendissuancefixed_singal()


def ipfs_milti_nfts():
    import ipfs_multi_nfts.ipfs_milti_nfts_to_omni_argumnets_txt
if user_input == 'ipfs':
    ipfs_milti_nfts()