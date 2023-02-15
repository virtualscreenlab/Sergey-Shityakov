def time_format(start_time, end_time):
    total = end_time - start_time
    hours = int(total / 3600)
    total -= hours * 3600
    minutes = int(total / 60)
    seconds = int(total - minutes * 60)
    return hours, minutes, seconds