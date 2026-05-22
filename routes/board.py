from flask import Blueprint

bp = Blueprint("board", __name__)

@bp.route("/board")
def board():
    return "Board Page Later"