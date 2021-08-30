print('Análise da Turma')
print('===')
napv = int(input('Número de aprovados? '))
nrep = int(input('Número de reprovados? '))
total = napv+nrep
porc_rep = 100*nrep/total
porc_apv = 100*napv/total
print('---')
print('Total de alunos na turma: {}' .format(total))
print('Aprovados: {} = {:.1f}%' .format(napv, porc_apv))
print('Reprovados: {} = {:.1f}%' .format(nrep, porc_rep))
