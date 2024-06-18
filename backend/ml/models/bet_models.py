import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, log_loss
from sklearn.model_selection import train_test_split

class BetModel:
    def __init__(self, model, model_name):
        self.model = model
        self.model_name = model_name

    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        self.evaluate(X_test, y_test)

    def evaluate(self, X_test, y_test):
        predictions = self.model.predict(X_test)
        prob_predictions = self.model.predict_proba(X_test)
        accuracy = accuracy_score(y_test, predictions)
        log_loss_value = log_loss(y_test, prob_predictions)
        print(f"Model: {self.model_name}, Accuracy: {accuracy}, Log Loss: {log_loss_value}")

class AgainstTheSpreadModel(BetModel):
    def __init__(self):
        super().__init__(LogisticRegression(), "Against The Spread Model")

class CorrectScoreModel(BetModel):
    def __init__(self):
        super().__init__(RandomForestClassifier(), "Correct Score Model")

class DoubleChanceModel(BetModel):
    def __init__(self):
        super().__init__(LogisticRegression(), "Double Chance Model")

class DoubleResultModel(BetModel):
    def __init__(self):
        super().__init__(RandomForestClassifier(), "Double Result Model")

class EvenMoneyModel(BetModel):
    def __init__(self):
        super().__init__(LogisticRegression(), "Even Money Model")

class ForecastModel(BetModel):
    def __init__(self):
        super().__init__(RandomForestClassifier(), "Forecast Model")

class FuturesModel(BetModel):
    def __init__(self):
        super().__init__(RandomForestClassifier(), "Futures Model")

class GrandSalamiModel(BetModel):
    def __init__(self):
        super().__init__(RandomForestClassifier(), "Grand Salami Model")

class HedgingModel(BetModel):
    def __init__(self):
        super().__init__(LogisticRegression(), "Hedging Model")

class LinesModel(BetModel):
    def __init__(self):
        super().__init__(LogisticRegression(), "Lines Model")

class LiveBettingModel(BetModel):
    def __init__(self):
        super().__init__(RandomForestClassifier(), "Live Betting Model")

class MoneylineModel(BetModel):
    def __init__(self):
        super().__init__(LogisticRegression(), "Moneyline Model")

class OverUndersModel(BetModel):
    def __init__(self):
        super().__init__(LogisticRegression(), "Over/Unders Model")

class ParlayModel(BetModel):
    def __init__(self):
        super().__init__(RandomForestClassifier(), "Parlay Model")

class PickEmModel(BetModel):
    def __init__(self):
        super().__init__(LogisticRegression(), "Pick'Em Model")

class PointSpreadModel(BetModel):
    def __init__(self):
        super().__init__(LogisticRegression(), "Point Spread Model")

class PoolsModel(BetModel):
    def __init__(self):
        super().__init__(RandomForestClassifier(), "Pools Model")

class PropsModel(BetModel):
    def __init__(self):
        super().__init__(RandomForestClassifier(), "Props/Prop Bets Model")

class ReverseForecastModel(BetModel):
    def __init__(self):
        super().__init__(RandomForestClassifier(), "Reverse Forecast Model")

class RoundRobinModel(BetModel):
    def __init__(self):
        super().__init__(RandomForestClassifier(), "Round Robin Model")

class RunLineModel(BetModel):
    def __init__(self):
        super().__init__(LogisticRegression(), "Run Line Model")

class SameGameParlayModel(BetModel):
    def __init__(self):
        super().__init__(RandomForestClassifier(), "Same Game Parlay Model")

class SinglesBetsModel(BetModel):
    def __init__(self):
        super().__init__(LogisticRegression(), "Singles Bets Model")

class TeaserModel(BetModel):
    def __init__(self):
        super().__init__(LogisticRegression(), "Teaser Model")

class TriBetModel(BetModel):
    def __init__(self):
        super().__init__(RandomForestClassifier(), "Tri-Bet/Win-Draw-Win Model")

class WinPlaceModel(BetModel):
    def __init__(self):
        super().__init__(RandomForestClassifier(), "Win/Place Model")
