{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8aedb75-7a3b-44af-bd7b-0cbb92f75e63",
   "metadata": {},
   "outputs": [],
   "source": [
    "#datashet : The MNIST database of handwritten digits\n",
    "\n",
    "from sklearn.datasets import fetch_openml\n",
    "\n",
    "X, y = fetch_openml ('mnist_784', data_home='./dataset/mnist', return_X_y=True)\n",
    "X.shape \n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib.cm as cm\n",
    "import numpy as np\n",
    "\n",
    "pos = 1 \n",
    "for data in X[:8]:\n",
    "    plt.subplot(1, 8, pos)\n",
    "    plt.imshow(data.reshape((28, 28)), \n",
    "    cmap = cm.Greys_r)\n",
    "    plt.axis('off')\n",
    "    pos += 1\n",
    "\n",
    "    plt.show()\n",
    "\n",
    "y[:8]\n",
    "\n",
    "#X_train = X[:6000]\n",
    "#y_train = y[:6000]\n",
    "#X_test = X[6000:]\n",
    "#y_test = y[6000:]\n",
    "\n",
    "X_train = X[:1000]\n",
    "y_train = y[:1000]\n",
    "X_test = X[69000:]\n",
    "y_test = y[69000:]\n",
    "\n",
    "#clasification dengan SVC (Support Vector Classifer)\n",
    "from sklearn.svm import SVC\n",
    "model = SVC(random_state=0)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "from sklearn.metrics import classification_report\n",
    "\n",
    "y_pred = model.predict(X_test)\n",
    "print(classification_report(y_test, y_pred))\n",
    "\n",
    "#Hyperparameter Tuning dengan GridSearchCV\n",
    "from sklearn.model_selection import GridSearchCV\n",
    "\n",
    "parameters = {\n",
    "    'kernel' : ['rbf', 'poly', 'sigmoid'],\n",
    "    'C' : [0.5, 1, 10, 100],\n",
    "    'gamma' : ['scale', 1, 0.1, 0.01, 0.001]\n",
    "}\n",
    "\n",
    "grid_search = GridSearchCV(estimator=SVC(random_state=0),\n",
    "param_grid = parameters,\n",
    "n_jobs=6,\n",
    "verbose=1,\n",
    "scoring='accuracy')\n",
    "grid_search.fit(X_train, y_train)\n",
    "\n",
    "print(f'Best Score: {grid_search.best_score_}')\n",
    "\n",
    "best_params = grid_search.best_estimator_.get_params()\n",
    "print(f'Best Parameters:')\n",
    "for param in parameters :\n",
    "    print(f'\\t{param}: {best_params[param]}')\n",
    "\n",
    "#Predict & Evaluate\n",
    "y_pred = grid_search.predict(X_test)\n",
    "print(classification_report(y_test, y_pred))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
