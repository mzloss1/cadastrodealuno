'''
trabalho python cadastro de matricula escola
'''
alunos = [
    {
        "matricula": 101201,
        "nome": "Ana",
        "curso": "Sistemas de Informação",
        "nota": 8.5
    },
    {
        "matricula": 201304,
        "nome": "Andre",
        "curso": "Sistemas de Informação",
        "nota": 5.5
    },
    {
        "matricula": 301560,
        "nome": "Joao",
        "curso": "Sistemas de Informação",
        "nota": 6.5
    }
]

while True:
    print('''
===== SISTEMA ACADÊMICO =====
  1 - Cadastrar aluno
  2 - Listar alunos
  3 - Buscar aluno
  4 - Exibir estatísticas
  5 - Sair
  Escolha uma opção:
  ''')
    try:
        opcao = int(input('escolha uma opção -> '))
    except ValueError:
        print("\n[!] Por favor, digite um número válido.\n")
        continue

    if opcao == 5:
        print("\nSaindo do sistema... Até logo!")
        break

    elif opcao == 1:
        print("\n--- Cadastrar aluno ---")
        try:
            matricula = int(input('digite a matricula: '))
        except ValueError:
            print("\n[!] Erro: a matrícula deve conter apenas números.\n")
            continue

        if any(a['matricula'] == matricula for a in alunos):
            print("\n[!] Erro: já existe um aluno cadastrado com essa matricula.\n")
            continue

        nome = input('digite o nome: ')
        curso = input('digite o curso: ')
        try:
            nota = float(input('digite a nota: '))
        except ValueError:
            print("\n[!] Erro: digite uma nota válida (ex: 7.5).\n")
            continue

        alunos.append({
            'matricula': matricula,
            'nome': nome,
            'curso': curso,
            'nota': nota
        })
        print(f"\n-> Aluno(a) {nome} cadastrado(a) com sucesso!\n")

    elif opcao == 2:
        print("\n--- Lista de Alunos ---")
        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for a in alunos:
                print(f"Matrícula: {a['matricula']} | Nome: {a['nome']} | Curso: {a['curso']} | Nota: {a['nota']}")

    elif opcao == 3:
        print("\n--- Buscar Aluno ---")
        try:
            busca_mat = int(input('Digite a matrícula do aluno que deseja buscar: '))
        except ValueError:
            print("\n[!] Erro: digite apenas números para a matrícula.\n")
            continue

        encontrado = False
        for a in alunos:
            if a['matricula'] == busca_mat:
                print(f"\n-> Aluno encontrado:")
                print(f"   Nome: {a['nome']}")
                print(f"   Matrícula: {a['matricula']}")
                print(f"   Curso: {a['curso']}")
                print(f"   Nota: {a['nota']}\n")
                encontrado = True
                break
        
        if not encontrado:
            print("\n[!] Nenhum aluno encontrado com essa matrícula.\n")

    elif opcao == 4:
        print("\n--- Estatísticas da Turma ---")
        if not alunos:
            print("Não há alunos cadastrados para calcular estatísticas.")
        else:
            total_alunos = len(alunos)
            notas = [a['nota'] for a in alunos]
            media_geral = sum(notas) / total_alunos
            maior_nota = max(notas)
            menor_nota = min(notas)
            aprovados = sum(1 for n in notas if n >= 6.0)

            print(f"Total de alunos cadastrados: {total_alunos}")
            print(f"Média geral das notas: {media_geral:.2f}")
            print(f"Maior nota: {maior_nota}")
            print(f"Menor nota: {menor_nota}")
            print(f"Alunos com nota >= 6.0: {aprovados}\n")

    else:
        print("\n[!] Opção inválida! Escolha um número entre 1 e 5.\n")
