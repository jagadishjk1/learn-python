"""
Task: Deployment Readiness Checker
Concepts: functions, return, *args/**kwargs, validation functions,
          orchestrator pattern, if-elif-else

Simulate checking whether a server is "ready" for deployment based
on a few conditions, using small validation functions tied together
by one orchestrator function.
"""
#validation function
def has_enough_disk(disk_percent_used):
    return disk_percent_used < 90

def has_enough_memory(memory_percent_used):
    return memory_percent_used < 85

def is_service_running(status):
    return status == "running"

#orchestrator function
def check_deployment_ready(disk, memory, status):
    disk_st=has_enough_disk(disk)
    memory_st=has_enough_memory(memory)
    status_st=is_service_running(status)
    return disk_st and memory_st  and status_st

#main funtion
deployment_1 = {"disk" : 85, "memory" : 80, "status" : "running"}
deployment_2 = {"disk" : 85, "memory" : 90, "status" : "running"}
deployment_3 = {"disk" : 95, "memory" : 80, "status" : "running"}
deployment_4 = {"disk" : 85, "memory" : 80, "status" : "stopped"}

# Pack them into a master dictionary to keep track of their names
all_deployments = {
    "deployment_1": deployment_1,
    "deployment_2": deployment_2,
    "deployment_3": deployment_3,
    "deployment_4": deployment_4
} 

#status print
ready_status = "Ready for deployment"
not_ready_status = "NOT ready for deployment"

#loop
for name, deploy in all_deployments.items():
    # print(deploy)
    status=check_deployment_ready(**deploy)
    if status:
        print(f"{name}: {ready_status}")
    else:
        print(f"{name}: {not_ready_status}")