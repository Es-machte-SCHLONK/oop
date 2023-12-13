import random
import datetime


class Node:
    yellow = True
    green = False
    red = False
    black = False
    no = 0

    def __init__(self, no, yellow, green, red):
        self.no = int(no)
        self.yellow = bool(yellow)
        self.green = bool(green)
        self.red = bool(red)
        self.black = False

    def __init__(self, no, yellow, green, red, black):
        self.no = int(no)
        self.yellow = bool(yellow)
        self.green = bool(green)
        self.red = bool(red)
        self.black = bool(black)


class Connection:
    source = ""
    targets = []


class Mapgenerator:
    now = datetime.datetime.now().timestamp()
    random.seed(now)
    totalNodeCount = 0
    greenNodeCount = 0
    redNodeCount = 0
    blackNodeCount = 0
    randomInt = 0
    nodeList = []

    # Additional Information, based on official Scotland Yard map:
    #   every 3.333 nodes, a GREEN node.    >> 30 per 100  >> 300 per 1000
    #   every 13.333 nodes, a RED node.     >> 7,5 per 100 >> 75 per 1000
    #   every 40 nodes, a BLACK node.       >> 2,5 per 100 >> 25 per 1000
    #   Every RED node is also GREEN and YELLOW node.
    #   Black nodes are special.
    def __init__(self, total_node_count):
        self.totalNodeCount = int(total_node_count)
        # Statistical distribution of green, red and black nodes.
        for i in range(total_node_count):
            
            self.randomInt = random.randint(1, 1000)
            if self.randomInt <= 75:
                green = True
                red = True
            elif self.randomInt <= 300:
                green = True
                red = False
            else:
                green = False
                red = False

            if random.randint(1, 1000) <= 25:
                black = True
            else:
                black = False

            new_node = Node(i, True, green, red, black)
            self.nodeList.append(new_node)


print(now)

random.seed(now)

print(random.randint(0, 4))
print(random.randint(0, 4))
print(random.randint(0, 4))
print(random.randint(0, 4))
print(random.randint(0, 4))
print(random.randint(0, 4))
print(random.randint(0, 4))
print(random.randint(0, 4))
print(random.randint(0, 4))
print(random.randint(0, 4))
