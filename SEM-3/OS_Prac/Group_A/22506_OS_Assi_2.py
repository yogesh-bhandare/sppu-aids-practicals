#Yogesh Bhandare SE AIDS 22506
#Implement producer-consumer problem with counting semaphores and mutex
import threading
import time
import random

BUFFER_SIZE = 5
BUFFER = []
mutex = threading.Semaphore(1)
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)


class Producer(threading.Thread):
    def run(self):
        for _ in range(10):  # Number of items to produce
            item = random.randint(1, 100)
            empty.acquire()
            mutex.acquire()
            BUFFER.append(item)
            print(f"Produced {item}. Buffer: {BUFFER}")
            mutex.release()
            full.release()
            time.sleep(random.uniform(0.1, 0.5))


class Consumer(threading.Thread):
    def run(self):
        for _ in range(10):  # Number of items to consume
            full.acquire()
            mutex.acquire()
            item = BUFFER.pop(0)
            print(f"Consumed {item}. Buffer: {BUFFER}")
            mutex.release()
            empty.release()
            time.sleep(random.uniform(0.1, 0.5))


def main():
    producer = Producer()
    consumer = Consumer()

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print("Program Execution Completed.")


if __name__ == "__main__":
    main()
