


def Encode():
    global enco
    enco = s.encode('iso-8859-8' , errors = 'xmlcharrefreplace')
    print(enco)
    print(type(enco))

def Decode():
    deco = enco.decode()
    print(deco)
    print(type(deco))


    
s = input('Enter your text : ')

Encode()
Decode()
