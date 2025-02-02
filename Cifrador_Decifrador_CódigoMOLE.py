CaracM = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..", '.': '.-.-.-',',': '--..--', '?': '..--..', '!': '-.-.--', '-': '-....-',"'": '.----.', '/': '-..-.', '(': '-.--.', ')': '-.--.-','&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-.-.-','+': '.-.-.', '_': '..--.-', '$': '...-..-', '@': '.--.-.'}
Num = {"1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----"}
MorseCod = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E','..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J','-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O','.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T','..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y','--..': 'Z', '-----': '0', '.----': '1', '..---': '2','...--': '3', '....-': '4', '.....': '5', '-....': '6','--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.','--..--': ',', '..--..': '?', '-.-.--': '!', '-....-': '-','.----.': "'", '-..-.': '/', '-.--.': '(', '-.--.-': ')','.-...': '&', '---...': ':', '-.-.-.': ';', '-.-.-': '=','.-.-.': '+', '..--.-': '_', '...-..-': '$', '.--.-.': '@',}
print("Este é um cifrador e decifrador de código MOLE. Caso queira decifrar uma palavra codificada, separe cada caractere com um espaço e cada palavra com dois espaços. Caso queira codificar, a tradução resultante virá na mesma lógica. Orgulho de ser Mecajun!")

while True:
    mensagem = str(input('Digite o texto para que seja traduzido: ')).upper()
    morse = []
    trad = []
    if mensagem[0] == "." or mensagem[0] == "-":
        if ' ' in mensagem:
            palavras = mensagem.split('  ')
    
            for palavra in palavras:
                caracteres = palavra.split(' ')
                for carac in caracteres:
                    if carac in MorseCod:
                        traducao = ''.join(MorseCod.get(carac))
                        trad.append(traducao)
                    else:
                        print("A palavra não pôde ser traduzida. Algum caractere foi digitado incorretamente. Releia as instruções e tente novamente.")
            tradFinal = ' '.join(trad)
            print(tradFinal)
               
    elif mensagem[0] in CaracM or mensagem[0] in Num:
        
        for caractere in mensagem:
            if caractere == ' ':
                morse.append('  ')
                trad = " ".join(morse)
            elif caractere in CaracM:
                morse.append(CaracM[caractere])
                trad = " ".join(morse)
            elif caractere in Num:
                morse.append(Num[caractere])
                trad = " ".join(morse)
        print(trad)
    else:
        print("A palavra não pôde ser traduzida. Algum caractere foi digitado incorretamente ou não existe. Releia as instruções e tente novamente.")
