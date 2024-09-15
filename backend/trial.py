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

# learning rate: 0.005 hidden features: 32
# out_features: 8 dropout: 0.2
# head num 1: 4 head num 2: 2
# Test Loss: 0.03004862944285075 Test Accuracy: 0.3466666638851166
# learning rate: 0.005 hidden features: 32
# out_features: 8 dropout: 0.2
# head num 1: 4 head num 2: 4
# Test Loss: 0.02931783437728882 Test Accuracy: 0.3933333456516266
# learning rate: 0.005 hidden features: 32
# out_features: 8 dropout: 0.2
# head num 1: 8 head num 2: 2
# Test Loss: 0.027338775793711346 Test Accuracy: 0.4466666579246521
# learning rate: 0.005 hidden features: 32
# out_features: 8 dropout: 0.2
# head num 1: 8 head num 2: 4
# Test Loss: 0.029003087679545084 Test Accuracy: 0.36000001430511475
# learning rate: 0.005 hidden features: 32
# out_features: 8 dropout: 0.35
# head num 1: 4 head num 2: 2
# Test Loss: 0.02644729534784953 Test Accuracy: 0.4000000059604645
# learning rate: 0.005 hidden features: 32
# out_features: 8 dropout: 0.35
# head num 1: 4 head num 2: 4
# Test Loss: 0.02682916005452474 Test Accuracy: 0.4466666579246521
# learning rate: 0.005 hidden features: 32
# out_features: 8 dropout: 0.35
# head num 1: 8 head num 2: 2
# Test Loss: 0.031240920225779217 Test Accuracy: 0.23999999463558197
# learning rate: 0.005 hidden features: 32
# out_features: 8 dropout: 0.35

