from flask import Blueprint


english_blueprint = Blueprint("english", __name__, url_prefix="/english")
english_word_overview_blueprint = Blueprint("word_overview", __name__, url_prefix="/english/word-overview")
english_word_detail_blueprint = Blueprint("word_detail", __name__, url_prefix="/english/word-detail")
english_word_recite_blueprint = Blueprint("word_recite", __name__, url_prefix="/english/word-recite")


from .default import *
from .word_overview import *
from .word_detail import *
from .word_recite import *
