import torch
import os
import pandas as pd
import numpy as np
from torch_geometric.data import InMemoryDataset, Data, DataLoader
from variables import keypoint_start, keypoint_end, pose_map

def get_dataloader(filename, root, is_test):
    dataset = Dataset(filename, root, is_test)
    train_loader = DataLoader(dataset, batch_size=64)
    return train_loader

def create_edge_index(keypoint_start, keypoint_end):
    edge_indexes = np.array([keypoint_start, keypoint_end], dtype=np.float32)
    return torch.tensor(edge_indexes, dtype=torch.long)

def create_graph(row, edge_index):
    keypoint_coords = np.array(row.iloc[:3 * 31], dtype=np.float32).reshape(31, 3)
    class_index = pose_map[row.iloc[-1]]
    x = torch.tensor(keypoint_coords, dype=torch.float32)
    y = torch.tensor(np.asarray([class_index]), dtype=torch.long)

    return Data(x=x, edge_index=edge_index, y=y)

class Dataset(InMemoryDataset):
    def __init__(self, filename, root, data_test=False):
        self.data_test = data_test
        self.edge_index = create_edge_index(keypoint_start, keypoint_end)
        self.filename = filename
        super(Dataset, self).__init__(root)

    @property
    def raw_file_names(self):
        return self.raw_file_names
    
    @property 
    def processed_file_names(self):
        if self.data_test:
            return [f"graph_{i}.pt" for i in range(150)]
        else:
            return [f"graph_{i}.pt" for i in range(1250)]
        

    def get(self, i):
        return torch.load(os.path.join(self.processed_dir, f"graph_{i}.pt"))
    
    def len(self):
        if self.data_test:
            return 150
        else:
            return 1250

    def process(self):
        self.data = pd.read_csv(self.raw_paths[0])
        for index, row in self.data.iterrows():
            graph = create_graph(row, self.edge_index)
            torch.save(graph, os.path.join(self.processed_dir, f"graph_{index}.pt"))