# NeuralNetworksAndDeepLearning
course 1 & 2 of Deep Learning Specialization


## Course 4 

cheat sheet `https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-convolutional-neural-networks`

### Week 1

#### Convolutions over volume
    1. The channels are RGB typically 3
    2. The number of channels in filter is the same number as in input channels
    3. The output of applying the 3D input to a 3D filter is a 2D output
    4. The third dimension in the output is the same number of filters applied.
    5. Therefore the number of channels in the output is same as the number of features 

1. Max pooling - preserves the  feature detected
2. Max pooling - no impact on gradient descent
3. Max pooling - only hyperparameters and no parameters to learn