from orbit import ISS
from skyfield.api import load 
 
def add_location(output):
    ''' Writes the current time and location to a specified text file'''
    # Obtain the current time `t`
    t = load.timescale().now()
    # Compute where the ISS is at time `t`
    position = ISS.at(t)
    # Compute the coordinates of the Earth location directly beneath the ISS
    location = position.subpoint()

    file = open(output, 'w')
    file.writelines([location, t])
    file.close()