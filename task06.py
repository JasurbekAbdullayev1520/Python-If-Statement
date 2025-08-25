phone=input("Telefon raqam kiriting:")


c=phone[:2]

if c=='90' or c=='91':
    print("Beeline")

if c=='93' or c=='94':
    print("Ucell")

if c=='95' or c=='97':
    print("Uzmobile")

if c=='88' or c=='99':
    print("Mobiuz")

if c!='88' or c!='99' or c!='95' or c!='97' or c!='93'or c!= '94' or c!='90' or c!='91':
    print("Noma'lum raqam")