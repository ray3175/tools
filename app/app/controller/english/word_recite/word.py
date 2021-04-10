from flask import request, abort, make_response
from flask_cors import cross_origin
from xy.exception import XYWarning
from ....config import AppConfig
from ....lib.flask.decorator import json_content_type
from ....lib.flask.response import response
from ....service.english.word_recite.word import ServiceWordReciteWord
from ....service.auth import ServiceAuth
from .. import english_word_recite_blueprint
from ..._auth import auth


@english_word_recite_blueprint.route("/word", methods=["POST"])
@cross_origin()
@auth
@json_content_type()
def word():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    token = request.headers.get(AppConfig()["web"]["key"])
    user = ServiceAuth().verify(token)
    if not (isinstance(user, dict) and (person_id:=user.get("person_id"))):
        raise XYWarning("该账号未绑定用户身份！")
    data = request.get_json()
    category_id = data.get("category_id")
    word_type = data.get("word_type")
    word_number = data.get("word_number")
    word_random_mode = data.get("word_random_mode")
    service_word_recite_word = ServiceWordReciteWord()
    if not (category_id and word_type in service_word_recite_word.WORD_TYPE and isinstance(word_number, int) and isinstance(word_random_mode, bool)):
        abort(400)
    if isinstance(data:=service_word_recite_word.get_word(category_id, person_id, word_type, word_number, word_random_mode), list):
        rsp["code"] = 200
        rsp["data"] = data
        rsp["msg"] = "获取单词详情成功！"
    return response(**rsp)


@english_word_recite_blueprint.route("/history-word", methods=["POST"])
@cross_origin()
@auth
@json_content_type()
def history_word():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    token = request.headers.get(AppConfig()["web"]["key"])
    user = ServiceAuth().verify(token)
    if not (isinstance(user, dict) and (person_id:=user.get("person_id"))):
        raise XYWarning("该账号未绑定用户身份！")
    data = request.get_json()
    category_id = data.get("category_id")
    word_type = data.get("word_type")
    history_time = data.get("history_time")
    service_word_recite_word = ServiceWordReciteWord()
    if not (category_id and word_type in service_word_recite_word.WORD_TYPE):
        abort(400)
    if isinstance(data:=service_word_recite_word.get_history_word(category_id, person_id, word_type, history_time), list):
        rsp["code"] = 200
        rsp["data"] = data
        rsp["msg"] = "获取单词详情成功！"
    return response(**rsp)


@english_word_recite_blueprint.route("/word-audio", methods=["POST"])
@cross_origin()
@auth
@json_content_type()
def word_audio():
    data = request.get_json()
    word_id = data.get("word_id")
    if not word_id:
        abort(400)
    audio_base64 = ServiceWordReciteWord().get_word_audio(word_id)
    rsp = make_response(audio_base64)
    rsp.headers["Content-Type"] = "audio/mpeg"
    return audio_base64


@english_word_recite_blueprint.route("/example-sentence", methods=["GET"])
@cross_origin()
@auth
def example_sentence():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    word_id = request.args.get("word_id")
    if not word_id:
        abort(400)
    if isinstance(data:=ServiceWordReciteWord().get_example_sentence(word_id), list):
        rsp["code"] = 200
        rsp["data"] = data
        rsp["msg"] = "获取单词例句成功！"
    return response(**rsp)


@english_word_recite_blueprint.route("/example-sentence/audio", methods=["POST"])
@cross_origin()
@auth
@json_content_type()
def example_sentence_audio():
    data = request.get_json()
    example_sentence_id = data.get("example_sentence_id")
    if not example_sentence_id:
        abort(400)
    audio_base64 = ServiceWordReciteWord().get_example_sentence_audio(example_sentence_id)
    rsp = make_response(audio_base64)
    rsp.headers["Content-Type"] = "audio/mpeg"
    return audio_base64


@english_word_recite_blueprint.route("/word/add-history", methods=["POST"])
@cross_origin()
@auth
@json_content_type()
def word_add_history():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    token = request.headers.get(AppConfig()["web"]["key"])
    user = ServiceAuth().verify(token)
    if not (isinstance(user, dict) and (person_id:=user.get("person_id"))):
        raise XYWarning("该账号未绑定用户身份！")
    data = request.get_json()
    record = data.get("record")
    if not isinstance(record, list):
        abort(400)
    if ServiceWordReciteWord().add_recite_history(person_id, record):
        rsp["code"] = 200
        rsp["msg"] = "恭喜您完成本次背诵！"
    return response(**rsp)

