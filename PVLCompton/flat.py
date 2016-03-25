import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create('54.250.155.29')
pos = mc.player.getTilePos()
mc.setBlocks(pos.x, pos.y, pos.z, pos.x+200, pos.y+0, pos.z+200, block.DIRT.id)
