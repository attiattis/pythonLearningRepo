def readsData(outfile):
    '''this method will read the data, return the list of lines'''
    data = outfile.read().split("\n")
    return data

def searchForMatch(selectedItem, lines):
    # iterate through the lines
    for line in lines:
        # split the line and store it into a temporary variable
        temp = line.split(" ")
        # check if the selectedItem is present in that 
        if selectedItem in temp:
            # the item is present in this, so print other details of this line
            if temp[0] == selectedItem:
                # print the other two items
                print("Bond Energy: ",temp[1],"  Bond Length: ",temp[2])
            elif temp[1] == selectedItem:
                print("Bond Type: ",temp[0],"  Bond Length: ",temp[2])
            elif temp[2] == selectedItem:
                print("Bond Type:",temp[0], "  Bond Energy: ",temp[1])

def main():
    # OPEN THE FILE
    outfile = open("data.txt")
    # call the method to read the data
    lines = readsData(outfile)
    outfile.close()

    while True:
        # read the search item from the user.
        
        selectedItem = input("What do you want to look for (blank t0 quit)? ")
        
        # check if the input value is the new line or not
        if not selectedItem :
            break
        else:
            # call the function to search
            searchForMatch(selectedItem, lines)


main()