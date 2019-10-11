def scaleRotate(z,alpha, tau):
    real = z.real
    img = z.imag
    r = math.sqrt((real*real)+(img*img))
    t = math.atan(img/real)
    t += tau
    x = r*(math.cos(t))
    y = r*(math.sin(t))
    z = complex(x,y)
    return z #return a complex number