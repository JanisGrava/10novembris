def lasit_datni():
    #pajautasim ievadit datnes nosaukumu
    datnes_nosaukums=input("ievadit datnes nosaukumu: ")
    try:
    #kā ielādēt datnes saturu?
       with open(datnes_nosaukums, 'r') as ff:
        saturs=ff.read()
        print(saturs)
        #print(saturs) pārliecinajos par to ka datne ir skaitli
        #IZVADI SIMBOLU SKAITU DATNĒ
        print(f"Simbolu skaits datē ir{len[saturs]}")

        #izvadi pirmos desmit simbolus
        print(f"pirmie 10simboli ir:{saturs[:10]}")

        # izvadi pirmo un pēdējo simbolu
        print(f"izvadit pirmo un pedejo simbolu:{saturs[0]} un {saturs[-1]}")


 except FileNotFoundError:
     print(""datne nav atrasta!")
 except ValueError:
     print("Datu kļuda!")




if __name__=="__main__":
    lasit_datni()