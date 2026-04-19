import numpy as np

scores = np.random.randint(0, 100, (10, 3))  
categories = np.array(["train", "value", "test", "train", "test", 
                       "value", "train", "train", "test", "value"])

train_filtered = scores[categories == "train"]

# print(scores)
print(train_filtered)

mask = (categories == "train") & (scores[:,0] > 0.5)
filtered = scores[mask]
filtered = train_filtered[(train_filtered[:,0]>50)]
print(train_filtered)
print("bigger making")
print(filtered)
