emojis = {"feliz":"😃", "enamorado":"😍","risa":"🤣", "llorando": "😭", "enojado":"🤬", "python": "🐍",\
           "cool": "😎", "preocupado": "😰", "sorprendido": "😱", "ok": "👌", "beso": "😘"}
frase = input("Ingresa una frase: ")
frase = frase.lower()
palabras = frase.split()
resouesta= " "
for palabra in palabras :
    if palabras in emojis:
        respuesta = respuesta + emojis[palabra] + " "
    else:
        respuesta = respuesta + palabras + " "
print(respuesta)
