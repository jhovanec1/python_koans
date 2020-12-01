#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrays in the Ruby Koans
#

from runner.koan import *

class AboutLists(Koan):
    def test_creating_lists(self):
        empty_list = list()
        self.assertEqual(list, type(empty_list))
        self.assertEqual(True, len(empty_list)==0)

    def test_list_literals(self):
        nums = list()
        self.assertEqual([], nums)

        nums[0:] = [1]
        self.assertEqual([1], nums)

        nums[1:] = [2]
        self.assertListEqual([1, 2], nums)

        nums.append(333)
        self.assertListEqual([1, 2, 333], nums)

    def test_accessing_list_elements(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(True, noms[0]== 'peanut')
        self.assertEqual(True, noms[3]== 'jelly')
        self.assertEqual(True, noms[-1]=='jelly')
        self.assertEqual(True, noms[-3]=='butter')

    def test_slicing_lists(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(True, noms[0:1]==['peanut'])
        self.assertEqual(True, noms[0:2]==['peanut','butter'])
        self.assertEqual(True, noms[2:2]==[])
        self.assertEqual(True, noms[2:20]==['and','jelly'])
        self.assertEqual(True, noms[4:0]==[])
        self.assertEqual(True, noms[4:100]==[])
        self.assertEqual(True, noms[5:0]==[])

    def test_slicing_to_the_edge(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(True, noms[2:]==['and','jelly'])
        self.assertEqual(True, noms[:2]==['peanut','butter'])

    def test_lists_and_ranges(self):
        self.assertEqual(range, type(range(5)))
        self.assertNotEqual([1, 2, 3, 4, 5], range(1,6))
        self.assertEqual(True, list(range(5))==[0,1,2,3,4])
        self.assertEqual(True, list(range(5, 9))==[5,6,7,8])

    def test_ranges_with_steps(self):
        self.assertEqual(True, list(range(5, 3, -1))==[5,4])
        self.assertEqual(True, list(range(0, 8, 2))==[0,2,4,6])
        self.assertEqual(True, list(range(1, 8, 3))==[1,4,7])
        self.assertEqual(True, list(range(5, -7, -4))==[5,1,-3])
        self.assertEqual(True, list(range(5, -8, -4))==[5,1,-3,-7])

    def test_insertions(self):
        knight = ['you', 'shall', 'pass']
        knight.insert(2, 'not')
        self.assertEqual(True, knight==['you','shall','not','pass'])

        knight.insert(0, 'Arthur')
        self.assertEqual(True, knight==['Arthur','you','shall','not','pass'])

    def test_popping_lists(self):
        stack = [10, 20, 30, 40]
        stack.append('last')

        self.assertEqual(True, stack==[10,20,30,40,'last'])

        popped_value = stack.pop()
        self.assertEqual(True, popped_value=='last')
        self.assertEqual(True, stack==[10,20,30,40])

        popped_value = stack.pop(1)
        self.assertEqual(True, popped_value==20)
        self.assertEqual(True, stack==[10,30,40])

        # Notice that there is a "pop" but no "push" in python?

        # Part of the Python philosophy is that there ideally should be one and
        # only one way of doing anything. A 'push' is the same as an 'append'.

        # To learn more about this try typing "import this" from the python
        # console... ;)

    def test_making_queues(self):
        queue = [1, 2]
        queue.append('last')

        self.assertEqual(True, queue==[1,2,'last'])

        popped_value = queue.pop(0)
        self.assertEqual(True, popped_value==1)
        self.assertEqual(True, queue==[2,'last'])

        # Note, popping from the left hand side of a list is
        # inefficient. Use collections.deque instead.

