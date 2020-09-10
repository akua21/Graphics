# Imports
import matplotlib.pyplot as plt
import csv
from csv import writer
from termcolor import colored

# Métodos

def showAllPoints():
    with open('databasePoints.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i, row in enumerate(csv_reader):
            if i != 0:
                plt.scatter(int(row[1]), int(row[2]))

    plt.show()


def showPoint(x, y):
    plt.scatter(int(x), int(y))
    plt.show()


def showAll():

    with open('databaseLines.csv') as csv_file:
        lines = []
        csv_reader = csv.reader(csv_file)
        for i, row in enumerate(csv_reader):
            if i != 0:
                lines.append(row)


    for elem in lines:
        coords = []
        for point in elem:
            coords.append(getCords(point))

        coordsX = [int(coords[0][0]), int(coords[1][0])]
        coordsY = [int(coords[0][1]), int(coords[1][1])]

        plt.plot(coordsX, coordsY)


    info = []
    numRows=0
    with open('databasePoints.csv') as csv_file:
        csv_reader = csv.reader(csv_file)

        for i, row in enumerate(csv_reader):
            if i != 0:
                info.append(row[0])
            numRows+=1

    for point in info:
        coords = getCords(point)

        plt.scatter(int(coords[0]), int(coords[1]))

    plt.show()


def getCords(namePoint):
        info = []
        numRows=0

        with open('databasePoints.csv') as csv_file:
            csv_reader = csv.reader(csv_file)

            for i, row in enumerate(csv_reader):
                if i != 0:
                    info.append(row)
                numRows+=1

            found = False
            i=0
            while i < numRows-1 and found == False:
                if namePoint == info[i][0]:
                    found = True
                    coords = [info[i][1], info[i][2]]
                i+=1

            if found == True:
                return coords
            else:
                print("There isn't a point with that name, please try it again\n")


def addPointDB(name, x, y):
    # Comprobar que no hay otro punto ya en el archivo que se llama igual
    info = []
    numRows=0

    with open('databasePoints.csv') as csv_file:
        csv_reader = csv.reader(csv_file)

        for i, row in enumerate(csv_reader):
            if i != 0:
                info.append(row)
            numRows+=1

        found = False
        i=0
        while i < numRows-1 and found == False:
            if name == info[i][0]:
                found = True
            else:
                i+=1
        if found == False:
            # Escribir el nuevo punto en el archivo
            with open('databasePoints.csv', 'a+', newline='') as csv_file:
                csv_writer = writer(csv_file)
                csv_writer.writerow([name, x, y])
        else:
            print("There is already a point with that name, please choose another one\n")

    return found


def addLineDB(firstPoint, secondPoint):

    with open('databaseLines.csv', 'a+', newline='') as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow([firstPoint, secondPoint])


def clearPointsDB():
    with open('databasePoints.csv', mode='w') as csv_file:
        csv_writer = writer(csv_file)
        head = ['Punto','coord_x','coord_y']
        csv_writer.writerow(head)

    print("Done!\n")


def clearLinesDB():
    with open('databaseLines.csv', mode='w') as csv_file:
        csv_writer = writer(csv_file)
        head = ['Punto X','Punto Y']
        csv_writer.writerow(head)

    print("Done!\n")



varI = None

# Loop
while varI != "exit":

    varI = input("To add a POINT write: "+ colored('Point ','blue')+ colored('point\'s name, coordinate X, coordinate Y ', 'red')+ "(example: "+ colored('Point B, 3, 6', 'green')+ ")\nTo add a LINE write: "+ colored('Line ','blue')+ colored('point\'s name 1, point\'s name 2 ', 'red')+ "(example: "+ colored('Line A, D', 'green')+ ")\n\nTo see all the points write: "+ colored('Show all points','blue')+"\nTo see a single point write: "+ colored('Show point ','blue') + colored('point\'s name ', 'red')+ "(example: "+ colored('Show point A', 'green')+")\nTo see all the points and lines write: "+ colored('Show all','blue')+"\n\nIf you want to CLEAR the DB write: "+ colored('Clear points data base','blue')+" or "+ colored('Clear lines data base','blue')+"\n\nTo CLOSE the program write: "+ colored('exit','yellow')+"\n\n")

    varItype = varI.split(" ")[0]

    varI0 = varI.split(" ")[0]
    if varI0 != 'exit':
        try:
            varI1 = varI.split(" ")[1]
        except:
            print("ERROR formato\n")
        else:

            # ADD POINT
            if varItype == 'Point':
                varIarray = varI.split(",")
                varIlength = len(varIarray)
                if varIlength == 3:
                    try:
                        varIarray[1] = int(varIarray[1])
                        varIarray[2] = int(varIarray[2])
                    except:
                        print("ERROR formato\n")
                    else:
                        coord_x =  varIarray[1]
                        coord_y = varIarray[2]
                        name = varIarray[0].split(" ")[1]
                        found = addPointDB(name, coord_x, coord_y)
                        if found == False:
                            print("Point '",name,"' added!\n")

                else:
                    print("ERROR formato\n")

            # SHOW ALL POINTS

            # SHOW ALL POINTS
            elif varI == 'Show all points':
                showAllPoints()

            # SHOW POINT X
            elif varI0 == 'Show' and varI1 == 'point':
                name = varI.split(" ")[2]
                info = []
                numRows=0
                with open('databasePoints.csv') as csv_file:
                    csv_reader = csv.reader(csv_file)

                    for i, row in enumerate(csv_reader):
                        if i != 0:
                            info.append(row)
                        numRows+=1

                    found = False
                    i=0
                    while i < numRows-1 and found == False:
                        if name == info[i][0]:
                            found = True
                            x = info[i][1]
                            y = info[i][2]
                        i+=1

                    if found == False:
                        print("There isn't a point with that name, please try it again\n")

                    else:
                        showPoint(x, y)

            # ADD LINE
            elif varItype == 'Line':
                varIarray = varI.split(", ")
                varIlength = len(varIarray)
                if varIlength == 2:

                    firstPoint = varIarray[0].split(" ")[1]
                    secondPoint = varIarray[1]

                    info = []
                    numRows=0
                    with open('databasePoints.csv') as csv_file:
                        csv_reader = csv.reader(csv_file)

                        for i, row in enumerate(csv_reader):
                            if i != 0:
                                info.append(row)
                            numRows+=1

                        found1 = False
                        found2 = False
                        i=0
                        while i < numRows-1 and (found1 == False or found2 == False):
                            if firstPoint == info[i][0]:
                                found1 = True
                                x1 = info[i][1]
                                y1 = info[i][2]
                            elif secondPoint == info[i][0]:
                                found2 = True
                                x2 = info[i][1]
                                y2 = info[i][2]
                            i+=1
                        if found1 == False:
                            print("Point '",firstPoint,"' doesn't exit\n")
                        if found2 == False:
                            print("Point '",secondPoint,"' doesn't exit\n")
                        if found1 == True and found2 == True:
                            addLineDB(firstPoint, secondPoint)
                            print("Line between '",firstPoint,"and",secondPoint,"' added!\n")

                else:
                    print("ERROR formato\n")

            # SHOW ALL
            elif varI == 'Show all':
                showAll()

            # CLEAR POINTS DB
            elif varI == 'Clear points data base':
                clearPointsDB()

            # CLEAR LINES DB
            elif varI == 'Clear lines data base':
                clearLinesDB()

            else:
                if varI != "exit":
                    print("ERROR formato\n")




print("Goodbye!")
