#INSTITUTO TECNOLOGICO DE SAN JUAN DEL RIO 
#ESTRUCTURA DE DATOS 
#UNIDAD 1
#NOMBRE : ROCIO MOLINA MONROY 
#-----------------------------------------------------------
class CifradoAscii:
    def __init__(self, conservar_no_letras=False):
        self.conservar_no_letras = conservar_no_letras

    def texto_a_ascii(self, texto):
        resultado = []
        for caracter in texto.lower():
            if 'a' <= caracter <= 'z':
                resultado.append(str(ord(caracter)))
            elif self.conservar_no_letras:
                resultado.append(caracter)
        return resultado

    def ascii_a_texto(self, lista_ascii):
        elementos = lista_ascii.split() if isinstance(lista_ascii, str) else lista_ascii
        
        caracteres_reconstruidos = []
        for elemento in elementos:
            if elemento.isdigit():
                caracteres_reconstruidos.append(chr(int(elemento)))
            elif self.conservar_no_letras:
                caracteres_reconstruidos.append(elemento)
                
        return "".join(caracteres_reconstruidos)
    
if __name__ == "__main__":
    cifrador = CifradoAscii(conservar_no_letras=False)

    palabra = input("Escribe una palabra o frase: ")
    
    lista_codigos = cifrador.texto_a_ascii(palabra)

    if lista_codigos:
        codigos_str = " ".join(lista_codigos)
        print(f"Códigos ASCII de las letras: {codigos_str}")
        
        texto_original = cifrador.ascii_a_texto(lista_codigos)
        print(f"Texto reconstruido: {texto_original}")
    else:
        print("No se encontraron letras de la 'a' a la 'z' en el texto.")