def sei_tocar_musica(musica, acordes):
    sei=0
    for e in musica:
        for el in acordes:
            if e==el:
                sei+=1
            if sei==len(musica): return True


    return False
