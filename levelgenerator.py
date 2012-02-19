import random

import settings


# Variabelen voor objecten in de level map.
BRICK = 1
COIN = 2
MONSTER = 3
EXIT = 4

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
	levelMap = [[[] for k in xrange(settings.LEVEL_WIDTH)] for l in xrange(settings.LEVEL_HEIGHT)]
	
	# Loop door alle tiles heen.
	for y in xrange(len(levelMap)):
		for x in xrange(len(levelMap[0])):
			
			# Haal de tile op.
			tile = levelMap[y][x]
			
			# Random blokjes.
			if random.random() > 0.90:
				tile.append(BRICK)

			# Random coins.
			if tile == []:
				if random.random() > 0.95:
					tile.append(COIN)

			# Random coins.
			if random.random() > 0.99:
				tile.append(MONSTER)

			# Rand eromheen.
			if x == 0 or x == settings.LEVEL_WIDTH-1 or y == 0 or y == settings.LEVEL_HEIGHT-1:
				levelMap[y][x] = [BRICK]
	
	# Plek vrijmaken voor de player.
	levelMap[-2][1] = []

	# Exit plaatsen
	levelMap[1][-2] = [EXIT]
	
	# Return het level.
	return levelMap



