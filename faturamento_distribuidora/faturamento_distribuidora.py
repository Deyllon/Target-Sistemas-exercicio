sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
total = sp+rj+mg+es+outros

porcentagem_sp = round((sp*100)/total,2)
porcentagem_rj = round((rj*100)/total,2)
porcentagem_mg = round((mg*100)/total,2)
porcentagem_es = round((es*100)/total,2)
porcentagem_outros = round((outros*100)/total,2)


print(f"O percentual do estado de São Paulo é igual a {porcentagem_sp}%, o percentual do estado do Rio de Janeiro é igual a {porcentagem_rj}%, " +
      f"o percentual do estado de Minas Gerais é igual a {porcentagem_mg}%, o percentual do estado do Espirinto Santo é igual a {porcentagem_es}%, "+
      f"o percentual de outros estados é igual a {porcentagem_outros}%")


