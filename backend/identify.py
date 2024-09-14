import numpy as np
import torch
from model import pose_rec_model
from dataset import create_edge_index
model = pose_rec_model("smth")
model.load_state_dict(torch.load("model_dir.pt", weights_only=False)) 
model.eval()

coords = [] # assuming that coords is a list of numbers

coords = coords[:31 * 3]
x = torch.tensor(np.array(coords).reshape(31, 3), dtype=torch.float32)

with torch.no_grad():
    out = model(x, create_edge_index(s), torch.tensor([0]))
    predictions = out.argmax(dim=1).item()
print(predictions) # not sure yet what you guys want to do here