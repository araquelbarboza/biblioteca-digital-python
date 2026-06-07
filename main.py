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


listar_documentos()
