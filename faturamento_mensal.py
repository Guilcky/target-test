sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total_faturado = sp + rj + mg + es + outros

percent_sp = sp  / total_faturado
percent_rj = rj  / total_faturado
percent_mg = mg  / total_faturado
percent_es = es / total_faturado
percent_outros = outros  / total_faturado

print(f'SP - R${sp:,.2f} - {percent_sp:.2%}')
print(f'RJ - R${rj:,.2f} - {percent_rj:.2%}')
print(f'MG - R${mg:,.2f} - {percent_mg:.2%}')
print(f'ES - R${es:,.2f} - {percent_es:.2%}')
print(f'Outros - R${outros:,.2f} - {percent_outros:.2%} \n')
print(f'Total Faturado: {total_faturado:,.2f}')