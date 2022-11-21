from filter_packets import *
from packet_parser import *
from compute_metrics import *

filter()
node1, node2, node3, node4 = parse()
compute(node1, node2, node3, node4)
