#Yogesh Bhandare SE AIDS 22506
#Demonstrate Reader-Writer problem with reader priority or writer
import threading
import time

readers = 0
resource = 0
readers_mutex = threading.Semaphore(1)
writers_mutex = threading.Semaphore(1)
readers_count_mutex = threading.Semaphore(1)


class Reader(threading.Thread):
    def run(self):
        global readers
        with readers_mutex:
            readers += 1
            if readers == 1:
                writers_mutex.acquire()
        self.read_resource()
        with readers_mutex:
            readers -= 1
            if readers == 0:
                writers_mutex.release()

    def read_resource(self):
        with readers_count_mutex:
            print(f"Reader {self.ident} is reading. Resource value: {resource}")
        time.sleep(1)


class Writer(threading.Thread):
    def run(self):
        with writers_mutex:
            self.write_resource()

    def write_resource(self):
        global resource
        with readers_count_mutex:
            resource += 1
            print(f"Writer {self.ident} is writing. Resource value: {resource}")
        time.sleep(1)


def main():
    num_readers = 3
    num_writers = 2

    reader_threads = [Reader() for _ in range(num_readers)]
    writer_threads = [Writer() for _ in range(num_writers)]

    all_threads = reader_threads + writer_threads

    for thread in all_threads:
        thread.start()

    for thread in all_threads:
        thread.join()

    print("Program Execution Completed.")


if __name__ == "__main__":
    main()
