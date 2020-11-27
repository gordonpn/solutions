def processLogFile(logs, threshold):
    """
    :type logs: List[str]
    :type threshold: int
    :rtype: List[str]
    """
    usage = {}
    results = []
    for log in logs:
        this_log = log.split()
        sender = this_log[0]
        recipient = this_log[1]
        if sender == recipient:
            if sender not in usage:
                usage[sender] = 1
            else:
                usage[sender] += 1
            continue
        if sender not in usage:
            usage[sender] = 1
        else:
            usage[sender] += 1
        if recipient not in usage:
            usage[recipient] = 1
        else:
            usage[recipient] += 1

    data_list = list(usage.items())
    data_list.sort(key=lambda x: x[1])
    for item in data_list:
        if item[1] >= threshold:
            results.append(item[0])
    return results


logs1 = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
threshold1 = 2

print(processLogFile(logs1, threshold1))  # ['88', '99']
