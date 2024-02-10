import torch
from transformers import pipeline

setiment_pipeline = pipeline("sentiment-analysis")
data = ["I love you", "I hate you"];

setiment_pipeline(data)
