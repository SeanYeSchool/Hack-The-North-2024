from dataset import get_dataloader
from model import pose_rec_model
import torch
from train import train, test

param_grid = {
    'learning_rate': [0.005, 0.01],
    'hidden_features': [32, 64, 128],
    'out_features': [8, 16, 32],
    'dropout': [0.2, 0.35],
    'head_num_1': [4, 8],
    'head_num_2': [2, 4]
}

train_dataloader, test_dataloader = get_dataloader("TRAIN_DF_SAMPLE.csv", "train_folder/", False), get_dataloader("TEST_DF_SAMPLE.csv", "test_folder/", True)

learning_rates = param_grid['learning_rate']
hidden_features_list = param_grid['hidden_features']
out_features_list = param_grid['out_features']
dropouts = param_grid['dropout']
head_num_1_list = param_grid['head_num_1']
head_num_2_list = param_grid['head_num_2']

epochs = 15

for learning_rate in learning_rates:
    for hidden_features in hidden_features_list:
        for out_features in out_features_list:
            for dropout in dropouts:
                for head_num_1 in head_num_1_list:
                    for head_num_2 in head_num_2_list:
                        model = pose_rec_model(3, hidden_features, out_features, 5, head_num_1, head_num_2, dropout)
                        criterion = torch.nn.CrossEntropyLoss()
                        optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
                        
                        for epoch in range(epochs):
                            loss, accuracy = train(model, train_dataloader, criterion, optimizer)
                            # print(f"Epoch {epoch} Train Loss: {loss:.4f} Train Accuracy: {accuracy:.4f}")

                        test_loss, test_acc = test(model, test_dataloader, criterion)
                        print(f"learning rate: {learning_rate} hidden features: {hidden_features}")
                        print(f"out_features: {out_features} dropout: {dropout}")
                        print(f"head num 1: {head_num_1} head num 2: {head_num_2}")
                        print(f"Test Loss: {test_loss} Test Accuracy: {test_acc}")

# path_to_model_save =  "test_model.pt"
# torch.save(model.state_dict(), path_to_model_save)
