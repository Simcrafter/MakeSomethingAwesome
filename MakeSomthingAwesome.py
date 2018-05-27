#importing modules
import math as m

#define functions
#calculates maximum theoretical range of the trebuchet
def distanceCalc(height,velocity):
    
    G=9.82
    distance=0
    
    while height>9.82:
        height-=G
        distance+=velocity
    
    velocity=velocity/10
    G=G/10
    
    while height>0:
        height-=G
        distance+=velocity
    
    return(distance)


#calculates the exit velocity of the trebuchet
def velocityCalc(massCounter,massProjectile,armLegnth,height):
    
    G=9.82
    
    force=(massCounter*G)-(massProjectile*G)
    accelerate=force/massProjectile
    distance=m.sqrt(((armLength**2)*2))
    velocity=(accelerate*distance)/2
    
    return(velocity)

#calculates the impact force of the trebuchet.
def forceCalc(velocity,massProjectile,height,time):
    
    G=9.82
    
    force=(((velocity)+(height*G))*massProjectile)
    
    return(force)
    

#intro
print("This will calculate the maxium range, exit velocity, and flight time of a trebuchet.")

#inputs
armLength=float(input("What is the distance bettwen the pivot and the attachment of the projectile (in meters): "))
massProjectile=float(input("What is the mass of the projectile (in kilograms): "))
massCounter=float(input("What is the mass of the counterweight (in kilograms): "))
height=float(input("What is the height of the pivot point (in meters):"))

#calculating
velocity=velocityCalc(massCounter,massProjectile,armLength,height)
distance=distanceCalc(height,velocity)
time=distance/velocity
impact=forceCalc(velocity,massProjectile,height,time)


#outputs
print("The described trebuchet had a maximum theoretical range of ",distance)
print("The exit velocity of the projectile was",velocity)
print("The flight time of the projectile was",time)
print("The impact force of the projectile was",impact)


