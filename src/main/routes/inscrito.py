from flask import Blueprint, jsonify, request

inscrito_route_bp = Blueprint("inscrito_route", __name__)

from src.http_types.http_request import HttpRequest

from src.validators.inscritos_creator_validator import inscritos_creator_validator

from src.model.repositories.inscritos_repository import InscritosRepository

from src.controllers.inscritos.inscritos_creator import InscritosCreator

@inscrito_route_bp.route("/inscrito", methods=["POST"])
def create_new_inscrito():
    inscritos_creator_validator(request)
    http_request = HttpRequest(body=request.json)

    inscritos_repo = InscritosRepository()
    inscritos_creator = InscritosCreator(inscritos_repo)

    http_response = inscritos_creator.create(http_request)

    return jsonify(http_response.body), http_response.status_code