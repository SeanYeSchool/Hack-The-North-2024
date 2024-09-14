import warnings
import torch.nn as nn
import torch.nn.functional as F
import torch_geometric.nn as gnn

warnings.filterwarnings('ignore')

class pose_rec_model(nn.Module):
    def __init__(self, in_features, hidden_features, out_features, num_classes, head_num_1, head_num_2, dropout):
        super(pose_rec_model, self).__init__()
        self.gat1 = gnn.GATConv(in_features, hidden_features, heads = head_num_1, concat = True, dropout = dropout)
        self.gat2 = gnn.GATConv(head_num_1 * hidden_features, out_features, heads = head_num_2, concat = False)
        self.classifier = nn.Linear(out_features, num_classes)

    def forward(self, x, edge_index, batch):
        x = self.gat1(x, edge_index)
        x = F.relu(x)
        x = self.gat2(x, edge_index)
        x = gnn.global_max_pool(x, batch)
        x = self.classifier(x)
        return x 
