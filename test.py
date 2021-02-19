elements = [1,2,3,4,5,6,7,8,9]
absolute_difference = [abs(i-j) for i in elements for j in elements]
print(max(absolute_difference))
