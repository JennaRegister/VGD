# here is an array with 200 numbers in it, all between 1 and 1000
the_array = [563, 683, 752, 73, 452, 851, 21, 861, 199, 476, 395, 807, 563, 987, 926, 633, 88, 789, 428, 58, 134, 618, 104, 392, 864, 106, 477, 161, 906, 846, 117, 555, 393, 82, 509, 695, 987, 202, 200, 585, 362, 580, 410, 917, 549, 289, 359, 694, 218, 430, 704, 324, 209, 727, 523, 409, 443, 277, 911, 715, 937, 595, 72, 820, 810, 306, 525, 32, 868, 17, 822, 701, 64, 10, 468, 286, 945, 211, 265, 94, 197, 65, 480, 925, 241, 282, 3, 255, 169, 48, 437, 292, 383, 742, 996, 390, 625, 563, 241, 717, 549, 133, 510, 904, 670, 786, 215, 186, 59, 280, 400, 623, 839, 109, 685, 97, 73, 252, 575, 749, 32, 879, 109, 84, 884, 29, 45, 889, 319, 473, 597, 714, 397, 421, 285, 83, 557, 855, 956, 721, 717, 548, 30, 926, 562, 981, 128, 649, 255, 393, 942, 83, 75, 615, 875, 31, 372, 593, 683, 265, 804, 73, 205, 918, 112, 153, 347, 735, 684, 422, 790, 768, 991, 460, 706, 366, 664, 529, 129, 546, 791, 379, 564, 982, 542, 442, 244, 434, 256, 848, 360, 938, 674, 452, 496, 695, 612, 385, 371, 811];

# here is another one with different values
the_other_array = [169, 969, 159, 964, 972, 659, 141, 148, 879, 330, 786, 37, 97, 5, 9, 316, 278, 709, 557, 742, 382, 559, 687, 691, 189, 24, 627, 121, 989, 554, 491, 941, 51, 848, 820, 744, 539, 742, 687, 273, 789, 711, 320, 26, 878, 280, 519, 934, 234, 659, 445, 705, 345, 240, 764, 320, 170, 201, 437, 398, 618, 794, 872, 811, 65, 279, 39, 842, 973, 632, 596, 31, 898, 545, 434, 495, 793, 916, 50, 54, 339, 933, 280, 295, 276, 117, 123, 457, 634, 542, 31, 722, 47, 314, 848, 816, 676, 967, 194, 608, 178, 712, 832, 749, 413, 308, 464, 874, 191, 60, 530, 592, 43, 22, 431, 961, 333, 359, 819, 283, 658, 219, 946, 870, 160, 233, 999, 974, 597, 722, 340, 759, 281, 799, 164, 832, 939, 607, 206, 724, 197, 132, 41, 256, 509, 122, 553, 904, 573, 854, 711, 439, 587, 217, 595, 134, 323, 446, 897, 592, 866, 812, 929, 541, 994, 149, 972, 201, 883, 251, 809, 913, 150, 346, 108, 290, 528, 990, 375, 301, 12, 395, 989, 462, 616, 402, 556, 128, 400, 840, 622, 993, 793, 865, 731, 399, 679, 922, 535, 285]


def get_minimum(array):
    # returns the minimum value of a given array

    minimum_so_far = 1001

    for num in array:
        # YOUR CODE HERE
        pass # pass is just a 'placeholder' that tells python that nothing goes here yet. you can - and should - delete it

    return minimum_so_far

def get_sum(array):
    # returns the sum of all the values of a given array

    # YOUR CODE HERE
    pass

print("the smallest number of the_array is", get_minimum(the_array)) # should be 3
print("the sum of the_array is", get_sum(the_array)) # should be 95911

print("the smallest number of the_other_array is", get_minimum(the_other_array)) # should be 5
print("the sum of the_other_array is", get_sum(the_other_array)) # should be 102513