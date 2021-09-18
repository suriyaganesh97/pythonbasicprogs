sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
new_sentence = sentence.split()
result = {word:len(word) for word in new_sentence}


print(result)