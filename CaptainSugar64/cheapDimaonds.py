import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create('54.250.155.29')


while True:
    pos = mc.player.getTilePos()
    time.sleep(1)
    mc.setBlock(pos.x+3, pos.y, pos.z, block.DIAMOND_BLOCK.id)
