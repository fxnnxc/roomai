
from typing import Dict
from roomai.models.entity_recognition import EntityRecognitionModel

class SentencenEntityRecognition:
    def __init__(self):
        self.model = EntityRecognitionModel()
    
    def get_entities(self, sentence:str) -> Dict:
        entities = self.model.forward(sentence)
        return entities
    
    
    