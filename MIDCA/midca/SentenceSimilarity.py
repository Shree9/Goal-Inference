# Program to measure the similarity between
# two sentences using cosine similarity.
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# X = input("Enter first string: ").lower()
# Y = input("Enter second string: ").lower()
X ="Stack the red block on the blue block."
# X ="Pick the red block."
# X ="Unstack the red block on the blue block."
# Y ="Let the red block be placed on the blue block."
Y = "Place the red block on top of the blue block."
# Y = "Deposit red block on the blue block."
# Y = "Connect the bottom of the red block to the top of the blue block."
# Y = "Connect red block to the top of the blue block."
# Y = "Connect red block to the blue block."
# Y = "Collapse the red block from the blue block"
# Y = "Let red and blue blocks be stacked."
# Y = "Put the red and blue blocks together."
# Y = "Bring the red block to the blue block."
# Y = "Can you stack the red block on the blue block?"
# Y = "Can you find the red block and blue block and then put them together?"
# Y = "Now, the red block is on the blue block."
# Y ="Build a tower."
# Y = "Build a tower using red and blue blocks."
# Y = "arrange the red block on the blue block."
# Y= "Unstack the red block on the blue block."
# Y = "Build a tower with red and blue blocks."
# Y = "Elevate the red block and place it on the blue block."

# X = "I am thirsty."
# Y = "I need some water."
# Y = "I need coffee."
# Y = "My mouth is dry."

# tokenization
X_list = word_tokenize(X)
Y_list = word_tokenize(Y)

# sw contains the list of stopwords
sw = stopwords.words('english')
l1 =[];l2 =[]

# remove stop words from the string
X_set = {w for w in X_list if not w in sw}
Y_set = {w for w in Y_list if not w in sw}

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
