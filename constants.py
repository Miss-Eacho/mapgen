# Side length of generated map.
# Must be a power of two.
MAP_SIZE = 256

# Fraction of map above sea level.
LAND_PROPORTION = 0.6
# Initial size of wibbliness
# Higher values produce maps with greater altitude variation.
# Low values produce flattish maps.
LAND_WIBBLE_BASE = 40
# Rate of wibbliness decay.
# Higher values produce large continents, smooth angular coastlines.
# Lower values produce scattered islands, rough irregular coastlines.
LAND_WIBBLE_SCALE = 1.5

# Force minimum and maximum elevation of map edges.
EDGE_MIN = 0
EDGE_MAX = 30
# Force sea level upwards to cover edges?
# Can reduce land proportion if EDGE_MAX is too high.
FORCE_SEA_EDGES = True

# Fraction of sea counted as deep water.
DEEP_WATER_PROPORTION = 0.3

# Semi-arbitrary constant. Ignore.
SCATTER_WIBBLE_BASE = 20

# Minimum height of snowy areas above sea level
SNOW_MIN_HEIGHT = 24
# Fraction of land above SNOW_MIN_HEIGHT covered by snow.
SNOW_PROPORTION = 0.9
# Clumpiness of snow.
SNOW_WIBBLE_SCALE = 0.8

# Fraction of [terrain type] covered by rocks.
ROCK_PROPORTION_GRASS = 0.08
ROCK_PROPORTION_SNOW  = 0.16
ROCK_PROPORTION_WATER = 0.06
# Clumpiness of rocks.
ROCK_WIBBLE_SCALE = 0.88

# Fraction of waterline areas covered by sand beaches.
SAND_PROPORTION = 0.8
# Clumpiness of beach areas.
SAND_WIBBLE_SCALE = 0.88

# Fraction of [terrain type] covered by trees.
TREE_PROPORTION_GRASS = 0.2
TREE_PROPORTION_SNOW  = 0.1
# Clumpiness of trees.
TREE_WIBBLE_SCALE = 0.8

# Maximum depth of bogs below sea level.
BOG_MAX_DEPTH = 1
# Maximum height of bogs above sea level.
BOG_MAX_HEIGHT = 3
# Fraction of land between above limits covered by bog.
BOG_PROPORTION = 0.15
# Clumpiness of boggy areas.
BOG_WIBBLE_SCALE = 1.8

# Number of streams to generate.
# This feature is mostly broken.
NUM_STREAMS = 100