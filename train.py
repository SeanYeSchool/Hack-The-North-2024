import torch

def train_model_perbatch(model, loader, criterion, optimizer):
    loss = 0
    num_correct = 0

    model.train()
    for graph in loader:
        x, y, edge_index, batch = graph.x, graph.y, graph.edge_index, graph.batch
        
        optimizer.zero_grad()
        output = model(x, edge_index, batch)
        
        for i in range(len(y)):
            if output.argmax(dim=1)[i] == y[i]:
                num_correct += 1
        
        loss = criterion(output, y)
        loss.backward()
        optimizer.step()

        loss += loss.item()
    
    avg_loss = loss / len(loader.dataset), avg_correct = num_correct / len(loader.dataset)

    return avg_loss, avg_correct 

def test_model_perbatch(model, loader, criterion):
    loss = 0
    num_correct = 0

    model.eval()
    with torch.no_grad():
        for graph in loader:
            x, y, edge_index, batch = graph.x, graph.y, graph.edge_index, graph.batch
            
            output = model(x, edge_index, batch)
            
            for i in range(len(y)):
                if output.argmax(dim=1)[i] == y[i]:
                    num_correct += 1
            
            loss = criterion(output, y)
            loss.backward()

            loss += loss.item()
    
    avg_loss = loss / len(loader.dataset), avg_correct = num_correct / len(loader.dataset)

    return avg_loss, avg_correct 