#importing modules
import math as m

#definine globals
G=9.82
pi=3.14159265359

#define functions
def distanceCalc(height,velocityV,velocityH):
    
    global G
    distance=0
    
    while height>9.82:
        velocityV-=G
        height+=velocityV
        distance+=velocityH
    
    velocityV=velocityV/10
    velocityH=velocityH/10
    g=9.82/10
    
    while height>0:
        velocityV-=G
        height+=velocityV
        distance+=velocityH
    
    return(distance)


def velocityCalc(massCounter,massProjectile,armLegnth,height):
    
    global G
    global pi
    velocity=0
    
    force=(massCounter*G)-(massProjectile*G)
    accelerate=force/massProjectile
    distance=(2*armLegnth)*pi
    for i in range(0,int(distance*10)):
        velocity+=(accelerate/10)
    
    return(velocity)

def velocityVCalc(velocity,releaseAngle):
    
    velocityV=velocity*(releaseAngle/90)
    
    return(velocityV)
    
def velocityHCalc(velocity,velocityV):
    
    velocityH=velocity-velocityV
    
    return(velocityH)

def forceCalc(velocity,massProjectile,height,time):

    global G
    
    force=(((velocity)+(height*G))*massProjectile)
    
    return(force)
    

#intro
print("This will calculate the maxium range, exit velocity, and flight time of a trebuchet.")

#inputs
armLength=float(input("What is the distance between the pivot and the attachment of the projectile (in meters): "))
massProjectile=float(input("What is the mass of the projectile (in kilograms): "))
massCounter=float(input("What is the mass of the counterweight (in kilograms): "))
height=float(input("What is the height of the pivot point (in meters):"))
releaseAngle=float(input("What is the release angle of the projecttile (projectile velocity elevaion from ground, 37.5 is ideal, above 45 is not recomended):"))

#calculating
velocity=velocityCalc(massCounter,massProjectile,armLength,height)
velocityV=velocityVCalc(velocity,releaseAngle)
velocityH=velocityHCalc(velocity,velocityV)
distance=distanceCalc(height,velocityV,velocityH)
time=distance/velocity
impact=forceCalc(velocity,massProjectile,height,time)


#outputs
print("The described trebuchet had a maximum theoretical range of ",distance,"meters.")
print("The exit velocity of the projectile was",velocity,"meters per second.")
print("The flight time of the projectile was",time,"seconds.")
print("The impact force of the projectile was",impact,"Newtons")


