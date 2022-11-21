#Compute each of the node lists created by the parser
def compute(n1, n2, n3, n4) :
    f = open('output.csv', 'w')
    f.write('Node 1 \n')
    compute_node(n1, f , '192.168.100.1')
    f.write('\n\nNode 2 \n')
    compute_node( n2, f , '192.168.100.2' )
    f.write('\n\nNode 3 \n')
    compute_node(n3, f , '192.168.200.1')
    f.write('\n\nNode 4 \n')
    compute_node(n4, f , '192.168.200.2' )    
    
    f.close()

def output(filename, node, reqs,reqr,reps,repr,bs,br,ds,dr,rtt,th) :
    f = open(filename, 'w')
    f.write('Node 1 \n')
    
    for i in range( 1, 5 ) :
        node_num = 'Node ' + str(i)
        #print(node_num)
        format(f, node_num)

    

    f.close()


def compute_node( node, f, SEND_IP ) :
    requests = []


    #Data Size Metrics
    req_sent = 0
    req_rec = 0
    rep_sent = 0
    rep_rec = 0

    bytesSent = 0
    bytesRec = 0
    dataSent = 0
    dataRec = 0

    #Time Based Metrics
    rtt = 0
    throughput = 0 #bytesSent / rtt
    goodput = 0 # dataSent / rtt
    delay = 0
    hop = 0

    #For loop going through each individual packet in the node
    
    for i in range(0, len(node)):

        #BY PACKET
        
        time, source, length, repreq, seq, ttl = node[i]
        if ( repreq == 'Request' ):
            #REQUESTS
            if( source == SEND_IP):  #Requests SENT
                req_sent += 1
                bytesSent += length
                dataSent += (length-42)

            else:                     #Requests RECIEVED
                req_rec += 1
                bytesRec += length
                dataRec += (length-42)
            requests.append(node[i]) #add request to list

        else:
            #Replies

            #Match Replys with their Request
            for i in range(0, len(requests)):
                if( requests[i][4] == seq):
                   reqtime = requests[i][0]
                   reqsource = requests[i][1]
                   reqlen = requests[i][2]
                   reqttl = requests[i][5]
                   requests.remove(requests[i])
                   break

            #Collect Data on the Match
            if ( source == SEND_IP ) : #If the reply is being sent
                rep_sent += 1
                delay += ((time-reqtime) * 1000000 )
                #TTL of the sent reply will be default value, TTL of the recieved
                 

            else : #If reply is being recieved
                rep_rec += 1
                rtt += ((time - reqtime) * 1000 )
                hop += (reqttl-ttl)+1

    #after every packet has been computed
    delay /= req_rec
    hop /= req_sent
    throughput = (bytesSent / 1000) / (rtt / 1000) 
    goodput = dataSent / rtt
    rtt /= req_sent

    #Write Data
    f.write('\n' + 'Echo Requests Sent, Echo Requests Received, Echo Replies Sent, Echo Replies Received')
    f.write('\n' + str(req_sent) + ',' + str(req_rec) + ',' + str(rep_sent) + ',' + str(rep_rec))
    f.write('\n' + 'Echo Request Bytes Sent (bytes), Echo Request Data Sent (bytes)')
    f.write('\n' + str(bytesSent) + ',' + str(dataSent))
    f.write('\n' + 'Echo Request Bytes Received (bytes), Echo Request Data Received (bytes)')
    f.write('\n' + str(bytesRec) + ',' + str(dataRec) + '\n')
    f.write('\n' + 'Average RTT (milliseconds) , ' + str(round(rtt,2)))
    f.write('\n' + 'Echo Request Throughput (kB/sec) , ' + str(round(throughput,2)))
    f.write('\n' + 'Echo Request Goodput (kB/sec) , ' + str(round(goodput,2)))
    f.write('\n' + 'Average Reply Delay (microseconds) , ' + str(round(delay,2)))
    f.write('\n' + 'Average Echo Request Hop Count , ' + str(round(hop,2)))
