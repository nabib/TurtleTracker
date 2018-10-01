# ARGOSQueryTool.py
#
# Description: Parses a line of ARGOS tracking data
#
# Created by: Nicole Abib (nicole.abib@duke.edu)
# Created on: Sept, 2018

# Create a variable pointing to the file with no header
fileName = "SaraNoHeader.txt"

# Open the file as a read-only file object
fileObj = open(fileName, 'r')

# Read in all lines in the text file into a list variable
lineStrings = fileObj.readlines()
#lineStringsNoHeader = lineStrings[1:len(lineStrings)]
print("There are {} records in the file".format(len(lineStrings)))
      
# Close the file
fileObj.close()

# Create empty dictionaries
dateDict = {}
locationDict = {}

# Loop through the lines until all lines have been read
for lineString in lineStrings:
    # Use the split command to parse the items in lineString into a list object
    lineData = lineString.split("\t")

    # Assign variables to specfic items in the list
    recordID = lineData[0]              # ARGOS tracking record ID
    obsDateTime = lineData[2]           # Observation date and time (combined)
    obsDate = obsDateTime.split()[0]    # Observation date - first item in obsDateTime list object
    obsTime = obsDateTime.split()[1]    # Observation time - second item in obsDateTime list object
    obsLC = lineData[3]                 # Observation Location Class
    obsLat = lineData[5]                # Observation Latitude
    obsLon = lineData[6]                # Observation Longitude

    # Filter records that get added to the dictionary
    if obsLC in ("1","2","3"):
        # Add values to dictionary
        dateDict[recordID] = obsDate
        locationDict[recordID] = (obsLon,obsLat)

# Ask user for date, specifying the format
userDate = input("Enter a date (M/D/YYYY):")

# Create empty key list
keyList = []

# Loop through all key, value pairs in the dateDictionary
for k, v in dateDict.items():
    # See if date matches the user date
    if v == userDate:
        keyList.append(k)

# Check that at least one key was returned
if len(keyList) == 0:
    print("No observations returned for {}".format(userDate))
else:
    # Loop through each key and report the date's associated location
    for k in keyList:
        theDate = dateDict[k]
        theLocation = locationDict[k]
        theLat = theLocation[1]
        theLon = theLocation[0]
        print("Record {0}: Sara was seen at {1}N,{2}W, on {3}".format(k,theLat,theLon,theDate))


