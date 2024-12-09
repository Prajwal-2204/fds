def bubble_sort(arr):
    """
    Bubble sort implementation to sort an array of floating point numbers in ascending order.
    """
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def display_top_scores(arr, top_n=5):
    """
    Display top scores from a sorted array.
    """
    if len(arr) < top_n:
        top_n = len(arr)
    print(f"Top {top_n} scores:")
    for score in arr[-top_n:]:
        print(score)

def main():
    # Example array of 12th class percentages (can be user input as well)
    percentages = [87.5, 91.2, 85.0, 78.3, 92.7, 95.1, 83.9, 89.6, 81.4, 90.0, 88.2, 94.5]

    # Sort percentages using bubble sort
    bubble_sort(percentages)

    # Display top 5 scores
    display_top_scores(percentages)

if __name__ == "__main__":
    main()
def bubble_sort(arr):
    """
    Bubble sort implementation to sort an array of floating point numbers in ascending order.
    """
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def display_top_scores(arr, top_n=5):
    """
    Display top scores from a sorted array.
    """
    if len(arr) < top_n:
        top_n = len(arr)
    print(f"Top {top_n} scores:")
    for score in arr[-top_n:]:
        print(score)

def main():
    # Example array of 12th class percentages (can be user input as well)
    percentages = [87.5, 91.2, 85.0, 78.3, 92.7, 95.1, 83.9, 89.6, 81.4, 90.0, 88.2, 94.5]

    # Sort percentages using bubble sort
    bubble_sort(percentages)

    # Display top 5 scores
    display_top_scores(percentages)

if __name__ == "__main__":
    main()
