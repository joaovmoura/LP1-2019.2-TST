#coding utf-8
def quanto_tempo(horario1, horario2):
    h1,m1 = horario1.split(':')
    h1,m1 = [int(e) for e in (h1,m1)]
    h2,m2 = horario2.split(':')
    h2,m2 = [int(e) for e in (h2,m2)]

    t1 = 60*h1+m1
    t2 = 60*h2+m2

    d = t2-t1
    hd = d//60
    md = d%60

    s = '%d hora(s) e %d minuto(s)' %(hd,md)

    return s


