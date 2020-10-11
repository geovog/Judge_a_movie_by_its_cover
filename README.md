# Judge_a_movie_by_its_cover
## Cnn/LSTM implementation in python, to predict a movies genre by it's listing picture, or it's short description in imdb.com

- In phase 1 we create our dataset via calling scrap_threaded script which donwloads the movie's images and short descriptions from IMDB.com
- In phase 2 we explore and prerocess our data converting them to 228x228 size max
- In phase 3 we create a CNN model with multiple Conv2d layers, followed by 3 Dense Layers
- In phase 4 we create bidirectional LSTM model followed by a Convolutional-1D layer and lastly a Dense layer.
- In phase 5 we create a multi-input model using both image and text data in a try to create a multi-modal model which will make predictions based on both of the input types.

Trained models links on my personal drive (due to github size limitations)

https://drive.google.com/drive/folders/1_SN5Ol6m5YHjaWII8iVsqkARQN0Y2kC3?usp=sharing

Pre-trained word vectors used:

http://nlp.stanford.edu/data/glove.6B.zip

Dataset(Resized to 224X224):

Csv:

https://drive.google.com/file/d/16Fso0nPjPVIkaA5mvww9P-HqA_kMlFZ-/view?usp=sharing

## Prerequisites:
 
 - Conda
 - Python 3.7.9
 - Tensorflow 2
 - Graphviz (https://graphviz.gitlab.io/download/)
 - Jupyterlab
 - Sklearn
 
 Team Members:
 - George Vogiatzis
 - Michalis Prasinos
 - Myrsini Zourou
 
 
 ## Helpful Links Used
