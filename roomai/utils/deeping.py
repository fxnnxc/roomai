
from deeping.nlp import *

MODELS = {
    "bert-entity": None
}


def get_model(model_name):
    model = MODELS[model_name]
    return model