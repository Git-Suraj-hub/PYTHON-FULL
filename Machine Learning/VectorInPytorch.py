import torch 
x = torch.tensor([25,2,3])   # 1d tensor
print(x)
print(type(x))
print(len(x))
print(x[0])
print(type(x[0]))
print(x.T)  
print(len(x.T))
 # warning show because this is 1d 


 # 2d tensor
y = torch.tensor([[25,2,3]])   # 1d
print(y)
print(type(y))
print(len(y))
print(y[0])
print(type(y[0]))
print(y.T) 
print(len(y.T))