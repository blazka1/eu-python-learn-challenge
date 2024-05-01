from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        result = []
        for item in input_array:
            should_include, transformed_item = func(item)
            if should_include:
                result.append(transformed_item)
        return result
