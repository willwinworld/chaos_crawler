zombies = 1001.0
warriors = 100.0
guns = 10.0 
bullets = 1000.0
knives = 100.0
warriors_use_guns = guns 
warriors_use_knives = warriors - guns 
average_bullets_per_guns = bullets / guns 
average_zombies_per_warriors_need_to_be_killed = zombies / warriors



print "There are", zombies, "zombies need to be killed."
print "There are", warriors_use_guns, "guns which is more efficient than knives."
print "There are", warriors_use_knives, "knives which is less efficient than guns."
print "Average bullets", average_bullets_per_guns, "of each guns."
print average_zombies_per_warriors_need_to_be_killed, "average zombies per warriors need to killed." 