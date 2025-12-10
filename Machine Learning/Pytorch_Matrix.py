import torch as t
x = t.tensor([[25,2,3],[20,10,121],[12,14,16],[20,10,0]])

print(x)
print(x.shape)
print(len(x))
print(type(x))
print(x[0][1])
print(x[:,1])
print(x[2,:])