import torch
import torch.nn as nn

class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return torch.sigmoid(self.fc(x))

model = SimpleNN()

# Example input
input_tensor = torch.rand((1, 10))
output = model(input_tensor)
print("Model output:", output)
