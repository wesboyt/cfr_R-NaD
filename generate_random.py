from sim_hand import Hand
from sim_encoder import Encoder
import random
import multiprocessing
import json

def generate_hands(queue):
    encoder = Encoder()
    while True:
        hand = Hand()
        player = random.randint(0, 5)
        while not hand.done:
            action_space = hand.get_action_space()
            match random.choice(list(action_space.keys())):
                case 'fold':
                    hand.fold()
                case 'check':
                    hand.check()
                case 'call':
                    hand.call()
                case 'min_bet':
                    hand.bet_or_raise(random.randint(action_space['min_bet'], action_space['max_bet']))
                case 'max_bet':
                    hand.bet_or_raise(random.randint(action_space['min_bet'], action_space['max_bet']))
        queue.put(encoder.encode(json.dumps(hand.get_u_hand(player)), True, True))



if __name__ == '__main__':
    num_threads = 16
    work_queue = multiprocessing.Queue(3000)
    threads = []
    outfile = open("random_hands.txt", 'wt')

    for i in range(num_threads):
        thread = multiprocessing.Process(target=generate_hands, args=[work_queue], daemon=True)
        thread.start()
        threads.append(thread)
    while True:
        handhistory = work_queue.get()
        outfile.write(handhistory + '\n')