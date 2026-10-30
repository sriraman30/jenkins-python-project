import datetime

print("-------------------------------------------------")
print("Hello Jenkins! Python Script run aaga start aagiduchu...")

# Current time edukurathu
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Oru puthu text file create panni athula ezhuthurathu
with open("output.txt", "w") as file:
    file.write(f"Jenkins automated this file creation at {current_time}!\n")
    file.write("Python scripting automation success.")

print("Task Completed: 'output.txt' file automatic-a create aagiduchu.")
print("-------------------------------------------------")
