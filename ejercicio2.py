class Libro:
    def _init_(self, titulo, autor, anio_publicacion, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.numero_paginas = numero_paginas

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio_publicacion}, Páginas: {self.numero_paginas}")

libro = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, 417)
libro.mostrar_informacion()