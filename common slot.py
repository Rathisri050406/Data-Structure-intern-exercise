slots1 = [[10, 50], [60, 120], [140, 210]]
slots2 = [[0, 15], [60, 70]]

# Get the meeting duration from user
meeting_duration = int(input("Enter meeting duration in minutes: "))

index_slot1 = 0
index_slot2 = 0

# Traverse both slot lists to find common time
while index_slot1 < len(slots1) and index_slot2 < len(slots2):
    # Get the overlapping window
    start_time = max(slots1[index_slot1][0], slots2[index_slot2][0])
    end_time = min(slots1[index_slot1][1], slots2[index_slot2][1])
    
    # Check if this overlapping window is enough for the meeting
    if end_time - start_time >= meeting_duration:
        print("Meeting time:", [start_time, start_time + meeting_duration])
        break

    # Move the pointer which has the earlier end time
    if slots1[index_slot1][1] < slots2[index_slot2][1]:
        index_slot1 += 1
    else:
        index_slot2 += 1
else:
    print("No common slot found.")
