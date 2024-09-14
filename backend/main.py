from dataset import get_dataloader
from model import pose_rec_model
import torch
from train import train, test

train_dataloader, test_dataloader = get_dataloader("TRAIN_DF_SAMPLE.csv", "train_folder/", False), get_dataloader("TEST_DF_SAMPLE.csv", "test_folder/", True)
model = pose_rec_model(3, 64, 16, 5, 8, 4, 0.35)
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

epochs = 20

for epoch in range(epochs):
    loss, accuracy = train(model, train_dataloader, criterion, optimizer)
    print(f"Epoch {epoch} Train Loss: {loss:.4f} Train Accuracy: {accuracy:.4f}")

test_loss, test_acc = test(model, test_dataloader, criterion)
print(f"Test Loss: {test_loss} Test Accuracy: {test_acc}")

path_to_model_save =  "test_model.pt"
torch.save(model.state_dict(), path_to_model_save)