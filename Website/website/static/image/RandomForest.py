#Importing Some Libraries

import pandas as pd
from sklearn.model_selection import train_test_split

#print(data[3800:])

X_full = pd.read_csv('train.csv', index_col = 'ID')
X_test_full = pd.read_csv('test.csv', index_col = 'ID')

#predected
y = X_full.Value
feature = ['Date']

# independent varibale
X = X_full[feature].copy()
X_test = X_test_full[feature].copy()

# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,
                                                      random_state=0)
print("Our random Trainnig data picked by algorithm: ")
print(X_train.head())
# Importing our Algorithm
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Define the models
model_1 = RandomForestRegressor(n_estimators=50, random_state=0)
model_2 = RandomForestRegressor(n_estimators=100, random_state=0)
model_3 = RandomForestRegressor(random_state=1)
model_4 = RandomForestRegressor(n_estimators=200, min_samples_split=20, random_state=0)
model_5 = RandomForestRegressor(n_estimators=100, max_depth=7, random_state=0)

models = [model_1, model_2, model_3, model_4, model_5]

# The difference between actual value and predicted value with mean absolute error (MAE)
from sklearn.metrics import mean_absolute_error

# Function for comparing different models
def score_model(model, X_t=X_train, X_v=X_valid, y_t=y_train, y_v=y_valid):
    model.fit(X_t, y_t)
    preds = model.predict(X_v)
    return mean_absolute_error(y_v, preds)

print("\nSocre of every Model: ")
for i in range(0, len(models)):
    mae = score_model(models[i])
    print("\nModel %d MAE: %d\n" % (i+1, mae))

best_model = model_1
    
# Fill in the best model
#best_model = model_1
# Define a model
my_model = best_model

# Fit the model to the training data
my_model.fit(X, y)

# Generate test predictions
preds_test = my_model.predict(X_test)

# Save predictions in format used for competition scoring
output = pd.DataFrame({'Date': X_test.Date,
                       'Value': preds_test})

# we have our prediction in submission.csv file

output.to_csv('submission.csv', index=False)
# to show the prediction
print("Prediction: \n", end = '\n ')
print(output, "\n")
#Actual value
print(X_test_full)