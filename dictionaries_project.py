# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def convert_damages_to_float(damage,conversion):
  updated_damages = []
  for damage in damages:
    if damage[-1] in conversion.keys():
      updated_damages.append(float(damage[:-1])*conversion[damage[-1]])
    else:
      updated_damages.append(damage)
  return updated_damages
# test function by updating damages
new_damage_list = convert_damages_to_float(damages,conversion)
#print(new_damage_list)

# 2 
# Create a Table
def compile_data():
  hurricane_data = {}
  count = 0
  for hurricane in names:
    hurricane_data[hurricane] = {"Name":names[count],"Month":months[count],"Year":years[count],"Max Sustained Wind":max_sustained_winds[count],"Areas Affected":areas_affected[count],"Damage":new_damage_list[count],"Deaths":deaths[count]}
    count += 1
  return hurricane_data
# Create and view the hurricanes dictionary
complete_data = compile_data()
#print(complete_data)

# 3
# Organizing by Year
def hurricane_by_year(hurricane_data):
  hurricane_by_year_dict = {}
  for name,data in hurricane_data.items():
    if data["Year"] not in list(hurricane_by_year_dict):
      hurricane_by_year_dict[data["Year"]] = [data]
    else:
      hurricane_by_year_dict[data["Year"]].append(data)
  return hurricane_by_year_dict
# create a new dictionary of hurricanes with year and key
hurricane_by_year_data = hurricane_by_year(complete_data)
# print(hurricane_by_year_data)

# 4
# Counting Damaged Areas
def damaged_area_count(hurricane_data):
  area_dict = {}
  for name,data in hurricane_data.items():
    for area in data["Areas Affected"]:
      if area not in list(area_dict):
        area_dict[area] = 1
      else: area_dict[area] = area_dict[area] + 1
  return area_dict
# create dictionary of areas to store the number of hurricanes involved in
area_dict = damaged_area_count(complete_data)
#print(area_dict)

# 5 
# Calculating Maximum Hurricane Count
def max_hurricane_count(area_affected_data):
  most_affected_area = ""
  highest_count = 0
  for area,count in area_affected_data.items():
    if count > highest_count:
      highest_count = count
      most_affected_area = area
  return most_affected_area,highest_count
# find most frequently affected area and the number of hurricanes involved in
hurricane_name,hurricane_count = max_hurricane_count(area_dict)
print("The most frequently affected area is " + str(hurricane_name) + " with " + str(hurricane_count) + " counts of being hit.")

# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane_count(hurricane_data):
  deadliest_hurricane = ""
  highest_count = 0
  for hurricane,data in hurricane_data.items():
    if data["Deaths"] > highest_count:
      deadliest_hurricane = hurricane
      highest_count = data["Deaths"]
  return deadliest_hurricane,highest_count
# find highest mortality hurricane and the number of deaths
worst_hurricane,highest_mortality = deadliest_hurricane_count(complete_data)
print("The deadliest hurricane is " + str(worst_hurricane) + " with " + str(highest_mortality) + " number of deaths.")

# 7
# Rating Hurricanes by Mortality
def order_by_mortality(hurricane_data):
  ordered_dict = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for key,data in hurricane_data.items():
    if data["Deaths"] == 0:
      ordered_dict[0].append(data)
    elif data["Deaths"] > 0 and data["Deaths"] <= 100:
      ordered_dict[1].append(data)
    elif data["Deaths"] > 100 and data["Deaths"] <= 500:
      ordered_dict[2].append(data)
    elif data["Deaths"] > 500 and data["Deaths"] <= 1000:
      ordered_dict[3].append(data)
    elif data["Deaths"] > 1000 and data["Deaths"] <= 10000:
      ordered_dict[4].append(data)
    elif data["Deaths"] > 10000:
      ordered_dict[5].append(data)
  return ordered_dict
# categorize hurricanes in new dictionary with mortality severity as key
hurricane_by_mortality = order_by_mortality(complete_data)
#print(hurricane_by_mortality)

# 8 Calculating Hurricane Maximum Damage
def max_damage(hurricane_data):
  max_dmg_hurricane = ""
  highest_cost = 0
  for hurricane,data in hurricane_data.items():
    if data["Damage"] == "Damages not recorded":
      continue
    elif data["Damage"] > float(highest_cost):
      max_dmg_hurricane = hurricane
      highest_cost = data["Damage"]
  return max_dmg_hurricane,highest_cost
# find highest damage inducing hurricane and its total cost
highest_dmg_hurricane,highest_cost = max_damage(complete_data)
print("The " + str(highest_dmg_hurricane) + " was the hurricane that caused the most damage financially at a value of " + str(highest_cost) + " dollars.")


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def order_by_damage(hurricane_data,scale):
  ordered_dict = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for key,data in hurricane_data.items():
    if data["Damage"] == "Damages not recorded":
      continue
    elif data["Damage"] == 0:
      ordered_dict[0].append(data)
    elif data["Damage"] > scale[0] and data["Damage"] <= scale[1]:
      ordered_dict[1].append(data)
    elif data["Damage"] > scale[1] and data["Damage"] <= scale[2]:
      ordered_dict[2].append(data)
    elif data["Damage"] > scale[2] and data["Damage"] <= scale[3]:
      ordered_dict[3].append(data)
    elif data["Damage"] > scale[3] and data["Damage"] <= scale[4]:
      ordered_dict[4].append(data)
    elif data["Damage"] > scale[4]:
      ordered_dict[5].append(data)
  return ordered_dict
# categorize hurricanes in new dictionary with damage severity as key
hurricanes_by_damage = order_by_damage(complete_data,damage_scale)
#print(hurricanes_by_damage)
