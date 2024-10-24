class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            print(f"Livro {self.titulo} emprestado com sucesso")
            self.disponivel = False
        else:
            print(f"O livro {self.titulo} não está disponível")

    def devolver(self):
        if self.disponivel == False:
            print(f'Confirmado a devolução do livro {self.titulo}')
            self.disponivel = True
        else:
            print(f'O livro encontra-se disponível na livraria!')

    def mostrar_info(self):
        status = 'Disponível' if self.disponivel else 'Emprestado'
        print(f'Título: {self.titulo}, Autor: {self.autor}, Status: {status}')


class Livraria:

    def __init__(self):
        self.livros = []
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'O título {livro.titulo} foi adicionado na livraria')

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.emprestar()
                return
        print(f'O livro "{titulo}" esta indisponível.')

    def mostrar_inventario(self):
        if not self.livros:
            print('A livraria está vazia.')
        else:
            print('Inventário de livros:')
            for livro in self.livros:
                livro.mostrar_info()


# Instânciando objetos

# Instânciando livros
livro1 = Livro('Legend of Zelda', 'Shigeru Miyamoto')
livro2 = Livro('Berserk', 'Kentaro Miura')

# Instânciando Livraria
print()
livraria = Livraria()
livraria.adicionar_livro(livro1)
livraria.adicionar_livro(livro2)

# Mostrar inventário
print()
livraria.mostrar_inventario()
livraria.emprestar_livro('Berserk')
livraria.emprestar_livro('Berserk')

# Funções livro
print()
livro1.devolver()
livro2.devolver()
livro1.mostrar_info()
livro2.mostrar_info()