#!/usr/bin/env python3
import calendar
class TestCal:
	def test_leapyear(self):
		assert calendar.isleap(2024) 
	def test_leapyear2(self):
		assert calendar.isleap(2028)
	def test_leapyear3(self):
		assert calendar.isleap(2032)
	def test_leapyear4(self):
		assert calendar.isleap(2036)
	def test_leapyear5(self):
		assert calendar.isleap(2040)

