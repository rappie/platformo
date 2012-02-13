################################################################################
#
#  S E T T I N G S
# 
################################################################################
#
# Dit bestand bevat alle settings gerelateerde variabelen zoals bijvoorbeeld de
# grootte van de tiles of de grootte van blocks in het level cluster.
#
################################################################################


# Loop snelheid.
PLAYER_WALK_SPEED = 0.1

# Spring hoogte.
PLAYER_JUMP_SPEED = -5

# Spring cutoff.
#
# Als je in een sprong de knop loslaat vertraag je naar deze snelheid.
#
PLAYER_JUMP_CUTOFF_SPEED = -2.5

# De sterkte van de zwaartekracht.
#
# Hoe hoger hoe sneller je naar beneden accelereert en hoe lager je kan springen.
#
GRAVITY = 0.1

# Max speeds.
PLAYER_MAX_SPEED_HORIZONTAL = 4
PLAYER_MAX_SPEED_VERTICAL = 8


# Grootte van het level.
#
#LEVEL_WIDTH = 2048
#LEVEL_HEIGHT = 2048
#LEVEL_WIDTH = 1024
#LEVEL_HEIGHT = 1024
LEVEL_WIDTH = 512
LEVEL_HEIGHT = 512
#LEVEL_WIDTH = 16
#LEVEL_HEIGHT = 16


# Max FPS.
#
# Dit bepaalt hoeveel FPS je hebt maar ook hoe snel het level update enzo. Als
# je deze dus lager maakt moet je alle andere speeds hoger maken.
#
MAX_FPS = 100


# Speed van de player animations.
#
# Deze variabele bepaalt hoeveel miliseconden een player animation frame duurt.
#
PLAYER_ANIMATION_SPEED = 200


# Grootte van de tiles in een level.
TILE_WIDTH = 32
TILE_HEIGHT = 32

# Grootte van de player.
PLAYER_WIDTH = 26
PLAYER_HEIGHT = 26

# Grootte van cluster blocks.
#
# Dit bepaalt de grootte van de nodes in de 'onderste laag' in de cluster tree.
#
BLOCK_SIZE = 8




