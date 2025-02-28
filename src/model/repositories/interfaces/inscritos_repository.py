from abc import ABC, abstractmethod
from src.model.entities.inscritos import Inscritos

class InscritosRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, inscrito_infos: dict) -> None: pass
            
    @abstractmethod
    def select_incrito(self, email: str, event_id: int) -> Inscritos: pass