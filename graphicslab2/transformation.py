import math
def reflection(vertices,axis):
    print(axis)
    if axis=='x_axis':
        matrix=[[1,0,0],
        [0,-1,0],
        [0,0,1]
        ]
    elif axis=='y_xis':
        matrix=[[-1,0,0],
        [0,1,0],
        [0,0,1]
        ]
    elif axis=='origin':
        matrix=[[-1,0,0],
        [0,-1,0],
        [0,0,1]
        ]


    x_res=[]
    y_res=[]
    for i in range(len(vertices)):
        vertice=[[vertices[i][0]],[vertices[i][1]],[1]]
        result=[[0],[0],[0]]
        
        for i in range(len(matrix)):
            for j in range(len(vertice[0])):
                for k in range(len(vertice)):
                    result[i][j]+=matrix[i][k]*vertice[k][j]
        x_res.append(result[0][0])
        y_res.append(result[1][0])
    
    return(x_res,y_res)

def rotation(vertices,theta):
    theta=math.radians(theta)
    matrix=[[math.cos(theta),-math.sin(theta),0],
    [math.sin(theta),math.cos(theta),0],
    [0,0,1]
    ]
    x_res=[]
    y_res=[]
    for i in range(len(vertices)):
        vertice=[[vertices[i][0]],[vertices[i][1]],[1]]
        result=[[0],[0],[0]]
        
        for i in range(len(matrix)):
            for j in range(len(vertice[0])):
                for k in range(len(vertice)):
                    result[i][j]+=matrix[i][k]*vertice[k][j]
        x_res.append(result[0][0])
        y_res.append(result[1][0])
    
    return(x_res,y_res)



def shearing(vertices,axis,sh):
    print(axis)
    if axis=='x_axis':
        matrix=[[1,sh,0],
        [0,1,0],
        [0,0,1]
        ]
    elif axis=='y_axis':
        matrix=[[1,0,0],
        [sh,1,0],
        [0,0,1]
        ]
    


    x_res=[]
    y_res=[]
    for i in range(len(vertices)):
        vertice=[[vertices[i][0]],[vertices[i][1]],[1]]
        result=[[0],[0],[0]]
        
        for i in range(len(matrix)):
            for j in range(len(vertice[0])):
                for k in range(len(vertice)):
                    result[i][j]+=matrix[i][k]*vertice[k][j]
        x_res.append(result[0][0])
        y_res.append(result[1][0])
    
    return(x_res,y_res)


def translation(vertices,tx,ty):
    matrix=[[1,0,tx],
    [0,1,ty],
    [0,0,1]
    ]
    x_res=[]
    y_res=[]
    for i in range(len(vertices)):
        vertice=[[vertices[i][0]],[vertices[i][1]],[1]]
        result=[[0],[0],[0]]
        
        for i in range(len(matrix)):
            for j in range(len(vertice[0])):
                for k in range(len(vertice)):
                    result[i][j]+=matrix[i][k]*vertice[k][j]
        x_res.append(result[0][0])
        y_res.append(result[1][0])
    
    return(x_res,y_res)


def scaling(vertices,sx,sy):
    matrix=[[sx,0,0],
    [0,sy,0],
    [0,0,1]
    ]
    x_res=[]
    y_res=[]
    for i in range(len(vertices)):
        vertice=[[vertices[i][0]],[vertices[i][1]],[1]]
        result=[[0],[0],[0]]
        
        for i in range(len(matrix)):
            for j in range(len(vertice[0])):
                for k in range(len(vertice)):
                    result[i][j]+=matrix[i][k]*vertice[k][j]
        x_res.append(result[0][0])
        y_res.append(result[1][0])
    
    return(x_res,y_res)

