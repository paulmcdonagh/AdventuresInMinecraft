#!/usr/bin/env python

# Adventure 2: rent.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program is a game using geo-fencing.
# You are challenged to collect objects from a field in the shortest
# time possible. All the time you are in the field you are charged
# rent. You have to collect/destroy blocks by spending the minimum
# amount of rent. If you stay in the field for too long, your player
# is catapulted up into the sky and out of the field, which makes the
# game harder to play and much more fun!

# Import built-in Python modules
import time
import sys

# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block

if __name__ == '__main__':

    ipAddress = None
    myEntityId = None
    mc = None
    size = None
    rentalPeriod = None

    if len(sys.argv) != 5:
        print "Usage: rent.py ipaddress name size rentalTime"
        exit()
    else:
        ipAddress = sys.argv[1]
        mc = minecraft.Minecraft.create(ipAddress)
        myEntityId = mc.getPlayerEntityId(sys.argv[2])
        size = sys.argv[3]
        rentalPeriod = sys.argv[4]

    pos = mc.entity.getTilePos(myEntityId)

    # Define constants for the 4 coordinates of the geo-fence
    X1 = pos.x
    Z1 = pos.z
    X2 = pos.x + int(size)
    Z2 = pos.z + int(size)
    Y = pos.y

    # Constants for the place to move through when catapulted!
    HOME_X = X2 + 2
    HOME_Y = 10 # up in the sky
    HOME_Z = Z2 + 2

    # A variable to keep a tally of how much rent you have been charged
    rent = 0

    # A variable to hold the number of seconds the player is in the field
    inField = 0
    print "Geofence built with coordinates " + "(" + str(X1) + "," + str(Z1) + ")" + "(" + str(X1) + "," + str(Z2) + ")" + \
          "(" + str(X2) + "," + str(Z1) + ")" + "(" + str(X2) + "," + str(Z2) + ")"
    # The main game loop ticks round once every second



    try:
        # Create torches at the corner of the field
        mc.setBlock(X1, Y, Z1, block.TORCH.id)
        mc.setBlock(X1, Y, Z2, block.TORCH.id)
        mc.setBlock(X2, Y, Z1, block.TORCH.id)
        mc.setBlock(X2, Y, Z2, block.TORCH.id)
        print "You are now a landlord"

        while True:
            # Slow the program down a bit, this also helps with timing things
            time.sleep(float(rentalPeriod)) # the loop runs once every second

            # Get each of the players position
            players = mc.getPlayerEntityIds()
            for player in players:
                pos = mc.entity.getTilePos(player)

                if player == myEntityId and  pos.x>X1 and pos.x<X2 and pos.z>Z1 and pos.z < Z2:
                    print "You are inside your Geofence"
                    continue

            # If the player is in the field, charge him rent
                if pos.x>X1 and pos.x<X2 and pos.z>Z1 and pos.z < Z2:
                    # Charge 1 rent every time round the loop (1sec per loop)
                    rent = rent + 1
                    # Tell player how much rent they owe
                    mc.postToChat("You owe HyggeCrafter rent: $" + str(rent))
                    # Count number of seconds player is in the field (1sec per loop)
                    inField = inField + 1
                else:
                    # Not inside the field...
                    inField = 0 # ...so reset the counter to zero

                # If player in field for more that 3 seconds...
                if inField > 3:
                    mc.postToChat("Too slow to get off my land!")
                    # ...catapult player outside of the field
                    mc.entity.setPos(player, HOME_X, HOME_Y, HOME_Z)

    finally:
        mc.setBlock(X1, Y, Z1, block.AIR.id)
        mc.setBlock(X1, Y, Z2, block.AIR.id)
        mc.setBlock(X2, Y, Z1, block.AIR.id)
        mc.setBlock(X2, Y, Z2, block.AIR.id)

# END
