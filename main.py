from datetime import datetime

def penjadwalan_greedy(tasks):
    schedule = []
    tasks.sort(key=lambda x: (x[1], -x[2]))
    current_time = 0
    for task in tasks:
        duration = task[3] * 24
        deadline = task[1].timestamp()
        if current_time + duration <= deadline:
            schedule.append(task)
            current_time += duration
    return schedule

def get_tasks(num_tasks):
    tasks = []
    for i in range(num_tasks):
        try:
            nama, deadline_str, kesulitan_str, duration_str = input(f"Masukkan tugas {i+1} (Nama, Deadline (format: DD/MM/YYYY), Tingkat kesulitan, Durasi): ").split(", ")
            deadline = datetime.strptime(deadline_str.strip(), "%d/%m/%Y")
            kesulitan = min(max(int(kesulitan_str.strip()), 1), 10)
            duration = int(duration_str.strip())
            tasks.append((nama.strip(), deadline, kesulitan, duration))
        except ValueError:
            print("Format input salah. Pastikan Anda memasukkan semua informasi dengan benar.")
            return get_tasks(num_tasks)
    return tasks

def print_schedule(schedule):
    print("Jadwal Tugas:")
    for i, task in enumerate(schedule, 1):
        print(f"{i}. {task[0]} (Deadline: {task[1].strftime('%d/%m/%Y')}, Tingkat Kesulitan: {task[2]}), Durasi: {task[3]})")

num_tasks = int(input("Masukkan jumlah tugas: "))
tasks = get_tasks(num_tasks)

print("\nJadwal Tugas sebelum diurutkan:")
print_schedule(tasks)

schedule = penjadwalan_greedy(tasks)

print("\nJadwal Tugas setelah diurutkan berdasarkan deadline dan tingkat kesulitan:")
print_schedule(schedule)