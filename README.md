# Exercício de Livraria - Classe `Livro` e `Livraria`

Este exercício visa praticar os conceitos de Programação Orientada a Objetos (POO) em Python, implementando classes para gerenciar uma livraria, permitindo adicionar livros, emprestá-los e devolvê-los.

## Classes

### Classe `Livro`
A classe `Livro` representa um livro e possui os seguintes atributos e métodos:

#### Atributos:
- **`titulo`**: O título do livro.
- **`autor`**: O autor do livro.
- **`disponivel`**: Um booleano que indica se o livro está disponível para empréstimo. Por padrão, é `True`.

#### Métodos:
- **`__init__(self, titulo, autor)`**: Construtor que inicializa o título, autor e define o livro como disponível.
- **`emprestar(self)`**: Verifica se o livro está disponível. Se sim, marca o livro como não disponível e informa o sucesso do empréstimo. Caso contrário, informa que o livro não está disponível.
- **`devolver(self)`**: Permite devolver o livro, marcando-o novamente como disponível.
- **`mostrar_info(self)`**: Exibe as informações do livro (título, autor e status de disponibilidade).

### Classe `Livraria`
A classe `Livraria` gerencia um conjunto de livros e possui os seguintes métodos:

#### Atributos:
- **`livros`**: Uma lista que armazena os objetos da classe `Livro`.

#### Métodos:
- **`__init__(self)`**: Construtor que inicializa uma lista vazia de livros.
- **`adicionar_livro(self, livro)`**: Adiciona um objeto do tipo `Livro` à lista de livros da livraria.
- **`emprestar_livro(self, titulo)`**: Procura um livro pelo título e tenta realizar o empréstimo. Se o livro não for encontrado ou não estiver disponível, informa que o livro está indisponível.
- **`mostrar_inventario(self)`**: Exibe todos os livros presentes na livraria e suas informações. Se a livraria estiver vazia, exibe uma mensagem indicando isso.

## Exemplos de Uso

### Criando Livros

```python
livro1 = Livro('Legend of Zelda', 'Shigeru Miyamoto')
livro2 = Livro('Berserk', 'Kentaro Miura')
livraria = Livraria()
livraria.adicionar_livro(livro1)
livraria.adicionar_livro(livro2)
livraria.emprestar_livro('Berserk')  # Empresta o livro 'Berserk'
livraria.emprestar_livro('Berserk')  # Tentativa de emprestar novamente, falha pois já está emprestado
livro2.devolver()                    # Devolve o livro 'Berserk'
livraria.mostrar_inventario()  # Mostra os livros e seus status (disponível/emprestado)



