n = int(input())
perdido =  100*(n%400)/n
pag = n//400
print('Serão necessárias {} página(s) para visualizar os tweets.'.format(pag))
print('{:.1f}% dos tweets serão perdidos.' .format(perdido))
