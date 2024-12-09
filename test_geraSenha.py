import unittest
from geraSenha import gerar_senha

class TestGeradorDeSenhas(unittest.TestCase):

    def test_tamanho_da_senha(self):
        senha = gerar_senha(tamanho=8)
        self.assertEqual(len(senha), 8, "O tamanho da senha não corresponde ao especificado.")
        senha = gerar_senha(tamanho=16)
        self.assertEqual(len(senha), 16, "O tamanho da senha não corresponde ao especificado.")

    def test_incluir_maiusculas(self):
        senha = gerar_senha(tamanho=12, incluir_maiusculas=True, incluir_numeros=False, incluir_especiais=False)
        self.assertTrue(any(c.isupper() for c in senha), "A senha não contém letras maiúsculas.")

    def test_excluir_maiusculas(self):
        senha = gerar_senha(tamanho=12, incluir_maiusculas=False, incluir_numeros=False, incluir_especiais=False)
        self.assertFalse(any(c.isupper() for c in senha), "A senha contém letras maiúsculas, mas não deveria.")

    def test_incluir_numeros(self):
        senha = gerar_senha(tamanho=12, incluir_maiusculas=False, incluir_numeros=True, incluir_especiais=False)
        self.assertTrue(any(c.isdigit() for c in senha), "A senha não contém números.")

    def test_excluir_numeros(self):
        senha = gerar_senha(tamanho=12, incluir_maiusculas=False, incluir_numeros=False, incluir_especiais=False)
        self.assertFalse(any(c.isdigit() for c in senha), "A senha contém números, mas não deveria.")

    def test_incluir_caracteres_especiais(self):
        especiais = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
        senha = gerar_senha(tamanho=12, incluir_maiusculas=False, incluir_numeros=False, incluir_especiais=True)
        self.assertTrue(any(c in especiais for c in senha), "A senha não contém caracteres especiais.")

    def test_excluir_caracteres_especiais(self):
        especiais = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
        senha = gerar_senha(tamanho=12, incluir_maiusculas=False, incluir_numeros=False, incluir_especiais=False)
        self.assertFalse(any(c in especiais for c in senha), "A senha contém caracteres especiais, mas não deveria.")

    def test_tamanho_minimo(self):
        with self.assertRaises(ValueError):
            gerar_senha(tamanho=3, incluir_maiusculas=True, incluir_numeros=True)

    def test_gerar_senha_padrao(self):
        senha = gerar_senha()
        self.assertEqual(len(senha), 12, "O tamanho padrão da senha não é 12.")
        self.assertTrue(any(c.islower() for c in senha), "A senha padrão não contém letras minúsculas.")
        self.assertTrue(any(c.isupper() for c in senha), "A senha padrão não contém letras maiúsculas.")
        self.assertTrue(any(c.isdigit() for c in senha), "A senha padrão não contém números.")
        self.assertTrue(any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/~`" for c in senha), "A senha padrão não contém caracteres especiais.")

    def test_obrigatorios_na_senha(self):
        senha = gerar_senha(tamanho=12, incluir_maiusculas=True, incluir_numeros=True, incluir_especiais=True)
        self.assertTrue(any(c.isupper() for c in senha), "A senha não contém letras maiúsculas, mas deveria.")
        self.assertTrue(any(c.isdigit() for c in senha), "A senha não contém números, mas deveria.")
        self.assertTrue(any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/~`" for c in senha), "A senha não contém caracteres especiais, mas deveria.")

if __name__ == '__main__':
    unittest.main()
