from random import random
#initialise network
def initialize_network(n_inputs,n_hidden,n_outputs):
    network=list()
    hidden_layer=[{"weights":[random() for i in range(n_inputs+1)]} for i in range(n_hidden)]
    network.append(hidden_layer)
    output_layer=[{"weights":[random() for i in range(n_hidden+1)]} for i in range(n_outputs)]
    network.append(output_layer)
    return network
network=initialize_network(5,1,3)
for layer in network:
    print(layer)