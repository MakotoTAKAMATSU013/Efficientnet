import torch
import torch.nn as nn

class Swish(nn.Module):
    def __init__(self):
        super(Swish, self).__init__()

    def forward(self, x):
        return x * torch.sigmoid(x)

class ConvBnAct(nn.Module):
    def __init__(self, n_in, n_out, kernel_size = 3, stride = 1, padding = padding, ):
        super().__init__()

    def forward(self, x):
        return x


class SEBlock(nn.Module):
    def __init__(self):
        super().__init__()

    def forward():

        return x*y

class DropSample():
    def __init__(self):
        super().__init__()

    def forward():
        return

class MBConvN():
    def __init__(self):
        super().__init__()

    def forward(self, x):

        return x

class MBConv1(MBConvN):
    def __init__(self):
        super().__init__()

class MBConv6(MBConvN):
    def __init__(self):
        super().__init__()

