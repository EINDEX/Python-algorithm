import random
from algorithm.sort import *

class TestSort:
    def gene_list(self):
        for i in range(11):
            yield [random.randint(0, 2**i) for _ in range(2**i)]

    def sort_t(self, sort_func):
        g = self.gene_list()
        res = []
        for l in g:
            lt = l[:]
            lt.sort()
            res.append(lt == sort_func(l))
        
        return all(res)
    
    def test_bubble_sort(self):
        assert self.sort_t(bubble_sort)

    def test_bubble_sort_flag(self):
        assert self.sort_t(bubble_sort_flag)

    def test_count_sort(self):
        assert self.sort_t(count_sort)

    def test_shell_sort(self):
        assert self.sort_t(shell_sort)

    def test_seletion_sort(self):
        assert self.sort_t(selection_sort)

    def test_marge_sort(self):
        assert self.sort_t(merge_sort)

    def test_quick_sort(self):
        assert self.sort_t(quick_sort)

    
    def test_quick_sort_cookbook(self):
        assert self.sort_t(quick_sort_cookbook)

    def test_insert_sort(self):
        assert self.sort_t(insert_sort)
    

    def test_heap_sort(self):
        assert self.sort_t(heap_sort)
    
