import re


def read_logs(log_file):
    log_pattern = re.compile(r"^(?P<time>\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3})\s+(?P<tag>\S+)\s+(?P<message>.*)$")
    parsed_logs = []  # 用来装所有解析好的日志
    current_log = None  # 缓冲区

    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            match = log_pattern.match(line)

            if match:
                if current_log is not None:
                    parsed_logs.append(current_log)
                    current_log = []

                current_log = match.groupdict()
            else:
                if current_log is not None:
                    current_log["message"]+=f"\n{line}"

        if current_log is not None:
            parsed_logs.append(current_log)

    return parsed_logs


logs = read_logs("nlog_20260227.log.0.txt")

for index,log in enumerate(logs):
    print(f"这是第{index+1}条日志")
    print(f"时间:{log['time']}")
    print(f"正文:{log['message']}")