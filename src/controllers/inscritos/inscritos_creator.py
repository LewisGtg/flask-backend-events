from src.model.repositories.interfaces.inscritos_repository import InscritosRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class InscritosCreator:
    def __init__(self, inscritos_repo: InscritosRepositoryInterface):
        self.__inscritos_repo = inscritos_repo

    def create(self, http_request: HttpRequest) -> HttpResponse:
        inscrito_info = http_request.body["data"]
        inscrito_email = inscrito_info["email"]
        evento_id = inscrito_info["evento_id"]

        self.__check_inscrito(inscrito_email, evento_id)
        self.__insert_inscrito(inscrito_info)
        return self.__format_response(inscrito_info)

    def __check_inscrito(self, inscrito_email: str, evento_id: int) -> None:
        response = self.__inscritos_repo.select_incrito(inscrito_email, evento_id)
        if response: raise Exception("Inscrito already exists for this event")

    def __insert_inscrito(self, inscrito_info: dict) -> None:
        self.__inscritos_repo.insert(inscrito_info)

    def __format_response(self, inscrito_info: dict) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "type": "Inscrito",
                    "count": 1,
                    "attributes": inscrito_info
                }
            },
            status_code=201
        )