import os
import dns
import dns.resolver

# open a file
inputFile = open("hostnames.txt", "r")

# read the file
fileContent = inputFile.read()

# Parse hostnames
hostnames = fileContent.split()

# Go through the hostnames
for hostname in hostnames:
    # Try - MX record might not exist
    try:
        # Get MX Record
        result = dns.resolver.resolve(hostname, 'MX')

        # Find MX Record with the highest priority
        lowestPriority = 1000
        mxHostname = ''
        for ipval in result:
            record = ipval.to_text()
            recordField = record.split()
            #print(recordField[0])
            if(int(recordField[0]) < lowestPriority):
                mxHostname = recordField[1][:-1]
        print(hostname+" "+mxHostname)
    except:
        print('No MX record found')