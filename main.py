import matplotlib.pyplot as plt
import time
import random


class TVChannel:
    def __init__(self, name, viewers, viewing_time):
        self.name = name
        self.viewers = viewers
        self.viewing_time = viewing_time


def create_channel(i):
    name = f"Channel {i}"
    viewers = random.randint(500, 2000000)
    viewing_time = random.randint(30, 180)
    return TVChannel(name, viewers, viewing_time)


def rate_channel(channel):
    if channel.viewers >= 1500000:
        return "Rank 1 - Excellent"
    elif channel.viewers >= 1000000:
        return "Rank 2 - Great"
    elif channel.viewers >= 500000:
        return "Rank 3 - Good"
    elif channel.viewers >= 300000:
        return "Rank 4 - Average"
    elif channel.viewers >= 100000:
        return "Rank 5 - Poor"
    else:
        return "Rank 6 - Just shut down!"


def plot_sorting_algorithms():
    sorting_algorithms = ["Merge Sort", "Quick Sort", "Bubble Sort", "Selection Sort", "Insertion Sort"]
    running_times = []

    for algorithm in sorting_algorithms:
        # Generate random data for sorting
        data = [random.randint(1, 1000) for _ in range(1000)]

        # Measure running time of the sorting algorithm
        start_time = time.time()

        # Sort the data
        if algorithm == "Quick Sort":
            quick_sort(data)
        elif algorithm == "Selection Sort":
            selection_sort(data)
        elif algorithm == "Insertion Sort":
            insertion_sort(data)
        elif algorithm == "Merge Sort":
            merge_sort(data)
        elif algorithm == "Bubble Sort":
            bubble_sort(data)

        end_time = time.time()
        running_time = end_time - start_time
        running_times.append(running_time)

    plt.bar(sorting_algorithms, running_times)
    plt.xlabel("Sorting Algorithms")
    plt.ylabel("Running Time (seconds)")
    plt.title("Running Time of Sorting Algorithms")
    plt.show()


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        smaller = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(smaller) + [pivot] + quick_sort(greater)

    return quick_sort(lesser) + [pivot] + quick_sort(greater)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

        return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# App menu
def app_menu():
    channels = []
    while True:
        print("\nTV Channel App")
        print("1. Create 10 channels")
        print("2. Rate channels")
        print("3. Plot sorting algorithms")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            for i in range(0, 10):
                channel = create_channel(i + 1)
                channels.append(channel)
            print("Channels created successfully!")
        elif choice == "2":
            for channel in channels:
                rating = rate_channel(channel)
                print(f"{channel.name}:\n {channel.viewers} viewers, {channel.viewing_time} hours, {rating}")
        elif choice == "3":
            plot_sorting_algorithms()
        elif choice == "4":
            print("Exiting the app...")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the app
app_menu()