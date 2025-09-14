#  		insertion_sort.py			Sep 10, 2025
#  				Adrián E. Córdoba [software.dynamicmcs@gmail.com]
#
#  Copyright (C) 2025
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

def sort_0(array):
    """Typical insertion sort algorithm implementation."""
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def upward(x, y):
    return x < y


def downward(x, y):
    return x > y


def sort_1(array, *, direction=upward):
    """Implementation of the insertion sort algorithm
    that receives a parameter with the name of the function
    that determines the sorting direction."""
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and direction(key, array[j]):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def sort_2(array, *, direction=lambda x, y: x < y):
    """Implementation of the insertion sort algorithm
    that receives a parameter with the lambda expression
    that determines the order of sorting."""
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and direction(key, array[j]):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
