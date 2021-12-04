"""Nelson Booth
Assignment 7.1: Rental Price Analysis
Description: This program will take in a rental prices in the housing market
as a csv file and generate a text file report.
"""
# global variables/importations
OUTPUT_FILE = 'report.txt' # stores the output file name as 'report.txt'
import collections # importing the collections module
global nested_dictionary # initializes the 1st nested dictionary
nested_dictionary = {}
global nested_dictionaryv2 # initializes the 2nd nested dictionary
nested_dictionaryv2 = {}
global nested_dictionaryv3 # initializes the 3rd nested dictionary
nested_dictionaryv3 = {}
global addresses # initializes the list of addresses
addresses = []
global neighborhoods # initializes the list of neighborhoods
neighborhoods = []
# loads the 2nd list containing the neighborhood names in the csv file
def load_listv2(FILENAME): # takes in the filename as an argument
    with open(FILENAME, 'r') as f: # opens the csv file and proceeds to read the file
        lines = f.readlines() # stores the file object to reading each line
        del lines[0] # deletes the 1st line(header)
        for each_line in lines: # iterates through each address, neighborhood, and rent price in each line
            each_line = each_line.split(',') # splits at the comma between each item
            neighborhood = each_line[1] # stores neighborhood names to the 2nd item in each line
            neighborhoods.append(neighborhood) # adds each neigborhood name to the list
    return sorted(set(neighborhoods)) # returns a sorted and set list of neighborhood names

# loads the 1st list containing the address names in the csv file
def load_list(FILENAME): # takes in the filename as an argument
    with open(FILENAME, 'r') as f: # opens the csv file and proceeds to read the file
        lines = f.readlines() # stores the file object to reading each line
        del lines[0] # deletes the 1st line(header)
        for each_line in lines: # iterates through each address, neighborhood, and rent price in each line
            each_line = each_line.split(',') # splits at the comma between each item
            address = each_line[0] # stores address names to the 1st item in each line
            addresses.append(address) # adds each neigborhood name to the list
    return addresses # returns the list of address names

# loads the 1st dictionary containing all the data from the csv file
def load_dictionary(FILENAME): # takes in filename as an argument
    with open(FILENAME, 'r') as f: # opens the csv file and proceeds to read the file
        lines = f.readlines() # stores the file object to reading each line
        del lines[0] # deletes the 1st line(header)
        for each_line in lines: # iterates through each address, neighborhood, and rent price in each line
            each_line = each_line.strip() # each item is stripped of whitespaces
            each_line = each_line.replace("$", "") # replaces the symbol '$' with space
            each_line = each_line.split(',') # splits at the comma between each item
            address_key = each_line[0] # address is assigned to the first item of each line
            neighborhood_value = each_line[1] # neigborhood is assigned to the second of each line
            rent20_value = each_line[2] # 2020 rent price is assigned to the third item of each line
            rent21_value = each_line[3] # 2021 rent price is assigned to the fourth item of each line
            nested_dictionary.update({address_key:{'neighborhood': neighborhood_value, '2020 rent': rent20_value, '2021 rent': rent21_value}}) # updates the empty dictionary with above keys and values
    return nested_dictionary # returns the nested dictionary

