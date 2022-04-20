import sys, os
import time, random
import wave, argparse, pygame
import numpy as np
from collections import deque
from matplotlib import pyplot as plt

gShowPlt = False

pmNotes = {'C4':262, 'Eb': 311, 'F': 349, 'Bb': 466}

def writeWave(fname, data):
    file = wave.open(fname, 'wb')
    nChannels = 1
    sampleWidth = 2
    frameRate = 44100
    nFrames = 44100
    file.setparams((nChannels, smapleWidth, frameRate, nFrames, 'NONE', 'noncompressed'))
    file.writeframes(data)
    file.close()

def generateNote(freq):
    nSmples = 44100
    sampleRate = 44100
    N = int(sampleRate/freq)
    buf = deque([random.random() - 0.5 for i in range(N)])
    if gShowPlt:
        axline, = plt.plot(buf)
    samples = np.array([0]*nSamples, 'float32')
    for i in range(nSamples):
        samples[i] = buf[0]
        avg = 0.995*0.5*(buf[0] + buf[1])
        buf.append(avg)
        buf.popleft()
        if gShowPlt:
            if i % 1000 == 0:
                axline.set_ydate(buf)
                plt.draw()
				
class NotePlayer:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, 2048)
        pygame.init()
        self.notes = {}
    def add(self, filename):
        self.notes[filename] = pygame.mixer.Sound(filename)
    def play(self, fileName):
        try:
            self.notes[fileName].play()
        except:
            print(fileName + ' not found!')

    def playRandom(self):
        index = random.randint(0, len(self.notes) -1)
        note = list(self.notes.values())[index]
        note.play()
def main():
    global gShowPlt
    parser = argparse.ArgumentParser(description="Generating sounds with Karplus string algorithm")
    parser.add_argument('--display', action='store_true', required=False)
    parser.add_argument('--play', action='store_true', required=False)
    parser.add_argument('--piano', action='store_true', required=False)
    args = parser.parse_args()
    if args_display:
        gShowPlt = True
        plt.ion() 
    nplayer = NotePlayer()
    print('create notes...')    
    for name, freq in list(pmNotes.items()):
        fileName = name + '.wav'
        if not os.path.exists(fileName) or args.display:
            data = generateNote(freq)
            print('creating ' + fileName + '...')
            writeWave(fileName, data)
        else:
            print('fileName already created. skipping...')   
        nplayer.add(name + '.wav')
        if args.display:
            nplayer.play(name + '.wav')
            time.sleep(0.5)      
    if args.play:
        while True:
            try:
                nplayer.playRandom()
                rest = np.random.choice([1,2,4,8],1, p=[0.15,0.7,0.1,0.05])
                time.sleep(0.25*rest[0])
            except KeyboardInterrupt:
                exit()
    if args.piano:
        while True:
            try:
                for event in pygame.event.get():
                    if (event.type == pygame.KEYUP):
                        print("key pressed")
                        nplayer.playRandom()
                        time.sleep(0.5)

if __name__ == '__main__':
    main()