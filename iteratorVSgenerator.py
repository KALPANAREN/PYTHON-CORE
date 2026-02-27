l1 = [1,2,4,5,7]
print(dir(l1))
i1 = iter(l1)
print(dir(i1))

class MyIterator():
    def __init__(self,start,finish):
        self.begin =  start
        self.end = finish
    def __iter__(self):
        return self
    def __next__(self):
        if self.begin>self.end:
            raise StopIteration
        current = self.begin
        self.begin+=1
        return current

m1 = MyIterator(4,10)
for m in m1:
    print(m)


# generator

def gen_func(n):
    for  i in range(n):
        yield i
    
x = list(gen_func(8))
print(x)

# STREAMING LONG PIPELINES USING YIELD FROM

import json
from functools import wraps

def read_lines(stream):
    """Yield lines lazily from a file-like object."""
    for line in stream:
        yield line

def parse_json(lines):
    """Convert lines to dicts, skipping malformed JSON."""
    for line in lines:
        try:
            yield json.loads(line)
        except (json.JSONDecodeError, TypeError):
            continue

def filter_logs(logs, *, level=None, service=None):
    """Filter by log level and/or service."""
    for log in logs:
        if level is not None and log.get("level") != level:
            continue
        if service is not None and log.get("service") != service:
            continue
        yield log

def filter_time_range(logs, start_ts=None, end_ts=None):
    for log in logs:
        ts = log.get("timestamp")
        if ts is None:
            continue
        if start_ts is not None and ts < start_ts:
            continue
        if end_ts is not None and ts > end_ts:
            continue
        yield log

def transform_logs(logs):
    for log in logs:
        yield {
            "ts": log.get("timestamp"),
            "svc": log.get("service"),
            "msg": log.get("message"),
        }

def count_items(fn):
    """
    Wrap a generator function and count yielded items
    without breaking laziness.
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        count = 0
        for item in fn(*args, **kwargs):
            count += 1
            yield item
        wrapper.last_count = count
    wrapper.last_count = 0
    return wrapper

filter_logs = count_items(filter_logs)
transform_logs = count_items(transform_logs)

def _pipeline_gen(stream, *, level=None, service=None, start_ts=None, end_ts=None):
    """
    Internal generator used for yield-from delegation.
    Returns total processed count.
    """
    lines = read_lines(stream)
    parsed = parse_json(lines)
    filtered = filter_logs(parsed, level=level, service=service)
    timed = filter_time_range(filtered, start_ts, end_ts)
    transformed = transform_logs(timed)

    total = 0
    for item in transformed:
        total += 1
        yield item

    return total  # captured by yield from

def build_pipeline(stream, *, level=None, service=None, start_ts=None, end_ts=None):
    """
    Public pipeline entry.
    Delegates execution and returns processed count.
    """
    total = yield from _pipeline_gen(
        stream,
        level=level,
        service=service,
        start_ts=start_ts,
        end_ts=end_ts,
    )
    return total

# ANOTHER EXAMPLE FOR GENERATOR PIPELINE

"""
firstly, let us see non scalable version
"""
def extract_code():
    pass
lines = open("huge.log").read().splitlines()
errors = [l for l in lines if "ERROR" in l]
codes = [extract_code(l) for l in errors]

#generator pipeline version

def read_lines(path):
    with open(path,'r') as rf:
        for line in rf:
            yield line

def filter_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line

def extract_codes(lines):
    for line in lines:
        yield extract_code(line)

pipeline = extract_codes(filter_errors(read_lines("huge_file.log")))

for code in pipeline:
    # process(code)
    pass