# loads the 2nd dictionary containing all the data from the csv file
def load_dictionaryv2(FILENAME): # takes in filename as an argument
    with open(FILENAME, 'r') as f: # opens the csv file and proceeds to read the file
        lines = f.readlines() # stores the file object to reading each line
        del lines[0] # deletes the 1st line(header)
        nei_list = [] # initializes an empty list for neighborhood and 2021 rent prices
        re_list = []
        for each_line in lines: # iterates through each address, neighborhood, and rent price in each line
            each_line = each_line.strip() # each item is stripped of whitespaces
            each_line = each_line.replace("$", "") # replaces the symbol '$' with space
            each_line = each_line.split(',') # splits at the comma between each item
            neighborhood_name = each_line[1] # neigborhood is assigned to the second of each line
            rent21 = each_line[3] # 2021 rent price is assigned to the fourth item of each line
            nei_list.append(neighborhood_name) # adds each neighborhood name and 2021 rent price to respective lists
            re_list.append(rent21)
    zipped = sorted(zip(nei_list, re_list)) # stores the zipped and sorted list of tuples 
    in_dict = collections.defaultdict(list) # calls the defaultdict() method from collections module
    for a, b in zipped: # iterates through each neighborhood and 2021 rent price
        in_dict[a].append(b) # appends each 2021 rent price associated with their respective neighborhood
    in_dict = dict(in_dict) # casts the variable as a dictionary
    nested_dictionaryv2.update(in_dict) # 2nd empty nested dictionary is updated
    return nested_dictionaryv2 # returns the 2nd nested dictionary
"""Acknowledgement: stackoverflow.com, geeksforgeeks.org
Links: https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int,
https://www.geeksforgeeks.org/python-convert-list-of-tuples-to-dictionary-value-lists/
"""

# loads the 3rd dictionary containing all the data from the csv file
def load_dictionaryv3(FILENAME): # takes in filename as an argument
    with open(FILENAME, 'r') as f: # opens the csv file and proceeds to read the file
        lines = f.readlines() # stores the file object to reading each line
        del lines[0] # deletes the 1st line(header)
        nei_list = [] # initializes an empty list for neighborhood and 2020 rent prices
        re_list = []
        for each_line in lines: # iterates through each address, neighborhood, and rent price in each line
            each_line = each_line.strip() # each item is stripped of whitespaces
            each_line = each_line.replace("$", "") # replaces the symbol '$' with space
            each_line = each_line.split(',') # splits at the comma between each item
            neighborhood_name = each_line[1] # neigborhood is assigned to the second of each line
            rent20 = each_line[2] # 2020 rent price is assigned to the third item of each line
            nei_list.append(neighborhood_name) # adds each neighborhood name and 2020 rent price to respective lists
            re_list.append(rent20)
        zipped = sorted(zip(nei_list, re_list)) # stores the zipped and sorted list of tuples 
        in_dict = collections.defaultdict(list) # calls the defaultdict() method from collections module
        for a, b in zipped: # iterates through each neighborhood and 2020 rent price
            in_dict[a].append(b) # appends each 2020 rent price associated with their respective neighborhood
        in_dict = dict(in_dict) # casts the variable as a dictionary
        nested_dictionaryv3.update(in_dict) # 3rd empty nested dictionary is updated
        return nested_dictionaryv3 # returns the 3rd nested dictionary

# calculates the average rent price among the 2021 rent prices
def rent_average(nested_dictionary, addresses): # takes the 1st nested dictionary and the list of addresses as arguments
    ad_list = [] # initializes the list
    for each_address in addresses: # iterates through each address in the address list
        address_list = nested_dictionary[each_address]['2021 rent'] # gets and stores the value of each address' 2021 rent price
        address_list = int(address_list) # casts the 2021 rent price as an integer
        ad_list.append(address_list) # appends the price to the initial list
    avr = sum(ad_list) / len(ad_list) # stores the average by taking the sum of the prices list and the length of the prices list
    avr = f"${avr:.2f}" # formatted string that converts the average into proper dollar format
    return avr # returns the average

# calculates the highest rent price among 2021 rent prices
def rent_highest(nested_dictionary, addresses): # takes the 1st nested dictionary and the list of addresses as arguments
    hi_list = [] # initializes the list
    for each_address in addresses: # iterates through each address in the address list
        highest_list = nested_dictionary[each_address]['2021 rent'] # gets and stores the value of each address' 2021 rent price
        highest_list = int(highest_list) # casts the 2021 rent price as an integer
        hi_list.append(highest_list) # appends the price to the initial list
    high = max(hi_list) # using max, finds the highest number within the list
    index = hi_list.index(high) # stores the position of the highest number using .index()
    index_2 = addresses[index] # finds and stores the address in the address list with the same position
    hi_list = f"${high:.2f}, {index_2}" # formatted string converts the highest number to dollar format and displays the corresponding address
    return hi_list # returns the highest 2021 rent price

