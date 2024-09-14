from dataset import get_dataloader
from model import pose_rec_model
import torch
from train import train, test

train_dataloader, test_dataloader = get_dataloader("TRAIN_DF_SAMPLE.csv", "backend/train_folder/", False), get_dataloader("TEST_DF_SAMPLE.csv", "backend/test_folder/", True)
model = pose_rec_model(3, 128, 32, 5, 16, 8, 0.2)
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.005)

epochs = 100

for epoch in range(epochs):
    loss, accuracy = train(model, train_dataloader, criterion, optimizer)
    print(f"Epoch {epoch} Train Loss: {loss:.4f} Train Accuracy: {accuracy:.4f}")

test_loss, test_acc = test(model, test_dataloader, criterion)
print(f"Test Loss: {test_loss} Test Accuracy: {test_acc}")

path_to_model_save =  "test_model.pt"
torch.save(model.state_dict(), path_to_model_save)