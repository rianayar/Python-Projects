# A6 for Week 9
# COP 1030 - 48320
# Ria Nayar - 1091791

print("My name is Ria Nayar, so the last letter of my last name is R.\n\n")

# I chose the Hawaii Rainbow Warriors football team
# They got their name in 1923, when a rainbow appeared over Moiliili Field after they beat Oregon State, 7-0
# Their uniform and helmets are really cool :)

teamRoster = ["Dae Dae Hunter", "Penei Pavihi", "Matthew Shipley", "Jeremiah Pritchard", "Khoury Bethley", "Zion Bowens", "Calvin Turner", "Eugene Ford", "Jonah Panoke", "Mark Blocker II", "Sterlin Ortiz", "Justin Uahinui", "Chevan Cordeiro", "Jake Farrell", "Jalen Perdue", "James Phillips", "Armani Edden", "Logan Taylor", "Isaiah Tufaga", "Boone Abbott", "Cortez Davis", "Kamali'i Akina", "Quentin Frazier", "Cameron Lockridge", "Michael Washington", "Jared Smart", "Kai Kaneshiro", "Travon Killins", "Leonard Lee", "Koali Nishigaya", "Aaron Cephus", "Nalu Emerson", "Donovan Dalton", "Tiger Peterson", "Steven Fiso", "James Green III", "Hekili Keliiliki", "Kenneth Fitzgerald", "Alaka'i Mashima", "Kalamaku Kuewa", "Jonah Kahahawai-Welch", "Wyatt Tucker", "Payton Awaya", "Noa Kamana", "Derek Thomas", "Asher Pilanca", "Justus Tavai", "Ezra Evaimalo", "Solo Vaipulu", "Darius Muasau", "Kalani Kamakawiwo'ole", "Blessman Ta'ala", "Samson Siilata", "Kila Kamakawiwo'ole", "Andrew Choi", "Eliki Tanuvasa", "Kauka Umiamaka", "Sergio Muasau", "Ra Elkington", "Ben Falck", "Arasi Mose", "Micah Vanterpool", "Kohl Levao", "Gene Pryor", "Ilm Manning", "Michael Eletise", "Micah Soliai Howlett", "Grey Ihu", "Dayton Toney", "Nick Mardner", "Riley Wilson", "Dior Scott", "Tamatoa Mokiao-Atimalala", "Kilohana Haasenritter", "John Tuitupou", "Gabriel Iniguez Jr.", "Djuan Matthews", "Mason Mataafa", "Alema Kapoi", "Kemon Smith", "Adam Stack", "Maurice Ta'ala", "Zach Ritner", "Foi Shaw", "Jonah Laulu", "Colby Burton", "Zacchaeus McKinney", "Solomon Turner", "Kolby Wyatt"]

roster = teamRoster

# Print the list
for i in range(len(roster)) :
  print(roster[i], " - ", end='')
print("\n\n")

# Append Zooptopia
roster.append("Zootopia")
for i in range(len(roster)) :
    print(roster[i], " - ", end='')
print("\n\n")

# Reverse alphabetical order
reverseRoster = sorted(roster, reverse = True)
for i in range(len(reverseRoster)) :
  print(reverseRoster[i], " - ", end='')
print("\n\n")

# Remove the 2nd position player
reverseRoster.pop(1)
for i in range(len(reverseRoster)) :
  print(reverseRoster[i], " - ", end='')
