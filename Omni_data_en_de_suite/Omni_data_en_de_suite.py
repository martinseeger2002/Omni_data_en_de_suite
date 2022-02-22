
user_input = input\
('Input the action you would like to exacute.\n\nRead commands.\nvp = view props.\nip = Image parse.\n\nWrite commands.\nga = Gennerate omni arguments.\
\nfc = fee calulator.\nsif = Sendissuancefixed creats tokens. This will cost fees.\nsifs = Sendissuancefixed creats singal token. Wait 12 min before you do this. This will cost fees.\n:')


def fee_calc():
    import fee_calc.fee_calc
if user_input == 'fc':
    fee_calc()

def image_parse():
    import rpc_image_parse.image_parse
if user_input == 'ip':
    image_parse()

def gen_argumnets():
    import file_to_omni_argumnets_txt.file_to_omni_argumnets_txt
if user_input == 'ga':
    gen_argumnets()

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