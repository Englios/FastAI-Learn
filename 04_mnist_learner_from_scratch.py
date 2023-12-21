from fastai.vision.all import *
from fastbook import *

path = untar_data(URLs.MNIST)
path.ls()

train_data = (path/'training').ls().sorted()
test_data = (path/'testing').ls().sorted()


# Continue with the code
train_tensors = {path.name:tensor(Image.open(img)) for img in train_data}
print(train_tensors)