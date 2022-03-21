'''library of commands to write data to files''' 

def writeCSV(fileName : str, data : str):
    '''writes data into a csv in the current direcory comprised of the input string '''
    csv = open("{},csv".format(fileName), "w")
    csv.write(data)
    csv.close()


def appendCSV(fileName : str, data : str):
    '''appends data into a csv in the current direcory comprised of the input string '''
    csv = open("{},csv".format(fileName), "a")
    csv.write(data)
    csv.close()

