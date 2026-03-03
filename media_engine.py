# media_engine.py
def play_count_stream(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i ** 2

def monitor(func):
    def wrapper(*args, **kwargs):
        print("Processing Started")
        result = func(*args, **kwargs)
        print("Processing Completed")
        return result
    return wrapper

@monitor
def run_stream(limit):
    total_plays = 0
    records = 0
    for val in play_count_stream(limit):
        total_plays += val
        records += 1
    return total_plays, records
