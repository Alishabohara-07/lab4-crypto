import numpy as np

def exhaust_memory():
    try:
        # List to keep track of allocated arrays
        memory_hog = []
        while True:
            # Allocate a large NumPy array
            array_size = 10**7  # 10 million elements
            large_array = np.zeros(array_size, dtype=np.uint8)
            memory_hog.append(large_array)
            print(f"Allocated array with {array_size} elements")
    except MemoryError:
        print("Memory exhausted!")

if __name__ == "__main__":
    exhaust_memory()
