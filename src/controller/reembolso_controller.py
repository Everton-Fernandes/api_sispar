from flask import Blueprint, request, jsonify
from src.model.reembolso_model import Reembolso
from src.model import db
from flasgger import swag_from  # type: ignore

bp_reembolso = Blueprint("reembolso", __name__, url_prefix="/reembolso")


@bp_reembolso.route("/todos-reembolsos")
def pegar_dados_todos_reembolsos():
    reembolsos = db.session.execute(db.select(Reembolso)).scalars().all()
    reembolsos = [reembolso.all_data() for reembolso in reembolsos]
    return jsonify(reembolsos), 200


@bp_reembolso.route("/cadastrar", methods=["POST"])
@swag_from("../docs/reembolso/cadastrar_reembolso.yml")
def cadastrar_novo_reembolso():
    dados_requisicao = request.get_json()

    novo_reembolso = Reembolso(
        colaborador=dados_requisicao["colaborador"],
        empresa=dados_requisicao["empresa"],
        num_prestacao=dados_requisicao["num_prestacao"],
        descricao=dados_requisicao["descricao"],
        data=dados_requisicao["data"],
        tipo_reembolso=dados_requisicao["tipo_reembolso"],
        centro_custo=dados_requisicao["centro_custo"],
        ordem_interna=dados_requisicao["ordem_interna"],
        divisao=dados_requisicao["divisao"],
        pep=dados_requisicao["pep"],
        moeda=dados_requisicao["moeda"],
        distancia_km=dados_requisicao["distancia_km"],
        valor_km=dados_requisicao["valor_km"],
        valor_faturado=dados_requisicao["valor_faturado"],
        despesa=dados_requisicao["despesa"],
        id_colaborador=dados_requisicao["id_colaborador"],
        status=dados_requisicao["status"],
    )

    db.session.add(novo_reembolso)
    db.session.commit()

    return jsonify({"mensagem": "Dado cadastrado com sucesso"}), 201


@bp_reembolso.route("/atualizar/<int:id_reembolso>", methods=["PUT"])
def atualizar_dados_do_reembolso(id_reembolso):
    dados_requisicao = request.get_json()

    reembolso = db.session.execute(
        db.select(Reembolso).where(Reembolso.id == id_reembolso)
    ).scalar_one_or_none()

    if not reembolso:
        return jsonify({"mensagem": "Reembolso não encontrado"}), 404

    for key, value in dados_requisicao.items():
        setattr(reembolso, key, value)

    db.session.commit()

    return jsonify({"mensagem": "Dados do reembolso atualizados com sucesso"}), 200


@bp_reembolso.route("/deletar/<int:id_reembolso>", methods=["DELETE"])
def deletar_reembolso(id_reembolso):
    reembolso = db.session.execute(
        db.select(Reembolso).where(Reembolso.id == id_reembolso)
    ).scalar_one_or_none()

    if not reembolso:
        return jsonify({"mensagem": "Reembolso não encontrado"}), 404

    db.session.delete(reembolso)
    db.session.commit()

    return jsonify({"mensagem": "Reembolso deletado com sucesso"}), 200
