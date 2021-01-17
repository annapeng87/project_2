# LSTM RNN Pokemon Cardset Price Predictor

![Pokemon Price Predictor](Images/Pokemon.jpg)

We observed the closing prices for pokemon cardset has a dramatic rise over the years. We will use deep learning and NLP sentiment analysis to figure out the reasons of the rise and also predict the future prices for pokemon cardset.

In this assignment, we used deep learning recurrent neural networks to model pokemon closing prices. This model uses a 4 year window of closing prices to predict the next month's closing price.

Taks performed:

1. Prepare the data for training and testing
2. Build and train custom LSTM RNNs
3. Evaluate the performance of each model

- - -

## Instructions

### Prepare the data for training and testing

Use the starter code as a guide to create a Jupyter Notebook for each RNN. The starter code contains a function to create the window of time for the data in each dataset.

For the closing price model, we used previous closing prices to try and predict the next closing price. A function is provided in the notebook to help with this.

Each model will need to use 70% of the data for training and 30% of the data for testing.

Apply a MinMaxScaler to the X and y values to scale the data for the model.

Finally, reshape the X_train and X_test values to fit the model's requirement of samples, time steps, and features. 

### Build and train custom LSTM RNNs

Create the LSTM RNN architecture. We will fit the data using only closing prices.

Use the same parameters and training steps for each model. This is necessary to compare each model accurately.

### Evaluate the performance of each model

Finally, use the testing data to evaluate each model and compare the performance.

Use the above to answer the following:

> Which cardset is a better investment?
>
> Which window size works best for the model?

- - -

### Resources

[Keras Sequential Model Guide](https://keras.io/getting-started/sequential-model-guide/)

[Illustrated Guide to LSTMs](https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21)

[Stanford's RNN Cheatsheet](https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-recurrent-neural-networks)

- - -