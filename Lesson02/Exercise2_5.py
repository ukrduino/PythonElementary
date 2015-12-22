# Write a function that computes a large factorial using multiple threads
import threading
from Queue import Queue
from operator import mul

from Lesson02.Exercise2_1 import factorial_loop
from Lesson02.Exercise2_4 import factorial_l
from Lesson02.Exercise2_4 import wrapped_with_timer


# @wrapped_with_timer
def multiply_numbers_in_chunk(chunk, queue):
    chunk_id = str(chunk[0]) + "_" + str(chunk[-1])
    queue.put({chunk_id: reduce(mul, chunk)})


@wrapped_with_timer
def factorial_of_big_number_in_threads(number, number_of_threads):
    if number < 100:
        print "Calculating factorial of " + str(number) + " in 1 threads."
        return factorial_l(number)
    else:
        # step 0 - restricting number of threads
        num_of_threads = 1
        if number_of_threads > 1:
            num_of_threads = number_of_threads
        elif number_of_threads >= 10:
            num_of_threads = 10

        print "Calculating factorial of " + str(number) + " in " + \
              str(num_of_threads) + " threads."

        # step 1 - create list of number that should be multiplied
        # i.e. for 5! -> [1, 2, 3, 4, 5]
        list_of_numbers_for_factorial = range(1, number + 1)

        # step 2 - splitting list_of_numbers_for_factorial for chunks(lists)
        # of certain length for calculating factorial in threads.
        # We need separate chunk fo each thread.
        full_chunk_length = len(list_of_numbers_for_factorial) // \
            num_of_threads + 1  # +1 for round up

        list_of_chunks = [list_of_numbers_for_factorial[i:i +
                                                        full_chunk_length]
                          for i in range(0, len(list_of_numbers_for_factorial),
                                         full_chunk_length)]
        q = Queue()
        threads = []
        # step 3 - Running multiply_numbers_in_chunk in separate threads,
        # threads will put results in queue

        for chunk in list_of_chunks:
            thr = threading.Thread(target=multiply_numbers_in_chunk,
                                   args=(chunk, q))
            thr.start()
            threads.append(thr)

        for t in threads:
            t.join()

        prod_list = list()
        # step 4 - getting results from queue to prod_list
        # and finally multiplying them
        queue_res_dict = [q.get() for _ in xrange(len(list_of_chunks))]
        for res in queue_res_dict:
            prod_list.append(res.values()[0])
        res = reduce(mul, prod_list)
        return res


if __name__ == "__main__":
    res1 = factorial_of_big_number_in_threads(54476, 5)
    res2 = factorial_l(54476)
    print "Check successful -> " + str(res1 == res2)

    res3 = factorial_of_big_number_in_threads(5, 10)
    res4 = factorial_loop(5)
    print "Check successful -> " + str(res3 == res4)
