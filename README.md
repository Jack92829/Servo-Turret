# Servo-Turret
A small servo-turret that can be controlled remotely through a local website hosted on your network.  
An example can be seen *[here](https://www.reddit.com/r/raspberry_pi/comments/i4k69j/trackpad_controlled_servo_motors/#here "yep right here")*.

## Setup
### Server
Find your current network IP and insert that into the relevant places labelled in the Server.js and Pi-Side.py files

### Pi
Setup the servos on a breadboard as seen below
![Alt Text](https://github.com/Jack92829/Servo-Turret/blob/pi-info/65118D30-80D6-44CB-8CD5-2ED76DBC9FA7.png)

<p>The left side is ground, and the right is power.</p>
<p>Connect a wire from the left hand side to pin 6 or a ground pin of your choice.</p>
<p>Next connect a wire from the right hand side to pin 4 or pin 2.</p>
<p>Next connect white wire from the X-axis servo to pin 12.</p>
<p>And finally connect the white wire from the Y-axis servo to pin 11.</p>

<p>Note that these are just the pins i chose when writing the code, feel free to modify the code and pins accordingly if you would like.</p>
