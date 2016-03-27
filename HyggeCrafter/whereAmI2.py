import mcpi.minecraft as minecraft
from time import sleep


mc = minecraft.Minecraft.create('54.250.155.29')
while True:
    sleep(1)
    pos = mc.player.getPos()
    print str(pos.x) + " " + str(pos.y) + " " + str(pos.z)


