from typing import Dict
from roomai.utils import get_model

class EntityRecognitionModel:
    def __init__(self, model_type, restore_path):
        self.deep_model = get_model(model_type)
        self.deep_model.load(self, restore_path)
    
    def forward(self, input:str) -> Dict:
        input = self.preprocess(input)
        # --- Do something with deeplearning model 
        output = self.deep_model(input)
        output = self.postprocess(output)
        entities = self.make_model_result(output)
        return entities
    
    def make_model_result(self, x:Dict) -> Dict:
        """ Make the final model result for the hard decision

        Args:
            x ([type]): [description]
        """
        result = None
        
        return result
    
    def preprocess(self, x:Dict) -> Dict:
        """Preprocess the given string

        Args:
            x (str): The raw string
        Return: 
            x (str): Preprocessed string
        """
        x = None
        return 
    
    def postprocess(self, x:Dict) -> Dict:
        """Preprocess the model output

        Args:
            x (str): The raw string
        Return: 
            x (str): Preprocessed string
        """