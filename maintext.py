from pytubefix import YouTube
from pytubefix.cli import on_progress
#Essas linhas importam a classe YouTube e a função on_progress do módulo pytubefix. A classe YouTube é usada para 
#interagir com vídeos do YouTube, enquanto on_progress é uma função de callback que pode ser usada para mostrar o progresso do download.

url = input("Digite a URL do Vídeo: ")
#Essa linha solicita ao usuário que digite a URL do vídeo do YouTube que deseja baixar. A URL digitada é armazenada na variável url.

destino = "Pasta_Vídeo"
#Aqui, a variável destino é definida com o valor "Pasta_Vídeo", que será o diretório onde o vídeo baixado será salvo.

yt = YouTube(url, on_progress_callback=on_progress)
print("\n", yt.title)
#Essa linha cria uma instância da classe YouTube usando a URL fornecida pelo usuário. A função on_progress é passada como 
#callback para monitorar o progresso do download.

ys = yt.streams.get_highest_resolution()
#Aqui, a variável ys é definida como o stream de vídeo com a maior resolução disponível. A função get_highest_resolution 
#retorna o stream de maior qualidade.

ys.download(output_path=destino)
print("\n \n Download Concluído!")
#Aqui, a variável ys é definida como o stream de vídeo com a maior resolução disponível. A função get_highest_resolution 
#retorna o stream de maior qualidade.