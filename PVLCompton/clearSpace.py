import mcpi.minecraft
import mcpi.block as block
mc = mcpi.minecraft.Minecraft.create('54.250.155.29')
pos = mc.player.getTilePos()
mc.setBlocks(pos.x, pos.y, pos.z, pos.x+50, pos.y+50, pos.z+50, block.AIR.id)
