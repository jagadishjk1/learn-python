"""
Task: Simple Log Analyzer
Concepts: functions, loops, if-elif-else, string methods, accumulator pattern

Analyze a list of simulated log lines. Count how many are INFO,
WARNING, and ERROR level. Extract and print only the ERROR messages
separately. Use functions to organize the logic.
"""

log_lines = [
    "[INFO] Server started successfully",
    "[WARNING] High memory usage detected",
    "[ERROR] Failed to connect to database",
    "[INFO] User admin logged in",
    "[ERROR] Disk space critically low",
    "[WARNING] Slow response time on API",
    "[INFO] Backup completed",
    "[ERROR] Service crashed unexpectedly",
]

def get_log_level(log_line):
    level_clean = log_line.lstrip("[").split("]")
    log_level = level_clean[0]
    return log_level

#take whole list and process it
def count_log_levels(log_lines):
    info_count = 0
    warning_count = 0
    error_count = 0
    invaild_count = 0
    error_list = []
    #looping each log line
    for log in log_lines:
        critical_level = get_log_level(log)
        if critical_level == "INFO":
            info_count += 1
        elif critical_level == "WARNING":
            warning_count += 1
        elif critical_level == "ERROR":
            error_count += 1
            error_list.append(log)
        else:
            invaild_count += 1

    return info_count, warning_count, error_count, error_list

def print_errors(error_logs):
    print ("\n--- ERROR MESSAGES ---")
    for error in error_logs:
        print(error)
    print ("\n------------")


info, warning, error,error_lines = count_log_levels(log_lines)

print("Log Summary:")
print(f"INFO:{info}")
print(f"WARNING:{warning}")
print(f"ERROR:{error}")

print_errors(error_lines)

    

