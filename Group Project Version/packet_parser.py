import re
node1, node2, node3, node4 = [[],[],[],[]]

def parse() :
    global node1, node2, node3, node4
    node1 = parseFile('nodes/Node1_Filtered.txt')
    node2 = parseFile('nodes/Node2_Filtered.txt')
    node3 = parseFile('nodes/Node3_Filtered.txt')
    node4 = parseFile('nodes/Node4_Filtered.txt')
    return[ node1, node2, node3, node4 ]

def parseFile(filename) :
    packetdata = []
    f = open(filename, 'r')
    line = f.readline()
    while (line):
        #Capture each packet block
        if (line.startswith('No.')): #first part of the packet
            line = f.readline().split()
            time = line[1] #Packet does not contain time
            f.readline() #Read the empty line
            line= f.readline() #read the first line of the packet
            packet = ""
            while(line != '\n'): #Packet ends when there is an empty line
                packet+= line.strip().split("  ")[1]+" " #Add the packet to a string
                line = f.readline() #Next line
            packet = (packet.strip().split(' ')) #Convert string into an array of each set of 2 bytes
            source = (str(int(packet[26],16))+'.'+str(int(packet[27],16))+'.'+str(int(packet[28],16))+'.'+str(int(packet[29],16)))
            size = len(packet)
            sequence = str(int(packet[40]+packet[41],16))
            if( int(packet[34], 16) == 8 ):
                type = "Request"
            elif( int(packet[34], 16) == 0 ):
                type = "Reply"
            ttl = int(packet[22], 16)
            packetdata.append( [float(time), source, float(size), type, float(sequence), float(ttl)] )
        else:
            line = f.readline()
    return packetdata

    #Original Code pre-extra-credit
    # with open(filename , 'r') as f:
    #     datafile = f.readlines()

    # ## Parsed Packet Data
    # time = ""
    # source = ""
    # destination = ""
    # sequenceNum = ""
    # ttlNum = ""
    # packetData = []

    # ## Data Size Metrics
    # for line in datafile:
    #     if (line != '\n') :
    #         print(line.strip())
        
    #     packet = []
        
    #     match = re.search('\d+\.\d+', line)
    #     if match: 
    #         time = match.group()
    #         time = float(time)
    #         packet.append(time)

    #     match = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
    #     if match:
    #         source = match.group(1)
    #         destination = match.group(2)
    #         packet.append(source)
    #         #packet.append(destination)

    #     match = re.search('ICMP\s+\d+', line)
    #     if match:
    #         length = match.group()
    #         length = length.split()
    #         length = int(length[1])
    #         packet.append(length)

    #     if 'Echo (ping) request' in line:
    #         packet.append('Request')
        

    #     if 'Echo (ping) reply' in line:
    #         packet.append('Reply')

        
    #     match = re.search('seq=(.+?)/', line)
    #     if match:
    #         sequenceNum = match.group(1)
    #         sequenceNum = int(sequenceNum)
    #         packet.append(sequenceNum)
        
    #     ## NEED TO FIX TO GRAB TTL
    #     match = re.search('ttl=(\d+)', line)
    #     if match:
    #         ttlNum = match.group(1)
    #         ttlNum = int(ttlNum)
    #         packet.append(ttlNum)
    #         #break
        
    #     if len(packet) > 1 :
    #         packetData.append(packet)
    
    # f.close()
    # return packetData

parseFile('nodes/Node1_Filtered.txt')


