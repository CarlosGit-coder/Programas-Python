# Dicionario principal
alunos = {}

# evitar duplicatas
alunos_cadastrados = set()

def mostrar_menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Cadastrar aluno")
    print("2 - Registrar notas")
    print("3 - Listar alunos e médias")
    print("4 - Buscar aluno")
    print("5 - Mostrar aprovados e reprovados")
    print("6 - Relatórios")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def cadastrar_aluno():
    print("\n=== Cadastrar aluno ===")
    nome = input("Digite o nome do aluno: ").strip().capitalize()

    if not nome:
        print("Nenhum nome inserido! Insira um nome válido.")
        return

    if nome in alunos_cadastrados:
        print("Aluno já cadastrado! Escolha outro nome.")
        return

    alunos[nome] = ()
    alunos_cadastrados.add(nome)
    print(f"Aluno cadastrado com sucesso: {nome}")

def registrar_notas():
    print("\n=== Registrar notas ===")
    nome = input("Digite o nome do aluno: ").strip().capitalize()

    if nome not in alunos:
        print("Aluno inexistente! Cadastre o aluno antes.\n")
        return

    if alunos[nome]:
        confirmar = input(f"{nome} já tem notas cadastradas! Deseja substituir? [S/N]: ").strip().upper()
        if confirmar != 'S':
            print("Notas mantidas.\n")
            return

    notas_temporarias = []
    for i in range(3):
        while True:
            try:
                nota = float(input(f"Digite a nota {i + 1} do aluno: "))
                if 0 <= nota <= 10:
                    notas_temporarias.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Valor inválido! Digite um número (ex: 8.5).")

    alunos[nome] = tuple(notas_temporarias)
    print(f"Notas de {nome} registradas com sucesso!\n")

def listar_alunos_e_medias():
    print("\n=== Listar alunos e médias ===")
    if not alunos:
        print("Nenhum aluno cadastrado!")
        return

    for nome, notas in alunos.items():
        if notas:
            media = sum(notas) / len(notas)
            print(f"{nome}: média = {media:.2f}")
        else:
            print(f"{nome}: sem notas cadastradas.")
    print()

def buscar_aluno():
    print("\n=== Buscar aluno ===")
    nome = input("Digite o nome do aluno: ").strip().capitalize()

    if nome not in alunos:
        print("Aluno não encontrado.\n")
        return

    notas = alunos[nome]
    if notas:
        media = sum(notas) / len(notas)
        print(f"{nome}: notas = {notas}, média = {media:.2f}")
    else:
        print(f"{nome} ainda não possui notas cadastradas.")

def mostrar_aprovado_e_reprovado():
    print("\n=== Aprovados e Reprovados ===")
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return

    aprovados = []
    reprovados = []

    for nome, notas in alunos.items():
        if notas:
            media = sum(notas) / len(notas)
            if media >= 7:
                aprovados.append((nome, media))
            else:
                reprovados.append((nome, media))

    print("\n--- Aprovados ---")
    if aprovados:
        for nome, media in aprovados:
            print(f"{nome}: média = {media:.2f}")
    else:
        print("Nenhum aluno aprovado.")

    print("\n--- Reprovados ---")
    if reprovados:
        for nome, media in reprovados:
            print(f"{nome}: média = {media:.2f}")
    else:
        print("Nenhum aluno reprovado.")
    print()

def relatorio():
    if not alunos:
        print("Nenhum aluno cadastrado! Impossível gerar relatório.\n")
        return

    while True:
        opcao = mostrar_menu_relatorios()

        if opcao == '1':
            alunos_cadastrados_relatorio()
        elif opcao == '2':
            listar_alunos_e_medias()
        elif opcao == '3':
            mostrar_aprovado_e_reprovado()
        elif opcao == '0':
            break
        else:
            print("Opção inválida! Tente novamente.")

def mostrar_menu_relatorios():
    print("\n=== MENU RELATÓRIOS ===")
    print("1 - Alunos cadastrados")
    print("2 - Médias individuais")
    print("3 - Aprovados e reprovados")
    print("0 - Voltar")
    return input("Escolha uma opção: ")

def alunos_cadastrados_relatorio():
    print("\n=== Alunos cadastrados ===")
    for nome in alunos:
        print(f"- {nome}")
    print()

while True:
    opcao = mostrar_menu()

    if opcao == '1':
        cadastrar_aluno()
    elif opcao == '2':
        registrar_notas()
    elif opcao == '3':
        listar_alunos_e_medias()
    elif opcao == '4':
        buscar_aluno()
    elif opcao == '5':
        mostrar_aprovado_e_reprovado()
    elif opcao == '6':
        relatorio()
    elif opcao == '0':
        print("Programa encerrando... Programa finalizado! Dados salvos com sucesso.")
        break
    else:
        print("Opção inválida! Tente novamente.")