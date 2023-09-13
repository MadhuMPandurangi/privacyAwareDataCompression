import RLZ
import getDataFromDict
# opening both the files in reading modes
referenceFile = "dict1.zst"
inputFile = "dict2.zst"

S = getDataFromDict.getData(referenceFile)
T = getDataFromDict.getData(inputFile)

# # calling factorise function to create factors
# factors = RLZ.factorise(T, S)
# print(factors)


# # call addToRefDict to merge texts with less than the threshold length(tl)
# th_length = 1
# S = RLZ.addToRefDict(T, S, factors, th_length)


# # write merged data to reference file
# with open('referenceFile.txt', 'w') as file:
#     file.write(S)



