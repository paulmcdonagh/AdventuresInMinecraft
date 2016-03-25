import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create('54.250.155.29')
pos = mc.player.getTilePos()

mc.setBlock(pos.x+3, pos.y, pos.z, block.DIAMOND_BLOCK.id)
mc.setBlock(pos.x+3, pos.y+2, pos.z,  block.DIAMOND_BLOCK.id)
mc.setBlock(pos.x+3, pos.y+4, pos.z,  block.DIAMOND_BLOCK.id)
mc.setBlock(pos.x+3, pos.y, pos.z+4,  block.DIAMOND_BLOCK.id)
mc.setBlock(pos.x+3, pos.y+2, pos.z+4,  block.DIAMOND_BLOCK.id)
mc.setBlock(pos.x+3, pos.y+4, pos.z+4,  block.DIAMOND_BLOCK.id)
