class Quicksort:

    def recursive_sort(list):

        def quicksort(list, low, high):

            # if the low/high indexes haven't flipped
            if low < high:

                # partition index, which is sorted
                partition_index = partition(list, low, high)

                # sort the low side
                quicksort(list, low, partition_index - 1)

                # sort the high side
                quicksort(list, partition_index + 1, high)

        def partition(list, low, high):

            # set the pivot
            pivot = list[high]

            # index of low
            i = low

            for j in range(low, high):

                # if current is smaller than pivot
                if list[j] <= pivot:

                    # swap i (less than pivot) and j (greater than pivot)
                    list[i], list[j] = list[j], list[i]

                    # move up the index
                    i += 1

            # swap the low index marker (i) and the pivot
            list[i], list[high] = list[high], list[i]

            return i

        # sort
        quicksort(list, 0, len(list)-1)

        return list

    recursive_sort = staticmethod(recursive_sort)
