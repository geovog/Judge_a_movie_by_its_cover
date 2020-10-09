# Judge_a_movie_by_its_cover
Cnn/LSTM implementation in python, to predict a movies genre by it's listing picture, or it's short description in imdb.com

--In phase 1 we create a CNN model with multiple Conv2d layers, followed by 3 Dense Layers
--In phase 2 we create bidirectional LSTM model followed by a Convolutional-1D layer and lastly a Dense layer.
--In phase 3 we create a multi-input model using both image and text data in a try to create a multi-modal model which will make predictions based on both of the input types.
