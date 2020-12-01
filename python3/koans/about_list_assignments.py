#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrayAssignments in the Ruby Koans
#

from runner.koan import *

class AboutListAssignments(Koan):
    def test_non_parallel_assignment(self):
        names = ["John", "Smith"]
        self.assertEqual(True, names==['John', 'Smith'])

    def test_parallel_assignments(self):
        first_name, last_name = ["John", "Smith"]
        self.assertEqual(True, first_name== 'John')
        self.assertEqual(True, last_name=='Smith')

    def test_parallel_assignments_with_extra_values(self):
        title, *first_names, last_name = ["Sir", "Ricky", "Bobby", "Worthington"]
        self.assertEqual(True, title=='Sir')
        self.assertEqual(True, first_names==['Ricky','Bobby'])
        self.assertEqual(True, last_name=='Worthington')

    def test_parallel_assignments_with_sublists(self):
        first_name, last_name = [["Willie", "Rae"], "Johnson"]
        self.assertEqual(True, first_name==['Willie','Rae'])
        self.assertEqual(True, last_name=='Johnson')

    def test_swapping_with_parallel_assignment(self):
        first_name = "Roy"
        last_name = "Rob"
        first_name, last_name = last_name, first_name
        self.assertEqual(True, first_name=='Rob')
        self.assertEqual(True, last_name=='Roy')

