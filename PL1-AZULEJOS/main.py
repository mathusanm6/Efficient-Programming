from heap_bisect import HeapBis

n = int(input())
price_bg = [int(i) for i in input().split()]
height_bg = [int(i) for i in input().split()]
price_fg = [int(i) for i in input().split()]
height_fg = [int(i) for i in input().split()]

range1_n = list(range(n))
bg = list(zip(price_bg, height_bg, range1_n))
fg = list(zip(price_fg, height_fg, range1_n))

bg.sort(key=lambda azulejos: azulejos[0])
fg.sort(key=lambda azulejos: azulejos[0])

idx_bg, idx_fg = 0, 0
prev_price_bg, prev_price_fg = None, None

heap_bg = HeapBis([])
heap_fg = HeapBis([])

result_bg = []
result_fg = []

to_break = False


def fill_heap():
    global idx_bg, idx_fg
    if len(heap_bg) == 0 and idx_bg < len(bg):
        prev_price_bg = bg[idx_bg][0]
        while idx_bg < len(bg) and bg[idx_bg][0] == prev_price_bg:
            element_bg = bg[idx_bg]
            heap_bg.push(element_bg[1], element_bg)
            idx_bg += 1

    if len(heap_fg) == 0 and idx_fg < len(fg):
        prev_price_fg = fg[idx_fg][0]
        while idx_fg < len(fg) and fg[idx_fg][0] == prev_price_fg:
            element_fg = fg[idx_fg]
            heap_fg.push(element_fg[1], element_fg)
            idx_fg += 1


while not to_break:
    fill_heap()  # Ensure both heaps are checked and filled at the start of the loop

    if len(heap_bg) == 0 or len(heap_fg) == 0:
        if idx_bg >= len(bg) and idx_fg >= len(fg):
            break

    if len(heap_bg) < len(heap_fg):

        while len(heap_bg) > 0 and len(heap_fg) > 0:
            element_heap_bg = heap_bg.peek()
            element_heap_fg = heap_fg.pop_max_below(element_heap_bg[0])

            if element_heap_fg is None:
                break

            element_heap_bg = heap_bg.pop()

            if element_heap_bg[0] <= element_heap_fg[0]:
                print("impossible")
                to_break = True
                break

            result_bg.append(element_heap_bg[1][2])
            result_fg.append(element_heap_fg[1][2])

    elif len(heap_bg) > len(heap_fg):
        while len(heap_bg) > 0 and len(heap_fg) > 0:
            element_heap_fg = heap_fg.peek()
            element_heap_bg = heap_bg.pop_min_above(element_heap_fg[0])

            if element_heap_bg is None:
                break

            element_heap_fg = heap_fg.pop()

            if element_heap_bg[0] <= element_heap_fg[0]:
                print("impossible")
                to_break = True
                break

            result_bg.append(element_heap_bg[1][2])
            result_fg.append(element_heap_fg[1][2])
    else:
        while len(heap_bg) > 0 and len(heap_fg) > 0:
            element_heap_bg = heap_bg.pop()
            element_heap_fg = heap_fg.pop()

            if element_heap_bg[0] <= element_heap_fg[0]:
                print("impossible")
                to_break = True
                break

            result_bg.append(element_heap_bg[1][2])
            result_fg.append(element_heap_fg[1][2])

def print_result_xg(result_xg):
    for i in range(n - 1):
        print(result_xg[i], end=" ")
    print(result_xg[n - 1])

if not to_break:
    for i in range(n):
        result_bg[i] += 1
        result_fg[i] += 1

    print_result_xg(result_fg)
    
