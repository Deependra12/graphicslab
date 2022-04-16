
def midptellipse(rx, ry, xc, yc):
    x_res=[]
    y_res=[]
    x = 0
    y = ry

    # for region first
    p1 = ((ry * ry) - (rx * rx * ry) +
                (0.25 * rx * rx))
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y


    # For region 1
    while (dx < dy):
        #Appending symetric point to list 
        x_res.append(xc+x)
        y_res.append(yc+y)
        x_res.append(xc-x)
        y_res.append(yc+y)
        x_res.append(xc+x)
        y_res.append(yc-y)
        x_res.append(xc-x)
        y_res.append(yc-y)


        if (p1 < 0):
            x += 1
            dx = dx + (2 * ry * ry)
            p1 = p1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            p1 = p1 + dx - dy + (ry * ry)

    # for region 2
    p2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
    ((rx * rx) * ((y - 1) * (y - 1))) -
    (rx * rx * ry * ry));

    
    while (y >= 0):

    # Appending symetric point to list
        x_res.append(xc+x)
        y_res.append(yc+y)
        x_res.append(xc-x)
        y_res.append(yc+y)
        x_res.append(xc+x)
        y_res.append(yc-y)
        x_res.append(xc-x)
        y_res.append(yc-y)

        
        if (p2 > 0):
            y -= 1
            dy = dy - (2 * rx * rx)
            p2 = p2 + (rx * rx) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            p2 = p2 + dx - dy + (rx * rx)
    return x_res,y_res


