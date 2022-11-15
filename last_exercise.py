import argparse

if __name__ == "__main__":
    
    # Initialize the parser
    parser = argparse.ArgumentParser(
        prog="Training a MLP"
        description="This code trains a MLP using sklearn. The below hyperparamters should be fine tuned"
        epilog = "For more information visit: \n https://scikit-learn.org/stable/modules/generated/sklearn.neural_netwrok.MLPClassifier.html"
    )
    
    # Add the positional / optional params
    
    parser.add_argument("--hidden_layers",help="HIDDEN_LAYERS python list containing no. of neurons in each hidden layer")
    parser.add_argument("--activation",help="{identity, logistic, tanh, relu} activation function")
    parser.add_argument("--solver",help="{lbfgs, sgd, adam} optimizer algorithm")
    parser.add_argument("--batch_size",help="BATCH SIZE size of mini batches for stochastic optimizers")
    parser.add_argument("--learning_rate",help="{constant,invscaling, power_t, adaptive} Learning rate for weight updates")
    parser.add_argument("--learning_rate_init",help="initial learning rate", type = float)
    parser.add_argument("--early_stopping",help="Whether to use early stopping to terminate training", default = "Y")
    
    
    #Parse the arguments
    args = parser.parse_args()