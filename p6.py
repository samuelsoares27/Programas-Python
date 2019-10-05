def confirma(pergunta, tentativas=3, reclamacao='Sim ou Não por favor'):
    while True:
        resp = input(pergunta).lower()
        if resp in ('sim', 's'):
            return True
        elif resp in ('nao', 'não', 'n'):
            return False
        else:
            tentativas -= 1
        if tentativas == 0:
            raise IOError('Usuário não quer colaborar!!!')
        print(reclamacao)

confirma('Gravar <s/n>')