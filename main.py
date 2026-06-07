import os

PASTA_DOCUMENTOS = "documentos"

if not os.path.exists(PASTA_DOCUMENTOS):
    os.makedirs(PASTA_DOCUMENTOS)

print("Sistema de Biblioteca Digital iniciado.")


def listar_documentos():
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

    print("Documento criado com sucesso.")


listar_documentos()
adicionar_documento()