# calculates the lowest rent price among 2021 rent prices
def rent_lowest(nested_dictionary, addresses): # takes the 1st nested dictionary and the list of addresses as arguments
    lo_list = [] # initializes the list
    for each_address in addresses: # iterates through each address in the address list
        lowest_list = nested_dictionary[each_address]['2021 rent'] # gets and stores the value of each address' 2021 rent price
        lowest_list = int(lowest_list) # casts the 2021 rent price as an integer
        lo_list.append(lowest_list) # appends the price to the initial list
    low = min(lo_list) # using min, finds the lowest number within the list
    index = lo_list.index(low) # stores the position of the lowest number using .index()
    index_2 = addresses[index] # finds and stores the address in the address list with the same position
    lo_list = f"${low:.2f}, {index_2}" # formatted string converts the lowest number to dollar format and displays the corresponding address
    return lo_list # returns the lowest 2021 rent price

# calculates the average rent price change among 2021 and 2020 rent prices
def rent_average_change(nested_dictionary, addresses): # takes the 1st nested dictionary and the list of addresses as arguments
    dif_list = [] # initializes the list
    for each_address in addresses: # iterates through each address in the address list
        y = nested_dictionary[each_address]['2021 rent'] # gets and stores the 2021 rent price corresponding to the address
        x = nested_dictionary[each_address]['2020 rent'] # gets and stores the 2020 rent price corresponding to the address
        y = int(y) # casts the prices as integers respectively
        x = int(x)
        difference = y - x # finds and stores the difference between 2020 rent prices from 2021 rent prices
        dif_list.append(difference) # appends the difference to the list
    avr = sum(dif_list) / len(dif_list) # calculates the average by finding the sum of the list divided by the length of the list
    if avr >= 0: # if average is larger than zero
        avr = f"+${avr:.2f}" # formatted string with average in dollar format with a positive sign
        return avr # returns average
    else: # if average is not positive
        avr = f"-${avr:.2f}" # formatted string with average in dollar format witn a negative sign
        return avr # returns average

# calculates the highest average rent price change among 2021 and 2020  rent prices
def highest_rent_average_change(nested_dictionary, addresses): # takes the 1st nested dictionary and the list of addresses as arguments
    dif_list = [] # initializes the list
    for each_address in addresses: # iterates through each address in the address list
        y = nested_dictionary[each_address]['2021 rent'] # gets and stores the 2021 rent price corresponding to the address
        x = nested_dictionary[each_address]['2020 rent'] # gets and stores the 2020 rent price corresponding to the address
        y = int(y) # casts the prices as integers respectively
        x = int(x)
        difference = y - x # finds and stores the difference between 2020 rent prices from 2021 rent prices
        dif_list.append(difference) # appends the difference to the list
    highest = max(dif_list) # gets and stores the highest average rent price change
    index = dif_list.index(highest) # finds the position of the number using .index()
    index_2 = addresses[index] # matches the address with the same position
    if highest >= 0: # if the rent price change is larger than zero
        highest = f"+${highest:.2f}, {index_2}" # formatted string that converts the price to dollar format with a positive sign and displays the corresponding address
        return highest # returns the highest rent price change
    else: # if the rent price change is less than zero
        highest = f"-${highest:.2f}, {index_2}" # formatted string that converts the price to dollar format with a negative sign and displays the corresponding address
        return highest # returns the highest rent price change

