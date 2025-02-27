import pytest
from .inscritos_repository import InscritosRepository

@pytest.mark.skip("Insert in DB")
def test_insert():
    inscrito_info = {
        "name": "nome12",
        "email": "email12@email.com",
        "evento_id": 1
    }

    inscrito_repo = InscritosRepository()
    inscrito_repo.insert(inscrito_info)

@pytest.mark.skip("Select in DB")
def test_select_inscrito():
    email = "email@email.com"
    evento_id = 12

    subs_repo = InscritosRepository()
    resp = subs_repo.select_incrito(email, evento_id)
    print(resp)
