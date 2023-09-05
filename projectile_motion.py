#importing the required libraries
import math 
import matplotlib.pyplot as plt

g = 9.81 #defining the constant of gravity for further usage

#getting the rquired variables from the user
throwing_speed = float(input("Please enter the throwing speed: "))
throwing_height = float(input("Please enter the height of the ball in the beginning: "))
alfa_angle = float(input("Please enter with which angle the ball is thrown: "))

#calculating the vertical and horizontal speed components
x_speed = throwing_speed * math.cos(math.radians(alfa_angle))
y_speed = throwing_speed * math.sin(math.radians(alfa_angle))

#calculating how long will the ball go up
up_time = y_speed / g

#calculating the maximal height the ball will reach
maximal_height = throwing_height + y_speed * up_time - g * up_time ** 2 / 2

#calculating how long it will take for the ball to fall from the maximum height point
fall_time = math.sqrt(2 * maximal_height / g)

#calculating the total time of the motion
total_time = up_time + fall_time

#calculating the distance covered in x-axis
x_distance = x_speed * total_time

#calculating the y component of the speed when the ball hits the ground
y_fall_speed = fall_time * g

#calculating the total speed when the ball hits the ground
fall_speed = math.sqrt(y_fall_speed**2 + x_speed**2)

#Forming a string variable for the answer and printing it
solution = """
The motion will take {} seconds
The ball will reach maximum {} meters high
The ball will cover {} meters in x-axis
The ball will hit the ground with the speed {} meters per second
""".format(round(total_time,2),round(maximal_height,2),round(x_distance,2),round(fall_speed,2))

print(solution)

#defining lists for the values to use for plotting graphs
xList = []
yList = []
time_List = []
speed_List = []

tstep = 0.001 #step in which the values will be calculated (smaller steps will make the graphs more precise)

#filling the lists to plot graphes
t = 0 
while t <= total_time:
    xList.append(t*x_speed)
    yList.append(throwing_height + y_speed * t - (g * t**2 / 2))
    time_List.append(t)

    if t <= up_time:
        y_moment_speed = y_speed - g*t
    else:
        y_moment_speed = (t-up_time) * g
    moment_speed = math.sqrt(x_speed**2 + y_moment_speed**2)
    speed_List.append(moment_speed)
    
    t += tstep

#creating the graphs using pyplot
plt.subplot(2,1,1)
plt.plot(xList,yList,"green")
plt.title("Movement")
plt.xlabel("x-axis (m)")
plt.ylabel("y-axis (m)")

plt.subplot(2,1,2)
plt.plot(time_List,speed_List,"blue")
plt.title("Time - Velocity")
plt.xlabel("time (s)")
plt.ylabel("velocity (m/s)")

plt.show()