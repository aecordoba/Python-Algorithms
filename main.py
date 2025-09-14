#  		main.py			Sep 10, 2025
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

import insertion_sort

if __name__ == '__main__':
    array = [12, -4, 27, 5, 0, -2, 5, 9]
    insertion_sort.sort_0(array)
    print(f'Sorted array: {array}')

    array = [12, -4, 27, 5, 0, -2, 5, 9]
    insertion_sort.sort_1(array, direction=insertion_sort.downward)
    print(f'Sorted array: {array}')

    array = [12, -4, 27, 5, 0, -2, 5, 9]
    insertion_sort.sort_2(array, direction=lambda x, y: x > y)
    print(f'Sorted array: {array}')
