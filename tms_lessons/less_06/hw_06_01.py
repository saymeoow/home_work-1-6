some_txt_to_dec = b'r\xc3\xa9sum\xc3\xa9'
deco_txt=some_txt_to_dec.decode('utf-8')
print(deco_txt)
Latin_enc=deco_txt.encode('iso-8859-1')
print(Latin_enc)
Latin_deco=Latin_enc.decode('iso-8859-1')
print(Latin_deco)