import sys, argparse
import random, time, bext

WIDTH = 79
HEIGHT = 22
TREE = '^'
FIRE = '*'
EMPTY = ' '
INITIAL_TREE_DENSITY = 0.2
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01

PAUSE_LENGTH= 0.5

def displayForest(forest):
    bext.goto(0,0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x,y)] == TREE:
                bext.fg('green')
                print(TREE,end='')
            elif forest[(x,y)] == FIRE:
                bext.fg('red')
                print(FIRE,end='')
            elif forest[(x,y)] == EMPTY:
                print(EMPTY,end='')    
        print()
    bext.fg('reset')
    print('GROW CHANCE: {}% '.format(GROW_CHANCE *100), end='')
    print('Lighting CHANCE: {}% '.format(FIRE_CHANCE *100), end='')
    
    
def createNewforest():
    forest = { 'width' : WIDTH, 'height' : HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if(random.random() * 100 ) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY
            
    return forest
    
def main():
   forest = createNewforest()
   bext.clear()
   while True:
    displayForest(forest)
    nextforest = { 'width' : forest['width'], 'height' : forest['height']}
    
    for x in range(forest['width']):
        for y in range(forest['height']):
            if (x,y) in nextforest:
                continue
            if((forest[(x,y)] == EMPTY) and (random.random() <= GROW_CHANCE)):
                nextforest[(x, y)] = TREE
            elif((forest[(x,y)] == TREE) and (random.random() <= FIRE_CHANCE)):   
                nextforest[(x, y)] = FIRE
            elif(forest[(x,y)] == FIRE):   
                for ix in range(-1, 2):
                    for iy in range(-1, 2):
                        if forest.get((x + ix, y + iy)) == TREE:
                            nextforest[(x + ix, y + iy)] = FIRE
                nextforest[(x,y)] = EMPTY
            else:
                nextforest[(x,y)] = forest[(x,y)]
    forest = nextforest
    time.sleep(PAUSE_LENGTH)
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
