import subprocess
import time

# Record the start time
start_time = time.time()

# Execute main.py using subprocess
subprocess.run(['python3', 'trainDictionary.py'])

# Record the end time
end_time = time.time()

# Calculate the total time including main.py execution
total_time = end_time - start_time

print(f"Total time including execution: {total_time:.4f} seconds")
