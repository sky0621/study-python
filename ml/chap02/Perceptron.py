import numpy as np

"""
eta : float 学習率（0.0 to 1.0）
n_iter : int トレーニングデータのトレーニング回数

w_ : １次元配列（適合後の重み）
errors_ : リスト（各エポックでの誤分類数）
"""
class Perceptron(object):
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    """
        [配列のようなデータ構造]
        X : shape = [n_samples, n_features] トレーニングデータ
        y : shape = [n_samples] 目的変数
    """
    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)
