class SelectionSort:
    def _min_index(self,array:list) -> any:
        less = array[0]
        less_index = 0
        for index in range(1, len(array)):
            if less > array[index]:
                less = array[index]
                less_index = index
        
        return less_index

    def sort(self,array:list) -> list:
        sorted_array = []
        for i in range(len(array)):
            sorted_array.append(array.pop(self._min_index(array)))
        return sorted_array    
