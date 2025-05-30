# In this project, you will use regression models to predict the number of days a customer rents DVDs for.

## As with most data science projects, we will need to pre-process the data provided, in this case, a csv file called `dvd_rental_infos.csv`. Specifically:

### 1. Read in the csv file rental_info.csv using pandas.
### 2. Create a column named "rental_length_days" using the columns "return_date" and "rental_date", and add it to the pandas DataFrame. This column should contain information on how many days a DVD has been rented by a customer.
### 3. Create two columns of dummy variables from "special_features", which takes the value of 1 when:
- The value is "Deleted Scenes", storing as a column called "deleted_scenes".
- The value is "Behind the Scenes", storing as a column called "behind_the_scenes".
### 4. Make a pandas DataFrame called X containing all the appropriate features you can use to run the regression models, avoiding columns that leak data about the target.
### 5. Choose the "rental_length_days" as the target column and save it as a pandas Series called y.
### 6. Split the data into X_train, y_train, X_test, and y_test train and test sets, avoiding any features that leak data about the target variable, and include 20% of the total data in the test set.
Set random_state to 9 whenever you use a function/method involving randomness, for example, when doing a test-train split.
Recommend a model yielding a mean squared error (MSE) less than 3 on the test set

### 7. Save the model you would recommend as a variable named best_model, and save its MSE on the test set as best_mse.
