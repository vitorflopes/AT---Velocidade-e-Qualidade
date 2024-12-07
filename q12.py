import os

def listar_arquivos(caminho):
    for item in os.listdir(caminho):
        item_completo = os.path.join(caminho, item)
        if os.path.isfile(item_completo):
            print(item_completo)
        elif os.path.isdir(item_completo):
            listar_arquivos(item_completo)

listar_arquivos("C:/DEV/EngenhariaDeIA/Finning-Tuning")
