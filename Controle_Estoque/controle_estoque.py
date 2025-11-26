# categorias de produtos
CATEGORIAS = ("Alimentos", "Limpeza", "Bebidas")

# Lista principal de produtos
produtos = []

# códigos já cadastrados
codigos = set()

#funções do sistema
def mostrar_menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Atualizar produto")
    print("5 - Excluir produto")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def cadastrar_produto():
    print("\n=== Cadastro de Produto ===")

    try:
        codigo = int(input("Código do produto: "))
    except ValueError:
        print(" Código inválido! Use apenas números.")
        return

    if codigo in codigos:
        print(" Código já cadastrado! Escolha outro.")
        return

    nome = input("Nome do produto: ").strip()
    if not nome:
        print(" Nome não pode ficar em branco.")
        return

    try:
        preco = float(input("Preço: R$ "))
        if preco < 0:
            print(" O preço não pode ser negativo.")
            return
    except ValueError:
        print(" Preço inválido!")
        return

    try:
        quantidade = int(input("Quantidade em estoque: "))
        if quantidade < 0:
            print(" A quantidade não pode ser negativa.")
            return
    except ValueError:
        print(" Quantidade inválida!")
        return

    # Escolher categoria
    print("\nCategorias disponíveis:")
    for i, categoria in enumerate(CATEGORIAS, 1):
        print(f"{i} - {categoria}")

    try:
        escolha = int(input("Escolha o número da categoria: "))
        categoria = CATEGORIAS[escolha - 1]
    except (ValueError, IndexError):
        print(" Categoria inválida!")
        return

    # Criar dicionário do produto
    produto = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
        "categoria": categoria
    }

    # Guardar na lista e no set
    produtos.append(produto)
    codigos.add(codigo)

    print(f" Produto '{nome}' cadastrado com sucesso!")
# listar produtos
def listar_produtos():
    print("\n=== Lista de Produtos ===")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(f"Código: {produto['codigo']} | Nome: {produto['nome']} | "
              f"Preço: R${produto['preco']:.2f} | Quantidade: {produto['quantidade']} | "
              f"Categoria: {produto['categoria']}")
# procurar produto
def buscar_produto():
    print("\n=== Buscar Produto ===")

    try:
        codigo = int(input("Informe o código do produto: "))
    except ValueError:
        print(" Código inválido!")
        return

    for produto in produtos:
        if produto["codigo"] == codigo:
            print(f"\nProduto encontrado:")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R${produto['preco']:.2f}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Categoria: {produto['categoria']}")
            return

    print(" Produto não encontrado!")
# atualizar produto, caso aperte enter nao atualiza
def atualizar_produto():
    print("\n=== Atualizar Produto ===")

    try:
        codigo = int(input("Informe o código do produto: "))
    except ValueError:
        print(" Código inválido!")
        return

    for produto in produtos:
        if produto["codigo"] == codigo:
            print(f"\nProduto encontrado: {produto['nome']}")

            novo_nome = input("Novo nome (Enter para manter): ").strip()
            if novo_nome:
                produto["nome"] = novo_nome

            try:
                novo_preco = input("Novo preço (Enter para manter): ").strip()
                if novo_preco:
                    produto["preco"] = float(novo_preco)
            except ValueError:
                print("Preço inválido, mantendo o anterior.")

            try:
                nova_qtd = input("Nova quantidade (Enter para manter): ").strip()
                if nova_qtd:
                    produto["quantidade"] = int(nova_qtd)
            except ValueError:
                print("Quantidade inválida, mantendo a anterior.")

            # Atualizar categoria
            print("\nCategorias disponíveis:")
            for i, categoria in enumerate(CATEGORIAS, 1):
                print(f"{i} - {categoria}")
            nova_categoria = input("Escolha nova categoria (Enter para manter): ").strip()
            if nova_categoria:
                try:
                    idx = int(nova_categoria) - 1
                    produto["categoria"] = CATEGORIAS[idx]
                except (ValueError, IndexError):
                    print("Categoria inválida, mantendo a anterior.")

            print(" Produto atualizado com sucesso!")
            return

    print(" Produto não encontrado!")

def excluir_produto():
    print("\n=== Excluir Produto ===")

    try:
        codigo = int(input("Informe o código do produto: "))
    except ValueError:
        print(" Código inválido!")
        return

    for produto in produtos:
        if produto["codigo"] == codigo:
            confirmar = input(f"Tem certeza que deseja excluir '{produto['nome']}'? (S/N): ").strip().lower()
            if confirmar == "s":
                produtos.remove(produto)
                codigos.remove(codigo)
                print("Produto excluído com sucesso!")
            else:
                print(" Exclusão cancelada.")
            return

    print(" Produto não encontrado!")
#menu
while True:
    opcao = mostrar_menu()

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        buscar_produto()
    elif opcao == "4":
        atualizar_produto()
    elif opcao == "5":
        excluir_produto()
    elif opcao == "0":
        print("Saindo do sistema... 👋")
        break
    else:
        print(" Opção inválida! Tente novamente.")
