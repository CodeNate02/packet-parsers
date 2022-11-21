from scapy.all import *

NODEIP = '192.168.100.1'
packets = rdpcap('Node1.pcap')
ntwo = []
nfour = []






# FILTER
def filter( node, nodeIP ):
    for iter in packets:
        if(iter.haslayer('ICMP') == False): 
            continue #Filter out packets without ICMP
        elif((iter[ICMP].type != 8) and (iter[ICMP].type != 0)): 
            continue #Filter out packets that aren't requests/replies
        elif(iter[IP].src == nodeIP or iter[IP].dst == nodeIP):
            node.append(iter)

# CALCULATE METRICS
def calc( node, nodename ):
    scount = 0 #Count Echo Requests Sent
    bcount = 0 #Count Echo Request Bytes Sent
    #These two can be used to calculate the request data as well
    rtt = 0
    
    sentReqs = [] #Record of all request sent
    
    for iter in node:
        if((iter[ICMP].type == 8) and (iter[IP].src == NODEIP)) : #For REQUESTS SENT FROM NODE 1
            scount += 1  #Total number of requests sent += 1
            bcount += (iter[Ether].len ) #Sum of len sent
            sentReqs.append(iter)
        elif( (iter[ICMP].type == 0) and (iter[IP].dst == NODEIP) ):
            for x in sentReqs:
                if(x.seq != iter.seq): #Skip if the iter doesn't match
                    continue
                rtt += (iter.time - x.time)*1000 #add this ping's RTT
                sentReqs.remove(x) #Remove the ping that has already been matched
                break
    print("Number of Echo Requests sent by Node 1 to "+nodename+" = "+str(scount))
    print("Echo request bytes sent to "+nodename+" = "+str(bcount+(14*scount))) #Bytes = len sum + ethernet header
    print("Echo request data sent to "+nodename+" = "+ str(bcount - ((8+20) * scount)) ) #Data = len sum - IP and ICMP headers
    print("Average Echo Request RTT to "+nodename+" = "+str(round( (rtt / scount) ,3 ))+" msec")

filter( ntwo, '192.168.100.2')
filter( nfour, '192.168.200.2')
calc( ntwo, "Node 2")
calc( nfour, "Node 4")
