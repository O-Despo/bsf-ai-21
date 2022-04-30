 # Training and Evaluation with the built-in methods
//+source+https://www.tensorflow.org/guide/keras/train_and_evaluate
//+tags+code,tf,tensorflow,ai,model,api,bsfai

## Main methods

- `Model.fit()`
- `Model.evaluate()`
- `Model.predict()`

//+SN+you can customize what happens when using `fit()`

### There are two methods of passing data in

- **Np arrays** if data is small
- **`tf.data.dataset`** if there is more data

#### normal workflow

- Train
- Validation
- Evaluation of test data

### Training with fit

- Batch size is a parameter of fir that canf be used to create batched data
- `model.fit(x_train, y_train, batch_size=64, epochs=3, validation_data=(x_val, y_val)`
- `model.fit` returns a history object which has records of training
- `model.evaluation(x, y, batch_size=)` is used to evaluate the test data
- `model.predit` is used to get outputs for new data

## `compile()`

- `fit()` requires, loss func, optimizer, metrics to monitor
- **`compile()`**: provides information needed for fit to work
\\+nc+model.compile():model.compile(optimizer=,loss=,metrics=[])

#### custom losses

Custom losses can be made with either
- a func that takes `y_true` and `y_pred`
- if you want a more complex loss then subclass `tf.keras.losses.Loss`

custom metrics are created subclassing `tf.keras.metrics.Metrix` with 4 methods
1. `__init__(self)`
2. `update_state(self, y_true, y_pred, sample_weight=None)`
3. `result(self)`
4. `reset_state(self)`

### Training and Evaluation from tf.data datasets

- `tf.data`: set of tools for loading and processing data
\\+SN+`steps_per_epoch` can be used to specify how many training steps to run for each epoch


