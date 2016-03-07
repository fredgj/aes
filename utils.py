# Just a couple utility functions used by AES

# Divides a list into chunks of size n
def chunkify(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]


# Rotates a vector left so [a,b,c,d] => [b,c,d,a]
def rotate(vector):
    tmp = vector[0]

    for i in range(len(vector)-1):
        vector[i] = vector[i+1]

    vector[len(vector)-1] = tmp
    return vector