# calculates the lowest average rent price change among 2021 and 2020 rent prices
def lowest_rent_average_change(nested_dictionary, addresses): # takes the 1st nested dictionary and the list of addresses as arguments
    dif_list = [] # initializes the list
    for each_address in addresses: # iterates through each address in the address list
        y = nested_dictionary[each_address]['2021 rent'] # gets and stores the 2021 rent price corresponding to the address
        x = nested_dictionary[each_address]['2020 rent'] # gets and stores the 2020 rent price corresponding to the address
        y = int(y) # casts the prices as integers respectively
        x = int(x)
        difference = y - x # finds and stores the difference between 2020 rent prices from 2021 rent prices
        dif_list.append(difference) # appends the difference to the list
    lowest = min(dif_list) # gets and stores the lowest average rent price change
    index = dif_list.index(lowest) # finds the position of the number using .index()
    index_2 = addresses[index] # matches the address with the same position
    if lowest >= 0: # if the rent price change is larger than zero
        lowest = abs(lowest) # stores the absolute value of the number
        lowest = f"+${lowest:.2f}, {index_2}" # formatted string that converts the price to dollar format with a positive sign and displays the corresponding address
        return lowest # returns the lowest rent price change
    else: # if the rent price change is less than zero
        lowest = abs(lowest) # stores the absolute value of the number
        lowest = f"-${lowest:.2f}, {index_2}" # formatted string that converts the price to dollar format with a negative sign and displays the corresponding address
        return lowest # returns the lowest rent price change

# calculates the least afforable neighborhood among 2021 rent prices
def least_affordable_neighborhood(nested_dictionaryv2, neighborhoods): # takes the second nested dictionary and the list of neighborhoods as arguments
    least_list = [] # initializes the list
    for each_neighborhood in neighborhoods: # iterates through each neighborhood in the neighborhood list
        x = nested_dictionaryv2[each_neighborhood] # gets and stores the 2021 rent prices for specified neighborhood
        x = list(map(int, x)) # casts the rent prices as integers and into a list using map()
        avr = sum(x) / len(x) # calculates the average by finding the sum of the list divided by the length of the list
        least_list.append(avr) # appends the average to the initial list
    least_aff = max(least_list) # finds the highest average rent price within the list
    index = least_list.index(least_aff) # gets and stores the position of the number using .index()
    index_2 = neighborhoods[index] # finds the corresponding neighborhood using the same position
    least_aff = f"{index_2} (Avg. Rent: ${least_aff:.2f})" # formatted string with the average rent of the corresponding neighborhood in dollar format
    return least_aff # returns the least affordable neighborhood and its respective average rent price

# calculates the most affordable neighborhood among 2021 rent prices
def most_affordable_neighborhood(nested_dictionaryv2, neighborhoods): # takes the second nested dictionary and the list of neighborhoods as arguments
    most_list = [] # initializes the list
    for each_neighborhood in neighborhoods: # iterates through each neighborhood in the neighborhood list
        x = nested_dictionaryv2[each_neighborhood] # gets and stores the 2021 rent prices for specified neighborhood
        x = list(map(int, x)) # casts the rent prices as integers and into a list using map()
        avr = sum(x) / len(x) # calculates the average by finding the sum of the list divided by the length of the list
        most_list.append(avr) # appends the average to the initial list
    most_aff = min(most_list) # finds the lowest average rent price within the list
    index = most_list.index(most_aff) # gets and stores the position of the number using .index()
    index_2 = neighborhoods[index] # finds the corresponding neighborhood using the same position
    most_aff = f"{index_2} (Avg. Rent: ${most_aff:.2f})" # formatted string with the average rent of the corresponding neighborhood in dollar format
    return most_aff # returns the most affordable neighborhood and its respective average rent price

