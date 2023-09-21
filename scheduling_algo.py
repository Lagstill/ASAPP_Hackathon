import heapq

class Job:
    def __init__(self, priority, arrival_time, job_name):
        self.priority = priority
        self.arrival_time = arrival_time
        self.job_name = job_name

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.arrival_time < other.arrival_time
        return self.priority > other.priority

def build_max_heap(jobs,b_size):
    max_heap = []
    finished = []
    size = b_size
    for job in jobs:
        if size==len(max_heap):
            j1 = heapq.heappop(max_heap)
            temp = [j1.job_name,j1.priority,j1.arrival_time]
            finished.append(temp)
            # print(f"Finished {j1.job_name} (Priority: {j1.priority}, Arrival Time: {j1.arrival_time})")
        heapq.heappush(max_heap, job)
    return max_heap,finished


def in_queue(max_heap):
    processing = []
    while max_heap:
        job = heapq.heappop(max_heap)
        temp = [job.job_name,job.priority,job.arrival_time]
        processing.append(temp)
        # print(f"Processing {job.job_name} (Priority: {job.priority}, Arrival Time: {job.arrival_time})")
    return processing
