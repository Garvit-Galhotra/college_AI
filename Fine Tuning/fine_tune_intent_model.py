# Semantic Similarity For Intent Classification
# model = sentence-transformer

from sentence_transformers import SentenceTransformer, losses
from torch.utils.data import DataLoader
import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_path)
#sys.path.append(r"H:\AI_Assistant\college_AI")

from training_data.intent_train_data import get_training_data

intent_data = get_training_data()
# Load a pretrained model
model = SentenceTransformer('multi-qa-MiniLM-L6-dot-v1')

# Create a DataLoader
# select the batch 16-32 for laptops or small GPU to train the model
train_dataloader = DataLoader(intent_data, shuffle=True, batch_size=16)

# Define the loss function
# it tells us how good or poorly the model is performing
# smaller the loss == better the accuracy of the college
train_loss = losses.CosineSimilarityLoss(model)

# Fine-tune the model
model.fit(
           train_objectives=[(train_dataloader, train_loss)],
           epochs=5,
           warmup_steps=100,
           output_path=("models/Fine_Tuned_Intent_Model")
        )

print("The Model is Succefully Fine Tuned On Customized Dataset For College Domain.")