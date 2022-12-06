chosen_year = input("Enter the year of interest: ")
Min_life = 99999
Max_life = -1
Country_max = ""
Country_min = ""
Max_year = ""
Min_year = ""

sum = 0 
count = 0

year_chosen_max_life = -1
year_chosen_min_life = 99999
chosen_year_country_min = ""
chosen_year_country_max = ""
chosen_year_year_max = ""
chosen_year_year_min = ""

with open("life.txt") as NEW_FOLDER:
    next(NEW_FOLDER)
    for line in NEW_FOLDER:
        parts = line.split(",")
        Entity = parts[0].strip()
        Code = parts[1].strip()
        Year = parts[2]
        Life = float(parts[3])

        if Life > Max_life:
            Max_life = Life
            Country_max = Entity
            Max_year = Year

        if Life < Min_life:
            Min_life = Life
            Country_min = Entity
            Min_year = Year

        if Year == chosen_year:
            count += 1
            sum += Life

            if Life > year_chosen_max_life:
                year_chosen_max_life = Life
                chosen_year_country_max = Entity
                chosen_year_year_max = Year

            if Life < year_chosen_min_life:
                year_chosen_min_life = Life
                chosen_year_country_min = Entity
                chosen_year_year_min = Year

Average = sum/count

print(f"The overall max life expectancy is: {Max_life} from {Country_max} in {Max_year} ")
print(f"The overall min life expectancy is: {Min_life} from {Country_min} in {Min_year}")
print(f"For the year {chosen_year}:")
print(f"The average life expectancy across all countries was {Average:.2f}")
print(f"The max life expectancy was in {chosen_year_country_max} with {year_chosen_max_life:.2f}")
print(f"The min life expectancy was in {chosen_year_country_min} with {year_chosen_min_life:.2f}")