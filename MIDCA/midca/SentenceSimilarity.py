# Program to measure the similarity between
# two sentences using cosine similarity.
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string


database = {
              "stack": "stack the blue block on the green block",
              "unstack": "let the green block be separated from the blue block",
              # "unclutter the green block and blue block",
               #"detach the blue block from the green block",
              "pickup": "pick the green block",
              "putdown": "please put down the green block"
            }
# Y1
Y = "Can you find the green block, and blue block and then put them on each other?"
# Y2
# Y = "Now, the red block is on the blue block."
# Y3
# Y = "Connect the blue block to the green block."
# Y4
# Y = "Arrange the blue block on the green block."
# Y5
# Y = "Elevate the blue block and place it on the green block."
# Y6
# Y = "Build a tower with green and blue blocks."
# Y7
# Y = "Detach the bottom of the blue block from the top of the green block."
# Y8
# Y = "Put the green block on your hand"
# Y9
# Y = "Can the green block be lifted?"

# Y = "stack the green block on the blue block"
# Y = "let the green block be separated from the blue block"
# Y = "remove the green block from the blue block"

Y = Y.lower()

for X in database.values():
    print("-------------------------------")
    print(X)
    print(Y)

    # tokenization
    X_list = word_tokenize(X)
    Y_list = word_tokenize(Y)


    # sw contains the list of stopwords
    sw = stopwords.words('english')
    l1 =[];l2 =[]

    # remove stop words from the string
    X_set = {w for w in X_list if not w in sw}
    Y_set =  {w for w in Y_list if not w in sw}

    # form a set containing keywords of both strings
    rvector = X_set.union(Y_set)
    for w in rvector:
        if w in X_set: l1.append(1) # create a vector
        else: l1.append(0)
        if w in Y_set: l2.append(1)
        else: l2.append(0)

    c = 0

    # cosine formula
    for i in range(len(rvector)):
        c+= l1[i]*l2[i]
    cosine = c / float((sum(l1)*sum(l2))**0.5)
    print("similarity: ", cosine)
