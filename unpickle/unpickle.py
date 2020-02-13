import pickle

with open ('filename.pkl', 'rb') as f:
    data = pickle.load(f)

print(data)

