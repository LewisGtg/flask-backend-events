from src.model.configs.connection import DBConnectionHandler
from src.model.entities.inscritos import Inscritos

class InscritosRepository:
    def insert(self, inscrito_infos: dict) -> None:
        with DBConnectionHandler() as db:
            try:
                new_inscrito = Inscritos(
                    nome=inscrito_infos.get("name"),
                    email=inscrito_infos.get("email"),
                    link=inscrito_infos.get("link"),
                    evento_id=inscrito_infos.get("evento_id")
                )
                db.session.add(new_inscrito)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def select_incrito(self, email: str, event_id: int) -> Inscritos:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Inscritos)
                .filter(
                    Inscritos.email == email, 
                    Inscritos.evento_id == event_id
                )
                .one_or_none()
            )

            return data