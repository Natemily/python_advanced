letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
dict = dict(zip(letters, morse))
line = "".join(input().upper().split()).replace(" ","").replace(",","").replace("!","").replace("+","").replace("=","").replace("?","").replace(".","").replace("-","")
for i in range(len(line)):
    print(dict[line[i]], end = " ")
