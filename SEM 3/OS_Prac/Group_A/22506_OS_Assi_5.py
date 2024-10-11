#Yogesh Bhandare SE AIDS 22506
#Write a program to implement page Replacement strategies (FIFO, LRU,Optimal)
class PageReplacement:
    def __init__(self, page_frames):
        self.page_frames = page_frames
        self.pages = []
        self.page_faults = 0

    def fifo(self):
        print("\nFIFO Page Replacement:")
        frame_set = set()
        queue = []

        for page in self.pages:
            if page not in frame_set:
                self.page_faults += 1
                if len(frame_set) < self.page_frames:
                    frame_set.add(page)
                    queue.append(page)
                else:
                    removed_page = queue.pop(0)
                    frame_set.remove(removed_page)
                    frame_set.add(page)
                    queue.append(page)

            print(f"Page {page}: {list(frame_set)}")

        print(f"Total Page Faults: {self.page_faults}")

    def lru(self):
        print("\nLRU Page Replacement:")
        frame_list = []
        page_dict = {}

        for page in self.pages:
            if page not in frame_list:
                self.page_faults += 1
                if len(frame_list) < self.page_frames:
                    frame_list.append(page)
                else:
                    lru_page = min(page_dict, key=page_dict.get)
                    frame_list[frame_list.index(lru_page)] = page
                page_dict[page] = 0

            for key in page_dict:
                page_dict[key] += 1

            print(f"Page {page}: {frame_list}")

        print(f"Total Page Faults: {self.page_faults}")

    def optimal(self):
        print("\nOptimal Page Replacement:")
        frame_list = []

        for i, page in enumerate(self.pages):
            if page not in frame_list:
                self.page_faults += 1
                if len(frame_list) < self.page_frames:
                    frame_list.append(page)
                else:
                    future_pages = self.pages[i+1:]
                    for j, frame in enumerate(frame_list):
                        if frame not in future_pages:
                            frame_list[j] = page
                            break
                        elif j == len(frame_list) - 1:
                            frame_list[j] = page

            print(f"Page {page}: {frame_list}")

        print(f"Total Page Faults: {self.page_faults}")

    def simulate(self, pages):
        self.pages = pages
        self.fifo()
        self.page_faults = 0
        self.lru()
        self.page_faults = 0
        self.optimal()


# Example usage:
if __name__ == "__main__":
    page_frames = 3
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 1, 2, 0, 1, 7, 0, 1]

    page_replacement = PageReplacement(page_frames)
    page_replacement.simulate(pages)
