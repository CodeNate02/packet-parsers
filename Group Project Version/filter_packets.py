def filter_node(filename, new_filename, data) :
    f = open(filename, 'r')

    line = f.readline().strip()
 
    header = line
    substring1 = 'reply'
    substring2 = 'request'

    while line :
        if substring1 in line :
            data.append(header)
            data.append(line)
            data.append('')
            
            line = f.readline().strip()
            if not line.strip() :
                line = f.readline().strip()
            while line :
                data.append(line)
                line = f.readline().strip()
                if not line.strip() :
                     data.append('')

        elif substring2 in line :
            data.append(header)
            data.append(line)
            data.append('')

            line = f.readline().strip()
            if not line.strip() :
                line = f.readline().strip()
            while line :
                data.append(line)
                line = f.readline().strip()
                if not line.strip() :
                     data.append('')

        line = f.readline().strip()
        if not line.strip() :
            line = f.readline().strip()

    f.close()


# Open new file to wrtie to
    f = open(new_filename, 'w')
    
    for iter in data :
        f.write(iter + "\n")

    f.close()

def filter() :

    n = 0

    for i in range( 1, 5 ) :
        filter_node('nodes/Node' + str(i) + '.txt', 'nodes/Node' + str(i) + '_Filtered.txt', Node_list[n])

        n = n + 1

#/////////////////////////////////////////// End Of Functions

Node1_filtered = []
Node2_filtered = []
Node3_filtered = []
Node4_filtered = []
Node_list = [Node1_filtered, Node2_filtered, Node3_filtered, Node4_filtered]



