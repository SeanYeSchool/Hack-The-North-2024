import torch
import os
import pandas as pd
import numpy as np
from torch_geometric.data import InMemoryDataset, DataLoader
from variables import keypoint_start, keypoint_end, pose_map

def create_edge_index(keypoint_start, keypoint_end):
    edge_indexes = np.array([keypoint_start, keypoint_end], dtype=np.float32)
    return torch.tensor(edge_indexes, dtype=torch.long)

def create_graph(row, edge_index):
    keypoint_coords = np.array(row.iloc[:3 * 31], dtype=np.float32)
    class_index = pose_map[row.iloc[-1]]



class Dataset(InMemoryDataset):
    def __init__(self, filename, root):
        self.edge_index = create_edge_index(keypoint_start, keypoint_end)
        self.filename = filename
        super(Dataset, self).__init__(root)

    @property
    def raw_file_names(self):
        return self.raw_file_names
    
    @property 
    def processed_file_names(self):
        return pd.read_csv("")

    def get(self, i):
        return torch.load(os.path.join(self.processed_dir, f"data_{i}.pt"))
    
    def len(self):

    def process(self):
        self.data = pd.read_csv(self.raw_paths[0])
        for index, row in self.data.iterrows():
            graph = row_to_graph(row, self.edge_index)
            torch.save(graph, os.path.join(self.processed_dir, f"data_{index}.pt"))