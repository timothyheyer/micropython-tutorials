# DALEK poetry generator, by The Doctor (and Timothy Heyer)
import speech
import random
from microbit import sleep

# Randomly select fragments to interpolate into the template.
location = random.choice(["Colorado", "Orlando", "chicago", "san diego"])
action = random.choice(["hiked with", "surfed with", "sang to", "read to"])
obj = random.choice(["head", "hand", "dog", "foot"])
prop = random.choice(["with a bow", "under his toe", "with some dough",
                     "that was slow"])
result = random.choice(["it ran off", "it glowed", "it blew up",
                       "it turned blue"])
attitude = random.choice(["in the street", "like a fleet", "for a seat",
                         "with some meat"])
conclusion = random.choice(["were it so", "it's a no", "why they know",
                           "for a throw"])

# A template of the poem. The {} are replaced by the named fragments.
poem = [
    "there was a young man from {}".format(location),
    "who {} his {} {}".format(action, obj, prop),
    "one night he would see",
    "{} {}".format(result, attitude),
    "and he never worked out {}".format(conclusion),
    "EXTERMINATE",
]

# Loop over each line in the poem and use the speech module to recite it.
for line in poem:
    speech.say(line, speed=120, pitch=100, throat=100, mouth=200)
    sleep(500)