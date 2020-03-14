# Import necessary modules
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config

# Create a trainer that uses this config
trainer = Trainer(config.load("config.yml"))

# Load the training data
training_data = load_data('rasa.json')

# Create an interpreter by training the model
interpreter = trainer.train(training_data)


