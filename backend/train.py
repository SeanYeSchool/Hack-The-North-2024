import torch

def train(model, dataloader, criterion, optimizer):
    model.train()
    total_loss, correct = 0, 0

    for graph in dataloader:
        x, yoga_type, edge_index, batch = graph.x, graph.y, graph.edge_index, graph.batch
        
        optimizer.zero_grad()
        output = model(x, edge_index, batch)
        
        prediction = output.argmax(dim=1)
        correct += (prediction == (yoga_type)).sum()

        loss = criterion(output, yoga_type)
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item() 
        
    avg_loss, avg_correct = total_loss / len(dataloader.dataset), correct / len(dataloader.dataset)

    return avg_loss, avg_correct

def test(model, dataloader, criterion):
    total_loss, correct = 0, 0
    
    model.eval()
    with torch.no_grad():
        for graph in dataloader:
            x, yoga_type, edge_index, batch = graph.x, graph.y, graph.edge_index, graph.batch
            output = model(x, edge_index, batch)
            
            prediction = output.argmax(dim=1)
            correct += (prediction == yoga_type).sum()
            
            loss = criterion(output, yoga_type)
            total_loss += loss.item()
            
    avg_loss, avg_correct = total_loss / len(dataloader.dataset), correct / len(dataloader.dataset)

    return avg_loss, avg_correct 