#!/usr/bin/env python
"""
Parses through mediawiki writeup of plants and returns a dictionary. 
Format for each plant is:
Common_name: {Scientific_name:string, helps:[list], helped_by:[list], 
attracts:[list], repels:[list], avoid:[list], comment:string}
Due to the non-uniformed format, the returned data will have to 
skimmed through and edited a little bit. 
"""

def skip_header(filename):
    '''
    Returns a string with the formatting top and bottom removed from mediawiki format.
    This makes it easy to parse the main data.
    '''
    f = open(filename)
    original_data = f.read()
    f.close()
    
    i = 0
    for char in original_data:
        if char == "[":
	    start_position = i
	    break
	i += 1 
    return original_data[start_position-4:]

def parse_data(filename, plant_type):
    mediawiki_format = skip_header(filename)
    
    # Creates a string called split_plants of all information for each plant.
    removed_brackets = mediawiki_format.replace("[[", "")
    removed_brackets = removed_brackets.replace("]]", "")
    split_plants = removed_brackets.split('|-')
    
    # Strips each string to create a new list called clean_plants
    clean_plants = []
    for string in split_plants:
        if "style=" in string:
	    string = string.replace('style="background:#ffffff"', '')
	string = remove_tags(string, '<', '>')
	string = remove_tags(string, '{{', '}}')
	new_string = string.strip()
	if new_string[0] == "|":
	   clean_plants.append(new_string)
    
    # Creates a dictionary of all the plants.
    # Key is the plant name.
    # Common_name: {plant_type:string, scientific_name:string, 
    # 			helps:[list], helped_by:[list], 
    # 			attracts:[list], repels:[list], 
    #			avoid:[list], comment:string}
    plant_dict = {}
    for plant in clean_plants:
        info_list = plant.split("||")
	common_name = info_list[0][1:].replace("'", "").strip()
	scientific_name = info_list[1].replace("'", "").strip()
        helps = info_list[2].strip().split(",")
	helped_by = info_list[3].strip().split(",")
	attracts = info_list[4].strip().split(",")
	repels = info_list[5].strip().split(",")
	avoid = info_list[6].strip().split(",")
	comment = info_list[7].strip()
	plant_dict[common_name] = {
				"plant_type":		plant_type,
				"scientific_name":	scientific_name, 
				"helps":		helps,
				"helped_by":		helped_by, 
				"attracts":		attracts, 
				"repels": 		repels, 
				"avoid":		avoid, 
				"comment":		comment
				}
    for key in plant_dict:
        print "'%s' :" %key
	print "{ \t 'plant_type': '%s'," %plant_dict[key]["plant_type"]
	print "\t 'scientific_name': '%s'," %plant_dict[key]["scientific_name"]
	print "\t 'helps': %s," %plant_dict[key]["helps"]
	print "\t 'helped_by': %s," %plant_dict[key]["helped_by"]
	print "\t 'attracts': %s," %plant_dict[key]["attracts"]
	print "\t 'repels': %s," %plant_dict[key]["repels"]
	print "\t 'avoid': %s," %plant_dict[key]["avoid"]
	print "\t 'comment': '%s'" %plant_dict[key]["comment"]
	print "},"
	
    return plant_dict
				

def remove_tags(string, start_char, end_char):
    '''
    Removes tags and their entire contents within a given string.
    '''
    while "<" in string:
        start = string.find(start_char)
	end = string.find(end_char)
        new_string = string[:start] + string[end+1:]
	string = new_string
    return string

def main():
    parse_data('veggies.txt', "veggie")
    parse_data('flowers.txt', "flower")
    parse_data('herbs.txt', "herbs")

if __name__ == '__main__':
    main()
