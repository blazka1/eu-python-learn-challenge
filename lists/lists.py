class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        if not input_list:
            return []

        def find_max_value(lst: list[int]) -> int:
            max_value = lst[0]
            for item in lst:
                if item > max_value:
                    max_value = item
            return max_value

        max_value = find_max_value(input_list)
        return [max_value if x > 0 else x for x in input_list]

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        def binary_search(low: int, high: int) -> int:
            if high >= low:
                mid = (high + low) // 2
                if input_list[mid] == query:
                    return mid
                elif input_list[mid] > query:
                    return binary_search(low, mid - 1)
                else:
                    return binary_search(mid + 1, high)
            else:
                return -1

        return binary_search(0, len(input_list) - 1)

