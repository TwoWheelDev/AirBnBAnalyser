from csv import DictReader
import glob
import operator
from airbnb.functions import *

# Read in our CSV files
files = glob.glob('./csv/*.csv')

if len(files) != 2:
    print('Please ensure there are only two files in the CSV folder')
    exit(2)

with open(files[0], newline='') as f:
    file1_rows = list(DictReader(f))
f.close()

with open(files[1], newline='') as f:
    file2_rows = list(DictReader(f))
f.close()

# How many listings are in each file
file1_listings = len(file1_rows)
file2_listings = len(file2_rows)

# Filter the listings to only include Entire Home/Apt
filtered_listings1 = filter(filterhomeapt, file1_rows)
filtered_listings2 = filter(filterhomeapt, file2_rows)

# Create a count of the number of listings that each host_id has
f1_hosts = count_listings_by_host(filtered_listings1)
f2_hosts = count_listings_by_host(filtered_listings2)

# We are only interested in those with multiple listings
file1_hosts = hosts_with_multiple(f1_hosts)
file2_hosts = hosts_with_multiple(f2_hosts)

# Sort the hosts, by reverse order of number of listings
sorted1 = sorted(file1_hosts.items(), key=operator.itemgetter(1), reverse=True)
sorted2 = sorted(file2_hosts.items(), key=operator.itemgetter(1), reverse=True)

# Calculate the change in the number of listings between the two files
change = ((file2_listings - file1_listings) / file1_listings) * 100
print('%.2f%% change' % change)
