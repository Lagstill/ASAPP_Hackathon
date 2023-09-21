#http://127.0.0.1:8000/docs#/default/schedule_job_endpoint_schedule_job_post

from prediction_transforms import get_prediction_cpuid
from fastapi import FastAPI,Query
from scheduling_algo import Job, build_max_heap,in_queue
from typing import List

app = FastAPI()

result = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: []
}

cpu_queues = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: []
}

def schedule_job_fn(job_info,buffer_size):
    cpu_id = get_prediction_cpuid(job_info)
    priority = int(job_info[-2])
    start_time = int(job_info[-1])
    job_id = job_info[0]
    cpu_queue = cpu_queues[cpu_id]
    cpu_queue.append(Job(priority, start_time, job_id))
    max_heap,finished = build_max_heap(cpu_queue,buffer_size)
    in_queue_process = in_queue(max_heap)
    result[cpu_id] = {
        "queue": in_queue_process,
        "finished": finished
    }

@app.post("/schedule_job")
async def schedule_job_endpoint(job_info: List[str] = Query(None)):
    schedule_job_fn(job_info,buffer_size=3)
    cpu_queues_state = {cpu_id: result[cpu_id] for cpu_id in result}
    return str(cpu_queues_state)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

