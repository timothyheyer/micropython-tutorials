import speech
from microbit import sleep

# The say method attempts to convert English into phonemes.
speech.say("I can sing!")
sleep(1000)
speech.say("Listen to me!")
sleep(1000)

# Clearing the throat requires the use of phonemes. Changing
# the pitch and speed also helps create the right effect.
speech.pronounce("AEAE/HAEMM", pitch=200, speed=100)  # Ahem
sleep(1000)

# Singing requires a phoneme with an annotated pitch for each syllable.
solfa = [
    "#58DOWWWWWW",   # Doh
    "#62REYYYYYY",   # Re
    "#70MIYYYYYY",    # Mi
    "#78FAOAOAOAOR",  # Fa
    "#88SOHWWWWW",    # Soh
    "#94LAOAOAOAOR",  # La
    "#103TIYYYYYY",    # Ti
    "#115DOWWWWWW",    # Doh
]

# Sing the scale descending in pitch.
song = ''.join(solfa)
speech.sing(song, speed=100)
# Reverse the list of syllables.
solfa.reverse()
song = ''.join(solfa)
# Sing the scale ascending in pitch.
speech.sing(song, speed=100)