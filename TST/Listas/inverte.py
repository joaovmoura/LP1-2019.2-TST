def inverte3a3(s):
    ret=''
    for i in range(len(s)-1,-1, -3):
        ret+= s[i-2] + s[i-1] + s[i]
    return ret
