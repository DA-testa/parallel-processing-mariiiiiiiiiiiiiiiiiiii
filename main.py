# python3
import heapq


def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threads = [(0,i) for i in range(n)]
    heapq.heapify(threads)
    
    for duration in data:
        thread = heapq.heappop(threads)
        output.append((thread[1],thread[0]))
        heapq.heappush(threads,(thread[0]+duration,thread[1]))

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n,m = map(int,input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int,input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for index,time in result:
        print(index,time)



if __name__ == "__main__":
    main()
