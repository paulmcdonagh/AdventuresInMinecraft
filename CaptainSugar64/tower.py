import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create('54.250.155.29')
pos = mc.player.getTilePos()
for a in range(50):
     mc.setBlock(pos.x, pos.y+a, pos.z, block.SNOW_BLOCK.id)