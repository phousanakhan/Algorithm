class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """ 
        Do not return anything, modify matrix in-place instead.
        """
        _dict = {}
        for _list in matrix:
            for index,element in enumerate(_list):
                if index in _dict:
                    _dict[index].append(element)
                else:
                    _dict[index] = [element]
                 
        for i in _dict:
            _dict[i].reverse()
            matrix[i] = _dict[i]