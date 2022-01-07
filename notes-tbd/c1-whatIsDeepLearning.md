# 1 What is Deep Learning

## 1.1 AI, ML, DL

### 1.1.1 AI

- started in 1950's
- AI is a field of study
- *AI*: the effort to automate intellectual tasks normally performed by humans
- It is a general field that also includes Symbolic, ML, DL
- *Symbolic AI*: AI made by people writing rules (50-80)
- *Expert system*: form of symbolic AI

### 1.1.2 Mechine Learning

- Systems learning there own rules was introduced by Alan Turing in 1950 paper "Computing Machinery and Intelligence"
- ML is a new programming paradigm which allows computers to make rules form data & answers
- ML: data & answers > Rules Classical: rules & data > answers
- ML is trained
- It took over 90's b/c hardware & data
- ML differs from statistics b/c less math grounded and more hands on

### 1.1.3 Learning representations from data 

#### ML needs 3 things

1. Input data points: For a picture it would be pixels
2. Examples of the expected output: Labeled pictures
3. A way to measure whether the algorithm is doing a good job: Used to find how far off the guess of the network is

- The goal of ML is to meaningfully transform data/Learn useful representations
- *Representation*: A different way to look at data
- A ML model looks for the best transformations to make to the data
- *Hypothesis space*: the space containing all possible operations on a set

### 1.1.4 The "deep" in deep learning

- Emphasis on successive layers of increasingly meaningful representations
- Deep in deep learning references the number of layers
- *depth* : the number of layers in a model
- *shallow learning*: learning with only 1 or 2 layers
- Layers representations are almost always learned with *neural Networks* on top of each other
- A Neural Network operates like a filter from layer to layer

### 1.1.5 understanding how deep leaning works

- What a layers dose to input data is stored in *weights* (bunch of numbers)
- Weights of the parameters of the layers
- Leaning is finding the values of the weights and minimizes the loss function
- A deep neural network contains millions of parameters
- *loss function*: used to measure the distance between the guess of the network and the wanted value
- The score from the loss function is used as a feedback signal to adjust the values of the weights in a direction to make the loss function score smaller
- *optimizer*: controls the process of changing the weight by implementing the Back propagation algorithm
- At first the weights are set to random values
- *Training loop*: the process of running data and changing weights which is run until minimum loss is achieved

### 1.1.6 What deep learning has achieved so far

- Near-human, image classification, recognition, handwriting transition, machine translation, Text-to-speech, driving, etc.
- There is a lot of application

### 1.1.7 Don't believe the short-term hype

- human-level general intelligence should not be taken to serious 
- lots of promise

### 1.1.8 The promise of AI

- Don't believe the short term hype believe the long term vision
