import os #pra lidar com as pastas/arquivos
from PIL import Image
#pillow: Biblioteca do python que lida com imagens (pip install Pillow)

def reduzirTamanhoImagens(input_dir, output_dir, largura, altura):
    lista_de_arquivos = os.listdir(input_dir)

    for nome in lista_de_arquivos:
        imagem = Image.open(os.path.join(input_dir, nome))
        redimensionada = imagem.resize((largura, altura)) # resize(): Não altera a imagem original, ele gera uma nova
        redimensionada.save(os.path.join(output_dir, nome))

if __name__ == '__main__':
    diretorio_das_imagems = input("Diretorio das imagens: ")
    onde_salvar_as_imagens = input("Onde desaja salvar as imagens: ")
    largura = int(input("Nova largura da imagem: "))
    altura = int(input("Nova altura da imagem: "))
    #diretorio = '/home/paulo/Documentos/resizepy/imagens/'
    #'/home/paulo/Documentos/resizepy/uploads/'
    reduzirTamanhoImagens(diretorio_das_imagems, onde_salvar_as_imagens, largura, altura)

    
