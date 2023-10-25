from PIL import Image

# Abra a imagem
imagem = Image.open("C://Users//Dell//Pictures//broly//broly.jpg")

# Obtenha as dimensões da imagem
largura, altura = imagem.size

# Crie uma cópia da imagem original
imagem_pb = imagem.copy()

# Crie as coordenadas iniciais
x = 0
y = 0

# Comece o loop while para percorrer os pixels
while y < altura:
    while x < largura:
        # Obtenha a cor do pixel original
        cor_original = imagem.getpixel((x, y))
        
        # Calcule a média ponderada das intensidades de cores (preto e branco)
        cinza = int((cor_original[0] + cor_original[1] + cor_original[2]) / 3)
        
        # Defina a cor do pixel na imagem em preto e branco
        imagem_pb.putpixel((x, y), (cinza, cinza, cinza))
        
        x += 1
    y += 1
    x = 0

# Salve a imagem em preto e branco
imagem_pb.save("imagem_pb.jpg")

# Feche a imagem original
imagem.close()
