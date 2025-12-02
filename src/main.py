from manejador_tipos import ManejadorTipos

def main():
    manejador = ManejadorTipos()
    while True:
        entrada = input("> ").strip().split()
        if not entrada:
            continue
        comando = entrada[0]
        if comando == "ATOMICO":
            nombre, representacion, alineacion = entrada[1], int(entrada[2]), int(entrada[3])
            manejador.definir_atomico(nombre, representacion, alineacion)
        elif comando == "STRUCT":
            nombre = entrada[1]
            tipos_campos = entrada[2:]
            manejador.definir_struct(nombre, tipos_campos)
        elif comando == "UNION":
            nombre = entrada[1]
            tipos_campos = entrada[2:]
            manejador.definir_union(nombre, tipos_campos)
        elif comando == "DESCRIBIR":
            nombre = entrada[1]
            resultados = manejador.describir(nombre)
            for estrategia, info in resultados.items():
                print(f"{estrategia}: Tamaño={info['tamaño']}, Alineación={info['alineación']}, Padding={info['padding']}")
        elif comando == "SALIR":
            break
        else:
            print("Comando no reconocido")

if __name__ == "__main__":
    main()





    
# > ATOMICO char 1 1
# > ATOMICO int 4 4
# > STRUCT foo char int
# > DESCRIBIR foo
# sin_empaquetar: Tamaño=8, Alineación=4, Padding=3
# empaquetado: Tamaño=5, Alineación=4, Padding=0
# reordenado: Tamaño=8, Alineación=4, Padding=3
# > UNION bar char int
# > DESCRIBIR bar
# sin_empaquetar: Tamaño=4, Alineación=4, Padding=0
# empaquetado: Tamaño=4, Alineación=4, Padding=0
# reordenado: Tamaño=4, Alineación=4, Padding=0
# > SALIR