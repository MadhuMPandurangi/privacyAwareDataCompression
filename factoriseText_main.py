import RLZ
import getDataFromDict
# opening both the files in reading modes
referenceFile = "dict1.zst"
inputFile = "dict2.zst"

refFileData, metaData = getDataFromDict.getData(referenceFile)
inputFileData, _ = getDataFromDict.getData(inputFile)

print(refFileData)
print("\n")
print(inputFileData)
print("\n")
# calling factorise function to create factors
factors = RLZ.factorise(inputFileData, refFileData)
print(factors)


# call addToRefDict to merge texts with less than the threshold length(tl)
th_length = 2
mergedData = RLZ.addToRefDict(inputFileData, refFileData, factors, th_length)

# convert to bytes
mergedDataInBytes = mergedData.encode('utf-16')
print("\nmerged data in bytes format")
print(mergedDataInBytes)

# convert meta data from string to bytes
metaDataInBytes = metaData.encode('utf-16')
print("\n metaData in bytes fromat")
print(metaDataInBytes)
# print(metaDataInBytes)
# print(type(metaDataInBytes))

finalData = metaDataInBytes + mergedDataInBytes


# write merged data to reference file
with open('answerDict.zst', 'wb') as file:
    file.write(finalData)



