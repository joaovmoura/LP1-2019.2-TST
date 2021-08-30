def tradutor_morse(codigo):
    morse = ['.-', '-...', '-.-.', '-..', '.',
            '..-.', '--.', '....', '..', '.---', '-.-', '.-..',
            '--', '-.', '---', '.--.', '--.-', '.-.', '...', 
            '-',  '..-', '...-', '.--', '-..-', '-.--', '--..']
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    aux = ''
    for e in codigo:
        indice = 0
        for i in range(26):
            carac = morse[i]
            if e==carac:
                indice = i
                break
        aux+=alfabeto[indice]


    return aux

#print(tradutor_morse(['.-', '-...', '-.-.', '-..', '.','..-.', '--.', '....', '..', '.---', '-.-', '.-..','--', '-.', '---', '.--.', '--.-', '.-.', '...','-',  '..-', '...-', '.--', '-..-', '-.--', '--..']))


