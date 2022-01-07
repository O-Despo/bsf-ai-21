
# Chapter 3 Linear Regrestion and byond

- **Regression**: the study of how to best fit a curve (or line) to summarize data
- **Parameter**: the choice of slope (weight in other contexts)
- **Model**: the equation the uses the parameter 
- we can generalize the equation for $M = {y = wx}$ where x is the input and w is the weight
- **best-fit**: the line the produces the least error between prediction and truth over the whole data set
- **ground truth**: the model the produces the least difference from its prediction
- **regression tries**: to design a function F that maps a give input to output
- **multivariate regression**: a regression algorithm with multiple variables
- a regression algorithm will always return continues output
- How do we figure this out try every option
- There are two major ways to check performance 1: variance 2: Bias
- **variance**: how the model reacts to small changes in the training sets
- **Bias**: the dependence and assumptions made based on the data set
- **overfitting**: when the model to closely adapts to the training data and cannot generalize
- **underfitting**: when the model dose not learn on training data and may be good for generalizing but not accurate
- balancing over and under fitting is the great challenge of ML
- You test on a training set the move to a testing dataset
- **cost function**: a way for TF to score each parameter it tries
- **epoch**: on loop though the training process
- for linear regression mean-squared-difference is used 