# calculates the rent changes per neighborhood among 2020 and 2021 rent prices
def rent_changes_neighborhood(nested_dictionaryv2, nested_dictionaryv3, neighborhoods): # takes the second nested dictionary, the third nested dictionary, and the list of neighborhoods as arguments
    divide_list = [] # initializes the list
    for each_neighborhood in neighborhoods: # iterates through each neighborhood in the neighborhood list
        y = nested_dictionaryv2[each_neighborhood] # gets and stores the 2021 rent prices for specified neighborhood
        x = nested_dictionaryv3[each_neighborhood] # gets and stores the 2020 rent prices for specified neighborhood
        z = nested_dictionaryv3[each_neighborhood] # gets and stores the list of 2020 rent prices for specified neighborhood
        z = list(map(int, z)) # casts the rent prices as integers and into a list using map()
        y = list(map(int, y))
        x = list(map(int, x))
        y = sum(y) # finds and stores the sum of 2021 and 2020 rent prices respectively
        x = sum(x)
        difference = y - x # calculates and stores the difference of 2020 from 2021 rent prices
        divide = difference / len(z) # finds and stores the quotient of the difference divided by the length of the 2020 rent prices list
        divide_list.append(divide) # appends the quotient to the list
    string = " " # initial string
    zipped = sorted(set(zip(neighborhoods, divide_list))) # using zip(), sorts and sets the zipped list of tuples of neighborhoods and quotients
    for each_zipped in zipped: # iterates each tuple in the list
        if each_zipped[1] >= 0: # if the quotient is greater than zero
            string2 = f"\n\t{each_zipped[0]} (+${each_zipped[1]:.2f})" # formatted string with the quotient converted into dollar format with a positive sign along with its corresponding neighborhood
            string = string + string2 # using string concatenation, adds to empty string
        else: # if the quotient is less than zero
            absolute = abs(each_zipped[1]) # calculates the absolute value of the quotient
            string2 = f"\n\t{each_zipped[0]} (-${absolute:.2f})" # formatted string with the quotient converted into dollar format with a negative sign along with its corresponding neighborhood
            string = string + string2 # using string concatenation, adds to empty string
    return string # returns the rent changes per neighborhood

# main function to call helper functions
def main():
    # calls helper functions to load global dictionaries and lists from csv file
    # MUST INPUT THE CSV FILENAME INTO THESE FUNCTIONS BEFORE WRITING NEW OUTPUT FILE
    load_dictionary('rent_prices.csv')
    load_list('rent_prices.csv')
    load_listv2('rent_prices.csv')
    load_dictionaryv2('rent_prices.csv')
    load_dictionaryv3('rent_prices.csv')
    with open(OUTPUT_FILE, 'w') as f: # opens the new output file named 'report.txt' and prompts to write to it
        # calls the rest of helper functions
        f.write(f"Rent Report, 2020-2021\n")
        f.write(f"Average Rent: {rent_average(nested_dictionary, addresses)}\n")
        f.write(f"Highest Rent: {rent_highest(nested_dictionary, addresses)}\n")
        f.write(f"Lowest Rent: {rent_lowest(nested_dictionary, addresses)}\n")
        f.write(f"Average Rent Change: {rent_average_change(nested_dictionary, addresses)}\n")
        f.write(f"Highest Rent Change: {highest_rent_average_change(nested_dictionary, addresses)}\n")
        f.write(f"Lowest Rent Change: {lowest_rent_average_change(nested_dictionary, addresses)}\n")
        f.write(f"Least Affordable Neighborhood: {least_affordable_neighborhood(nested_dictionaryv2, neighborhoods)}\n")
        f.write(f"Most Affordable Neighborhood: {most_affordable_neighborhood(nested_dictionaryv2, neighborhoods)}\n")
        f.write(f"Rent Changes by Neighborhood: {rent_changes_neighborhood(nested_dictionaryv2, nested_dictionaryv3, neighborhoods)}\n")
    with open(OUTPUT_FILE, 'r+') as f: # opens the new output file named 'report.txt' and prompts to read from it
        print(f.read()) # prints and reads the new output file's contents(print is not neccessary)
# allows for main function to call helper functions
if __name__ == "__main__":
    main()