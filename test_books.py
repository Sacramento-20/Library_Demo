# Arquivo de testes para a classe Biblioteca
# Este arquivo contém testes automatizados que verificam o funcionamento
# correto das funcionalidades da biblioteca, incluindo:
# - Adição de catálogos e livros individuais
# - Listagem de livros
# - Busca de livros por título
import pytest
from books import Biblioteca

@pytest.fixture
def biblioteca():
    return Biblioteca()

def test_adicionar_catalogo(biblioteca):
    catalogo = [
        {"titulo": "Livro A", "autor": "Autor A", "ano": 2000},
        {"titulo": "Livro B", "autor": "Autor B", "ano": 2010}
    ]
    biblioteca.adicionar_catalogo(catalogo)
    assert len(biblioteca.catalogo_biblioteca) == 2

def test_adicionar_livro(biblioteca):
    biblioteca.adicionar_livro("Livro C", "Autor C", 2020)
    assert biblioteca.catalogo_biblioteca[-1]["titulo"] == "Livro C"

def test_listar_livros_vazio(capsys, biblioteca):
    biblioteca.listar_livros()
    captured = capsys.readouterr()
    assert "A biblioteca está vazia." in captured.out

def test_listar_livros_com_livros(capsys, biblioteca):
    biblioteca.adicionar_livro("Livro D", "Autor D", 2021)
    biblioteca.listar_livros()
    captured = capsys.readouterr()
    assert "Livro D" in captured.out

def test_buscar_livro_por_titulo_encontrado(capsys, biblioteca):
    biblioteca.adicionar_livro("Livro E", "Autor E", 2022)
    biblioteca.buscar_livro_por_titulo("Livro E")
    captured = capsys.readouterr()
    assert "Livro E" in captured.out

def test_buscar_livro_por_titulo_nao_encontrado(capsys, biblioteca):
    biblioteca.buscar_livro_por_titulo("Inexistente")
    captured = capsys.readouterr()
    assert "Nenhum livro encontrado" in captured.out
