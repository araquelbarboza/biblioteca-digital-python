import os

PASTA_DOCUMENTOS = "documentos"

if not os.path.exists(PASTA_DOCUMENTOS):
    os.makedirs(PASTA_DOCUMENTOS)

print("Sistema de Biblioteca Digital iniciado.")


def listar_documentos():
<<<<<<< HEAD
    if not os.path.exists(PASTA_DOCUMENTOS):
        print("Nenhum documento encontrado.")
        return

    print("\n📚 Documentos organizados por tipo:")

    for tipo in os.listdir(PASTA_DOCUMENTOS):
        pasta_tipo = os.path.join(PASTA_DOCUMENTOS, tipo)

        if os.path.isdir(pasta_tipo):
            print(f"\n📁 {tipo.upper()}")

            arquivos = os.listdir(pasta_tipo)

            if not arquivos:
                print("  (vazio)")
            else:
                for arquivo in arquivos:
                    print(" -", arquivo)


def adicionar_documento():
    tipo = input("Tipo (livros/artigos/teses): ")
    nome = input("Nome do documento: ")
    ano = input("Ano de publicação: ")

    pasta_tipo = os.path.join(PASTA_DOCUMENTOS, tipo)

    if not os.path.exists(pasta_tipo):
        os.makedirs(pasta_tipo)

    nome_arquivo = f"{ano}_{nome}"

    caminho = os.path.join(pasta_tipo, nome_arquivo)

    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Documento criado pelo sistema. Ano: {ano}")
=======
    arquivos = os.listdir(PASTA_DOCUMENTOS)

    if not arquivos:
        print("Nenhum documento encontrado.")
    else:
        print("\nDocumentos disponíveis:")
        for arquivo in arquivos:
            print("-", arquivo)


def adicionar_documento():
    nome = input("Digite o nome do documento: ")

    caminho = os.path.join(PASTA_DOCUMENTOS, nome)

    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write("Documento criado pelo sistema.")
>>>>>>> 3b893c6ea3251b795bf87604c998d95f4adce600

    print("Documento criado com sucesso.")


<<<<<<< HEAD
def remover_documento():
    tipo = input("Tipo (livros/artigos/teses): ")
    nome = input("Nome do documento: ")

    caminho = os.path.join(PASTA_DOCUMENTOS, tipo, nome)

    if os.path.exists(caminho):
        os.remove(caminho)
        print("Documento removido com sucesso.")
    else:
        print("Arquivo não encontrado.")


def renomear_documento():
    tipo = input("Tipo (livros/artigos/teses): ")
    nome_antigo = input("Nome atual do documento: ")
    novo_nome = input("Novo nome do documento: ")

    caminho_antigo = os.path.join(PASTA_DOCUMENTOS, tipo, nome_antigo)
    caminho_novo = os.path.join(PASTA_DOCUMENTOS, tipo, novo_nome)

    if os.path.exists(caminho_antigo):
        os.rename(caminho_antigo, caminho_novo)
        print("Documento renomeado com sucesso.")
    else:
        print("Arquivo não encontrado.")


=======
>>>>>>> 3b893c6ea3251b795bf87604c998d95f4adce600
def menu():
    while True:
        print("\n📚 SISTEMA DE BIBLIOTECA DIGITAL")
        print("1 - Listar documentos")
        print("2 - Adicionar documento")
<<<<<<< HEAD
        print("3 - Remover documento")
        print("4 - Renomear documento")
=======
>>>>>>> 3b893c6ea3251b795bf87604c998d95f4adce600
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_documentos()

        elif opcao == "2":
            adicionar_documento()

<<<<<<< HEAD
        elif opcao == "3":
            remover_documento()

        elif opcao == "4":
            renomear_documento()

        elif opcao == "0":
=======
        elif opcao == "0":
            print("Saindo...")
>>>>>>> 3b893c6ea3251b795bf87604c998d95f4adce600
            break

        else:
            print("Opção inválida")

<<<<<<< HEAD

menu()
=======
menu()


>>>>>>> 3b893c6ea3251b795bf87604c998d95f4adce600
