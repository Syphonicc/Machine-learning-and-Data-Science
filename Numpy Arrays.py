import numpy as np
# w1 = 0.3
# w2 = 0.2
# w3 = 0.5
#
# kanto = np.array([73, 67, 43])
# weights = np.array([w1, w2, w3])

#numpy arrays support arithmetic operators
#These operations would not have been possible with standard python lists
#So we have element wise multiplication and sum of two arrays
#print(kanto * weights)

#Python lists
arr1 = list(range(1000000))
arr2 = list(range(1000000, 2000000))

#Numpy arrays
arr1_np = np.array(arr1)
arr2_np = np.array(arr2)

#Multi-dimensional Numpy array

#climate_data = np.array([[73,67,43],
                        # [91,88,64],
                        #  [87,134,58],
                        #  [102,43,37],
                        #  [69,96,70]])
#A numpy array can have any number of dimensions
# we can use .shape to find out about the array for the above it will
# print (5, 3) meaning 5 rows and 3 columns
# All the elements in a numpy array have the same datatype.You can check the data type of an array
# using the .dtype property
#if an array contains even a single floating point number then all the other
# numbers also become floating point numbers
# @ = matrix multiplication charecter
# CSV = comma separated value

climate_data = np.genfromtxt('climate.csv', delimiter= ',', skip_header=1)
weights = np.array([0.3, 0.2, 0.5])

yields = climate_data @ weights

#print(yields.shape)
# We can now add yields back to climate_data as a fourth column using the np.concatenate function
climate_results = np.concatenate((climate_data , yields.reshape(10000, 1)), axis=1)
#by default axis is 0 which will add a row we want to add a column here
#print(climate_results)
#np.savetxt = The results are written back in the CSV format to the file climate_results.txt
np.savetxt('climate_results.txt',
           climate_results,
           fmt = '%.2f',
           header = 'temperature, rainfall, humidity, yield_apples',
           comments = '')
#print(open('climate_results.txt' , 'r').read())

#Numpy arrays also support brodcasting, which allows arthmetic operations between two array
#having a different number of dimensions, but compatible shapes
#Broadcasting only works if one of the array can be replicated to exactly match the shape of the other array
#in a boolean of arrays , 1 = True , 0 = False



