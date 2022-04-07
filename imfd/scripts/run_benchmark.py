import os
import sys
from shutil import rmtree
from subprocess import Popen, DEVNULL, PIPE
from time import time


# Config params
TIMEOUT = 60  # Max time per query in seconds
QUERY_EXEC = './../../../MillenniumDB-Dev/build/Release/bin/query'


# Execute a single query on MillenniumDB
def query_millennium(query_path, query_number, result_path):
    start_time = time()
    with open(result_path, 'w') as results_file, \
            open(query_path, 'r') as query_file:
        query_execution = Popen(
            [QUERY_EXEC],
            stdin=query_file,
            stdout=results_file,
            stderr=DEVNULL)
    exit_code = query_execution.wait()
    elapsed = int((time() - start_time) * 1000)
    p = Popen(['wc', '-l', result_path], stdout=PIPE, stderr=PIPE)
    result, _ = p.communicate()
    # 1 line from header + 2 for separators + 3 for stats
    results_count = int(result.strip().split()[0]) - 6
    with open(RESUME_FILE, 'a') as file:
        if exit_code == 0:
            file.write(f'{query_number},{results_count},OK,{elapsed}\n')
        elif elapsed >= TIMEOUT:
            file.write(f'{query_number},{results_count},TIMEOUT,{elapsed}\n')
        else:
            file.write(f'{query_number},0,ERROR,{elapsed}\n')


# Run MillenniumDB benchmark with queries from gMark
if __name__ == '__main__':
    try:
        in_dir = sys.argv[1]
        out_dir = sys.argv[2]
        rmtree(out_dir, ignore_errors=True)
        os.mkdir(out_dir)
        RESUME_FILE = f'{out_dir}/gmark.csv'  # Statistics file
        for subdir, dirs, files in os.walk(in_dir):
            for f in files:
                query_n = f[f.find('-') + 1:]
                query_millennium(os.path.join(subdir, f), query_n,
                                 os.path.join(out_dir, f'q{query_n}.txt'))
    except IndexError:
        print('Args are missing!')
