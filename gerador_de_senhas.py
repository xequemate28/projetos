#Gerador de senhas aleatórias

import secrets
senha = secrets.token_hex(8) #Se quiser aumentar o tamanho da senha, é só modificar esse número()
print(senha)
#mistura caracteres numéricos e alfanuméricos
#ex: se colocar(2) entre parênteses, fica com 4 caracteres, numéricos misturados com alfanuméricos

