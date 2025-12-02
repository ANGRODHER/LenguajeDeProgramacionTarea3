class TipoAtomico:
    def __init__(self, nombre, representacion, alineacion):
        self.nombre = nombre
        self.representacion = representacion
        self.alineacion = alineacion

    def tamaño(self, estrategia="sin_empaquetar"):
        return self.representacion

    def padding(self, estrategia="sin_empaquetar"):
        return 0  # Los tipos atómicos no tienen padding interno

class Struct:
    def __init__(self, nombre, campos):
        self.nombre = nombre
        self.campos = campos  

    def tamaño(self, estrategia="sin_empaquetar"):
        if estrategia == "empaquetado":
            return sum(c.tamaño(estrategia) for c in self.campos)
        elif estrategia == "reordenado":
            # Ordenar campos por alineación descendente para minimizar padding
            campos_ordenados = sorted(self.campos, key=lambda c: -c.alineacion)
            tamaño_total = 0
            for campo in campos_ordenados:
                alineacion = campo.alineacion
                # Calcular padding necesario para alinear el campo actual
                padding = (alineacion - (tamaño_total % alineacion)) % alineacion
                tamaño_total += padding + campo.tamaño(estrategia)
            # Ajustar el tamaño total a la alineación del struct (la mayor de sus campos)
            alineacion_struct = max(c.alineacion for c in campos_ordenados)
            padding_final = (alineacion_struct - (tamaño_total % alineacion_struct)) % alineacion_struct
            return tamaño_total + padding_final
        else:
            tamaño_total = 0
            for campo in self.campos:
                alineacion = campo.alineacion
                padding = (alineacion - (tamaño_total % alineacion)) % alineacion
                tamaño_total += padding + campo.tamaño(estrategia)
            return tamaño_total

    def alineacion(self):
        return max(c.alineacion for c in self.campos)  

    def padding(self, estrategia="sin_empaquetar"):
        return self.tamaño(estrategia) - sum(c.tamaño(estrategia) for c in self.campos)

class Union:
    def __init__(self, nombre, campos):
        self.nombre = nombre
        self.campos = campos  

    def tamaño(self, estrategia="sin_empaquetar"):
        return max(c.tamaño(estrategia) for c in self.campos)

    def alineacion(self):
        return max(c.alineacion for c in self.campos)  

    def padding(self, estrategia="sin_empaquetar"):
        return self.tamaño(estrategia) - max(c.tamaño(estrategia) for c in self.campos)

class ManejadorTipos:
    def __init__(self):
        self.tipos = {}

    def definir_atomico(self, nombre, representacion, alineacion):
        self.tipos[nombre] = TipoAtomico(nombre, representacion, alineacion)

    def definir_struct(self, nombre, tipos_campos):
        campos = [self.tipos[t] for t in tipos_campos]
        self.tipos[nombre] = Struct(nombre, campos)

    def definir_union(self, nombre, tipos_campos):
        campos = [self.tipos[t] for t in tipos_campos]
        self.tipos[nombre] = Union(nombre, campos)

    def describir(self, nombre):
        tipo = self.tipos[nombre]
        estrategias = ["sin_empaquetar", "empaquetado", "reordenado"]
        resultados = {}
        for estrategia in estrategias:
            tamaño = tipo.tamaño(estrategia)
            if hasattr(tipo, 'alineacion') and callable(getattr(tipo, 'alineacion', None)):
                alineacion = tipo.alineacion()  
            else:
                alineacion = tipo.alineacion    
            padding = tipo.padding(estrategia)
            resultados[estrategia] = {
                "tamaño": tamaño,
                "alineación": alineacion,
                "padding": padding
            }
        return resultados