# learning rate: 0.005 hidden features: 32
# out_features: 16 dropout: 0.2
# head num 1: 4 head num 2: 2
# Test Loss: 0.029034229119618733 Test Accuracy: 0.40666666626930237
# learning rate: 0.005 hidden features: 32
# out_features: 16 dropout: 0.2
# Test Loss: 0.028005313078562417 Test Accuracy: 0.3933333456516266
# learning rate: 0.005 hidden features: 32
# out_features: 16 dropout: 0.2
# head num 1: 8 head num 2: 2
# Test Loss: 0.030228150685628254 Test Accuracy: 0.36666667461395264
# learning rate: 0.005 hidden features: 32
# out_features: 16 dropout: 0.2
# head num 1: 8 head num 2: 4
# Test Loss: 0.02887806495030721 Test Accuracy: 0.41999998688697815
# learning rate: 0.005 hidden features: 32
# out_features: 16 dropout: 0.35
# head num 1: 4 head num 2: 2
# Test Loss: 0.029306204319000245 Test Accuracy: 0.3733333349227905
# learning rate: 0.005 hidden features: 32
# out_features: 16 dropout: 0.35
# head num 1: 4 head num 2: 4
# Test Loss: 0.027917606035868327 Test Accuracy: 0.3466666638851166
# learning rate: 0.005 hidden features: 32
# out_features: 16 dropout: 0.35
# head num 1: 8 head num 2: 2
# Test Loss: 0.02933502753575643 Test Accuracy: 0.30666667222976685
# learning rate: 0.005 hidden features: 32
# out_features: 16 dropout: 0.35
# head num 1: 8 head num 2: 4
# Test Loss: 0.02949985980987549 Test Accuracy: 0.3866666555404663
# learning rate: 0.005 hidden features: 32
# out_features: 32 dropout: 0.2
# head num 1: 4 head num 2: 2
# Test Loss: 0.03006187597910563 Test Accuracy: 0.36666667461395264
# learning rate: 0.005 hidden features: 32
# out_features: 32 dropout: 0.2
# head num 1: 4 head num 2: 4
# Test Loss: 0.029120130538940428 Test Accuracy: 0.4266666769981384
# learning rate: 0.005 hidden features: 32
# out_features: 32 dropout: 0.2
# head num 1: 8 head num 2: 2
# Test Loss: 0.030541672706604003 Test Accuracy: 0.273333340883255
# learning rate: 0.005 hidden features: 32
# out_features: 32 dropout: 0.2
# head num 1: 8 head num 2: 4
# Test Loss: 0.029852854410807293 Test Accuracy: 0.3266666531562805
# learning rate: 0.005 hidden features: 32
# out_features: 32 dropout: 0.35
# head num 1: 4 head num 2: 2
# Test Loss: 0.02822982947031657 Test Accuracy: 0.4000000059604645
# learning rate: 0.005 hidden features: 32
# out_features: 32 dropout: 0.35
# head num 1: 4 head num 2: 4
# Test Loss: 0.03127725203831991 Test Accuracy: 0.2666666805744171
# learning rate: 0.005 hidden features: 32
# out_features: 32 dropout: 0.35
# head num 1: 8 head num 2: 2
# Test Loss: 0.028409666220347088 Test Accuracy: 0.36666667461395264
# learning rate: 0.005 hidden features: 32
# out_features: 32 dropout: 0.35
# head num 1: 8 head num 2: 4
# Test Loss: 0.030203716754913332 Test Accuracy: 0.30666667222976685
# learning rate: 0.005 hidden features: 64
# out_features: 8 dropout: 0.2
# head num 1: 4 head num 2: 2
# Test Loss: 0.03097705841064453 Test Accuracy: 0.23333333432674408
# learning rate: 0.005 hidden features: 64
# out_features: 8 dropout: 0.2
# head num 1: 4 head num 2: 4
# Test Loss: 0.02960762580235799 Test Accuracy: 0.40666666626930237
# learning rate: 0.005 hidden features: 64
# out_features: 8 dropout: 0.2
# head num 1: 8 head num 2: 2
# Test Loss: 0.02768187443415324 Test Accuracy: 0.4266666769981384
# learning rate: 0.005 hidden features: 64
# out_features: 8 dropout: 0.2
# head num 1: 8 head num 2: 4
# Test Loss: 0.030638142426808675 Test Accuracy: 0.30666667222976685
# learning rate: 0.005 hidden features: 64
# out_features: 8 dropout: 0.35
# head num 1: 4 head num 2: 2
# Test Loss: 0.027422226270039877 Test Accuracy: 0.40666666626930237
# learning rate: 0.005 hidden features: 64
# out_features: 8 dropout: 0.35
# head num 1: 4 head num 2: 4
# Test Loss: 0.026258843739827474 Test Accuracy: 0.47333332896232605
# learning rate: 0.005 hidden features: 64
# out_features: 8 dropout: 0.35
# head num 1: 8 head num 2: 2
# Test Loss: 0.03060280720392863 Test Accuracy: 0.2666666805744171
# learning rate: 0.005 hidden features: 64
# out_features: 8 dropout: 0.35
# head num 1: 8 head num 2: 4
# Test Loss: 0.0281050443649292 Test Accuracy: 0.4000000059604645
# learning rate: 0.005 hidden features: 64
# out_features: 16 dropout: 0.2
# head num 1: 4 head num 2: 2
# Test Loss: 0.02949449936548869 Test Accuracy: 0.30666667222976685
# learning rate: 0.005 hidden features: 64
# out_features: 16 dropout: 0.2
# head num 1: 4 head num 2: 4
# Test Loss: 0.030420278708140056 Test Accuracy: 0.2933333218097687
# learning rate: 0.005 hidden features: 64
# out_features: 16 dropout: 0.2
# head num 1: 8 head num 2: 2
# Test Loss: 0.027486642996470134 Test Accuracy: 0.4466666579246521
# learning rate: 0.005 hidden features: 64
# out_features: 16 dropout: 0.2
# head num 1: 8 head num 2: 4
# Test Loss: 0.029201591014862062 Test Accuracy: 0.41333332657814026
# learning rate: 0.005 hidden features: 64
# out_features: 16 dropout: 0.35
# head num 1: 4 head num 2: 2
# Test Loss: 0.029195685386657715 Test Accuracy: 0.41999998688697815
# learning rate: 0.005 hidden features: 64
# out_features: 16 dropout: 0.35
# head num 1: 4 head num 2: 4
# Test Loss: 0.0310178542137146 Test Accuracy: 0.2933333218097687
# learning rate: 0.005 hidden features: 64
# out_features: 16 dropout: 0.35
# head num 1: 8 head num 2: 2
# Test Loss: 0.02965634822845459 Test Accuracy: 0.3333333432674408
# learning rate: 0.005 hidden features: 64
# out_features: 16 dropout: 0.35
# head num 1: 8 head num 2: 4
# Test Loss: 0.030209949016571046 Test Accuracy: 0.3400000035762787
# learning rate: 0.005 hidden features: 64
# out_features: 32 dropout: 0.2
# head num 1: 4 head num 2: 2
# Test Loss: 0.02890779495239258 Test Accuracy: 0.3733333349227905
# learning rate: 0.005 hidden features: 64
# out_features: 32 dropout: 0.2
# head num 1: 4 head num 2: 4
# Test Loss: 0.028335561752319337 Test Accuracy: 0.4466666579246521
# learning rate: 0.005 hidden features: 64
# out_features: 32 dropout: 0.2
# head num 1: 8 head num 2: 2
# Test Loss: 0.030355409781138102 Test Accuracy: 0.36000001430511475
# learning rate: 0.005 hidden features: 64
# out_features: 32 dropout: 0.2
# head num 1: 8 head num 2: 4
# Test Loss: 0.02989180326461792 Test Accuracy: 0.3466666638851166
# learning rate: 0.005 hidden features: 64
# out_features: 32 dropout: 0.35
# head num 1: 4 head num 2: 2
# Test Loss: 0.02931197007497152 Test Accuracy: 0.3466666638851166
# learning rate: 0.005 hidden features: 64
# out_features: 32 dropout: 0.35
# head num 1: 4 head num 2: 4
# Test Loss: 0.029514232476552327 Test Accuracy: 0.30000001192092896
# learning rate: 0.005 hidden features: 64
# out_features: 32 dropout: 0.35
# head num 1: 8 head num 2: 2
# Test Loss: 0.03075168450673421 Test Accuracy: 0.3333333432674408
# learning rate: 0.005 hidden features: 64
# out_features: 32 dropout: 0.35
# head num 1: 8 head num 2: 4
# Test Loss: 0.029878836472829184 Test Accuracy: 0.31333333253860474
# learning rate: 0.005 hidden features: 128
# out_features: 8 dropout: 0.2
# head num 1: 4 head num 2: 2
# Test Loss: 0.027735546429951987 Test Accuracy: 0.40666666626930237
# learning rate: 0.005 hidden features: 128
# out_features: 8 dropout: 0.2
# head num 1: 4 head num 2: 4
# Test Loss: 0.029643732706705728 Test Accuracy: 0.4000000059604645
# learning rate: 0.005 hidden features: 128
# out_features: 8 dropout: 0.2
# head num 1: 8 head num 2: 2
# Test Loss: 0.02887324889500936 Test Accuracy: 0.3933333456516266
# learning rate: 0.005 hidden features: 128
# out_features: 8 dropout: 0.2
# head num 1: 8 head num 2: 4
# Test Loss: 0.03147266785303752 Test Accuracy: 0.23333333432674408
# learning rate: 0.005 hidden features: 128
# out_features: 8 dropout: 0.35
# head num 1: 4 head num 2: 2
# Test Loss: 0.0296460485458374 Test Accuracy: 0.31333333253860474