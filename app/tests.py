from unittest import TestCase
from model_mommy import mommy

from app.models import AppModel


class Tests(TestCase):
    def test_soma(self):
        soma = 1 + 1
        self.assertEqual(soma, 3)

    def test_model(self):
        mommy.make(AppModel, nome='Teste', id=1)
        cadastros = AppModel.objects.all()
        self.assertEqual(cadastros.first().nome, 'Teste')
