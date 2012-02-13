import random

import settings



# Check level dimensies.
#
# Elk level moet vierkant zijn en opsplitsbaar zijn in blocks van grootte BLOCK_SIZE.
#
assert(settings.LEVEL_WIDTH % settings.BLOCK_SIZE == 0)
assert(settings.LEVEL_HEIGHT % settings.BLOCK_SIZE == 0)
assert(settings.LEVEL_WIDTH/2 >= settings.BLOCK_SIZE)
assert(settings.LEVEL_HEIGHT/2 >= settings.BLOCK_SIZE)
assert(settings.LEVEL_WIDTH == settings.LEVEL_HEIGHT)


def generateLevelMap():
	"""Return een gegenereerd level.
	"""

	# Maak een leeg level aan.	
	levelMap = [[0 for k in xrange(settings.LEVEL_WIDTH)] for l in xrange(settings.LEVEL_HEIGHT)]
	
	# Loop door alle tiles heen.
	for y in xrange(len(levelMap)):
		for x in xrange(len(levelMap[0])):
			
			# Rand eromheen.
			if x == 0 or x == settings.LEVEL_WIDTH-1 or y == 0 or y == settings.LEVEL_HEIGHT-1:
				levelMap[y][x] = 1
			
			# Random blokjes.
			if random.random() > 0.9:
				levelMap[y][x] = 1
	
	# Plek vrijmaken voor de player.
	levelMap[-2][1] = 0
	
	# Return het level.
	return levelMap



