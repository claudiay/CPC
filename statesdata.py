import model
from model import Location

def upload_locations(file):
    f = open(file)
    for line in f:
        l = line.strip().replace(' " ', "").replace(' "', "").replace('"', "").split(",")
    	print l
	location = Location(*l)
    	model.add(location)
    	model.save_all()

def main():
    upload_locations("plantdata/zips.csv")

if __name__ == '__main__':
    main()
