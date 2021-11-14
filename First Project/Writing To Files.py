File_Content = "1: EAT\n\n2: SLEEP\n\n3: GAME\n\n4: REPEAT"

daily_routine = open("My Daily Routine.txt", "w")

daily_routine.write(File_Content)

daily_routine.close()

print("Written:" + File_Content + "to file")