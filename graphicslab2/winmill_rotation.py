from math import sin,cos,radians
def rotation(vertices,theta):
    
    matrix=[
        [cos(radians(theta)),-sin(radians(theta)),0],
    [sin(radians(theta)),cos(radians(theta)),0],
    [0,0,1]
    ]
    final=[]

    for i in range(len(vertices)):
        test=[]
        vertice=[[vertices[i][0]],[vertices[i][1]],[1]]
        result=[[0],[0],[0]]
        
        for i in range(len(matrix)):
            for j in range(len(vertice[0])):
                for k in range(len(vertice)):
                    result[i][j]+=matrix[i][k]*vertice[k][j]
        
        test.append(result[0][0])
        test.append(result[1][0])
        final.append(test)
    return final


