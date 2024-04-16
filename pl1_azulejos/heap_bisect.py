import heapq
import bisect


class HeapBis:
    def __init__(self, arr):
        self.arr = [
            (-key, element) for key, element in arr
        ]  # Transforming Min-Heap to Max-Heap
        heapq.heapify(self.arr)

    def push(self, key, element):
        heapq.heappush(
            self.arr, (-key, element)
        )  # Store negative key for max-heap functionality

    def pop(self):
        if len(self.arr) == 0:
            raise Exception("Empty heap")
        key, element = heapq.heappop(self.arr)
        return -key, element

    def peek(self):
        if len(self.arr) == 0:
            raise Exception("Empty heap")
        key, element = self.arr[0]
        return -key, element

    def pop_max_below(self, value):
        """
        Get largest element smaller than a given value (might not be stored).
        Assumes that the value parameter refers to the key, not the element.
        """
        temp = sorted(self.arr, reverse=True)

        keys = [-t[0] for t in temp]

        index = bisect.bisect_left(keys, value)
        if index == 0:
            return None
        max_below = temp[index - 1]

        self.arr.remove(max_below)
        heapq.heapify(self.arr)
        return -max_below[0], max_below[1]

    def pop_min_above(self, value):
        """
        Get smallests element bigger than a given value (might not be stored).
        Assumes that the value parameter refers to the key, not the element.
        """
        temp = sorted(self.arr, reverse=True)

        keys = [-t[0] for t in temp]

        index = bisect.bisect_right(keys, value)

        min_above = temp[index]
        self.arr.remove(min_above)
        heapq.heapify(self.arr)
        return -min_above[0], min_above[1]

    def __len__(self):
        return len(self.arr)

    def __str__(self) -> str:
        return self.arr.__str__()
