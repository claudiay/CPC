import model
from model import States, Location

def upload_states(file):
    f = open(file)
    for line in f:
    	print line
	state = States(line)
        model.add(state)
	model.save_all()
    f.close()

def upload_locations(file):
    f = open(file)
    for line in f:
        l = line.strip().replace(' " ', "").replace(' "', "").replace('"', "").split(",")
    	print l
	location = Location(*l)
    	model.add(location)
    	model.save_all()
def main():
    # upload_states("plantdata/states.txt")
    upload_locations("plantdata/zips.csv")

if __name__ == '__main__':
    main()
