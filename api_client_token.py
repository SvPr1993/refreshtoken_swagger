import pickle

with open("token.pickle", "rb") as file:
    token_load = pickle.load(file)
    print(token_load)
