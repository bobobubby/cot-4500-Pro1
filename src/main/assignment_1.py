import math

def main():
    approximation()
    bisection(10 ** -3, 1, 2, 12)
    fixedPoint(1.5, 0.000001, 50)
    newtonRaphson(math.pi / 4, 0.000001, 20)

def approximation():
    upper = 1.5
    tolerance = 0.000001

    iter = 0;
    diff = upper
    x = upper

    print(iter, " : ", x)

    while diff>= tolerance:
        iter = iter + 1
        y = x

        x = (x/2) + (1/x)
        print(iter, " : ", x)

        diff = abs(x-y)

    print("Convergence after ",iter," iterations\n")

def bisection(tol,left,right,max):
    i = 0
    while abs(right-left)>tol and i<max:

        i = i+1
        p = (left+right)/2
        print(i, " : ", p)
        if ((biFunction(left)<0) and (biFunction(p)>0)) or ((biFunction(left)>0) and (biFunction(p)<0)):
            right = p
        else:
            left = p
    print("Convergence after ", i, " iterations\n")

def fixedPoint(init,tol,N):
    i = 1
    while i<= N:
        #p = init-biFunction(init) #equation 1
        p = ((10-init*init*init)**0.5)/2 #equation 2
        print(i," : ",p)
        if abs(p-init)<tol:
            print("Success after ",i," iterations\n")
            return
        i = i+1
        init = p
    print("Result diverges")
    print("Failure after ",i," iterations\n")
    return

def newtonRaphson(pPrev,tol,N):
    i=1
    print("iter ", 0, " ", pPrev)
    while i <= N:
        if -math.sin(pPrev)-1 != 0:
            pNext = pPrev-(math.cos(pPrev)-pPrev)/(-math.sin(pPrev)-1)
            print("iter ", i, " ", pNext)
            if abs(pNext-pPrev)<tol:
                #print(pNext," done")
                return
            #print("iter ",i, " ",pPrev)
            i = i+1
            pPrev=pNext
        else:
            print("unsuccessful")
    print("max iterations performed")


def biFunction(x):
    return x*x*x+4*x*x-10