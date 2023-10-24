import math

#multiply 3D vector by 4x4 matrix
def MultiplyMatrixVector(input, matrix):
    output = [0, 0, 0]
    w = 0
    output[0] = input[0] * matrix[0][0] + input[1] * matrix[1][0] + input[2] * matrix[2][0] + matrix[3][0]
    output[1] = input[0] * matrix[0][1] + input[1] * matrix[1][1] + input[2] * matrix[2][1] + matrix[3][1]
    output[2] = input[0] * matrix[0][2] + input[1] * matrix[1][2] + input[2] * matrix[2][2] + matrix[3][2]
    w = input[0] * matrix[0][3] + input[1] * matrix[1][3] + input[2] * matrix[2][3] + matrix[3][3]

    if w != 0:
        output[0] /= w
        output[1] /= w
        output[2] /= w
    return(output)

def calculateNormal(input):
    
    output = [0, 0, 0]
    line1 = [0, 0, 0]
    line2 = [0, 0, 0]

    #calculate lines
    line1[0] = input[1][0] - input[0][0]
    line1[1] = input[1][1] - input[0][1]
    line1[2] = input[1][2] - input[0][2]
    
    line2[0] = input[2][0] - input[0][0]
    line2[1] = input[2][1] - input[0][1]
    line2[2] = input[2][2] - input[0][2]

    #cross product
    output[0] = line1[1] * line2[2] - line1[2] * line2[1]
    output[1] = line1[2] * line2[0] - line1[0] * line2[2]
    output[2] = line1[0] * line2[1] - line1[1] * line2[0]

    return(output)

def normalizeVector(input):
    output = [0, 0, 0]
    #calculate length of normal
    length = math.sqrt(input[0] * input[0] + input[1] * input[1] + input[2] * input[2])

    #normalize normal
    if length != 0:
        output[0] = input[0] / length
        output[1] = input[1] / length
        output[2] = input[2] / length
        return(output)
    else:
        return(input)


def dotProduct(input1, input2):
    output = input1[0] * input2[0] + input1[1] * input2[1] + input1[2] * input2[2]
    return(output)

def createMeshFromOBJ(path):
    file = open(path)
    vectors = [[0, 0, 0]]
    mesh = []
    for line in file:
        if line[0] == "v":
            tempLine = line.split()
            tempVector = [0.0, 0.0, 0.0]
            tempVector[0] = float(tempLine[1])
            tempVector[1] = float(tempLine[2])
            tempVector[2] = float(tempLine[3])
            vectors.append(tempVector)
        elif line[0] == "f":
            tempLine = line.split()
            tempTri = [0.0, 0.0, 0.0]
            tempTri[0] = vectors[int(tempLine[1])]
            tempTri[1] = vectors[int(tempLine[2])]
            tempTri[2] = vectors[int(tempLine[3])]
            mesh.append(tempTri)
    return(mesh)

def sortByAverageZ(tri):
    sum = tri[0][2] + tri[1][2] + tri[2][2]
    average = sum / 3
    return(average)