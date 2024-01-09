from kata import evil
import codewars_test as test
import random

list_evil = [3, 5, 6, 9, 10, 12, 15, 17, 18, 20, 23, 24, 27, 29, 30, 33, 34, 36, 39, 40, 43, 45, 46, 48, 51, 53, 54, 57, 58, 60, 63, 65, 66, 68, 71, 72, 75, 77, 78, 80, 83, 85, 86, 89, 90, 92, 95, 96, 99, 101, 102, 105, 106, 108, 111, 113, 114, 116, 119, 120, 123, 125, 126, 129, 130, 132, 135, 136, 139, 141, 142, 144, 147, 149, 150, 153, 154, 156, 159, 160, 163, 165, 166, 169, 170, 172, 175, 177, 178, 180, 183, 184, 187, 189, 190, 192, 195, 197, 198]
list_odious = [1, 2, 4, 7, 8, 11, 13, 14, 16, 19, 21, 22, 25, 26, 28, 31, 32, 35, 37, 38, 41, 42, 44, 47, 49, 50, 52, 55, 56, 59, 61, 62, 64, 67, 69, 70, 73, 74, 76, 79, 81, 82, 84, 87, 88, 91, 93, 94, 97, 98, 100, 103, 104, 107, 109, 110, 112, 115, 117, 118, 121, 122, 124, 127, 128, 131, 133, 134, 137, 138, 140, 143, 145, 146, 148, 151, 152, 155, 157, 158, 161, 162, 164, 167, 168, 171, 173, 174, 176, 179, 181, 182, 185, 186, 188, 191, 193, 194, 196, 199]
test.assert_equals(evil(1),"It's Odious!")
test.assert_equals(evil(2),"It's Odious!")
test.assert_equals(evil(3),"It's Evil!")
test.assert_equals(evil(random.choice(list_evil)),"It's Evil!")
test.assert_equals(evil(random.choice(list_evil)),"It's Evil!")
test.assert_equals(evil(random.choice(list_evil)),"It's Evil!")
test.assert_equals(evil(random.choice(list_evil)),"It's Evil!")
test.assert_equals(evil(random.choice(list_evil)),"It's Evil!")
test.assert_equals(evil(random.choice(list_evil)),"It's Evil!")
test.assert_equals(evil(random.choice(list_odious)),"It's Odious!")
test.assert_equals(evil(random.choice(list_odious)),"It's Odious!")
test.assert_equals(evil(random.choice(list_odious)),"It's Odious!")
test.assert_equals(evil(random.choice(list_odious)),"It's Odious!")
test.assert_equals(evil(random.choice(list_odious)),"It's Odious!")
test.assert_equals(evil(random.choice(list_odious)),"It's Odious!")
list_evil1 = [3801, 3802, 3804, 3807, 3808, 3811, 3813, 3814, 3817, 3818, 3820, 3823, 3825, 3826, 3828, 3831, 3832, 3835, 3837, 3838, 3840, 3843, 3845, 3846, 3849, 3850, 3852, 3855, 3857, 3858, 3860, 3863, 3864, 3867, 3869, 3870, 3873, 3874, 3876, 3879, 3880, 3883, 3885, 3886, 3888, 3891, 3893, 3894, 3897, 3898, 3900, 3903, 3905, 3906, 3908, 3911, 3912, 3915, 3917, 3918, 3920, 3923, 3925, 3926, 3929, 3930, 3932, 3935, 3936, 3939, 3941, 3942, 3945, 3946, 3948, 3951, 3953, 3954, 3956, 3959, 3960, 3963, 3965, 3966, 3969, 3970, 3972, 3975, 3976, 3979, 3981, 3982, 3984, 3987, 3989, 3990, 3993, 3994, 3996, 3999]
list_odious1 = [3800, 3803, 3805, 3806, 3809, 3810, 3812, 3815, 3816, 3819, 3821, 3822, 3824, 3827, 3829, 3830, 3833, 3834, 3836, 3839, 3841, 3842, 3844, 3847, 3848, 3851, 3853, 3854, 3856, 3859, 3861, 3862, 3865, 3866, 3868, 3871, 3872, 3875, 3877, 3878, 3881, 3882, 3884, 3887, 3889, 3890, 3892, 3895, 3896, 3899, 3901, 3902, 3904, 3907, 3909, 3910, 3913, 3914, 3916, 3919, 3921, 3922, 3924, 3927, 3928, 3931, 3933, 3934, 3937, 3938, 3940, 3943, 3944, 3947, 3949, 3950, 3952, 3955, 3957, 3958, 3961, 3962, 3964, 3967, 3968, 3971, 3973, 3974, 3977, 3978, 3980, 3983, 3985, 3986, 3988, 3991, 3992, 3995, 3997, 3998]
test.assert_equals(evil(random.choice(list_evil1)),"It's Evil!")
test.assert_equals(evil(random.choice(list_evil1)),"It's Evil!")
test.assert_equals(evil(random.choice(list_evil1)),"It's Evil!")
test.assert_equals(evil(random.choice(list_evil1)),"It's Evil!")
test.assert_equals(evil(random.choice(list_evil1)),"It's Evil!")
test.assert_equals(evil(random.choice(list_evil1)),"It's Evil!")
test.assert_equals(evil(random.choice(list_odious1)),"It's Odious!")
test.assert_equals(evil(random.choice(list_odious1)),"It's Odious!")
test.assert_equals(evil(random.choice(list_odious1)),"It's Odious!")
test.assert_equals(evil(random.choice(list_odious1)),"It's Odious!")
test.assert_equals(evil(random.choice(list_odious1)),"It's Odious!")
test.assert_equals(evil(random.choice(list_odious1)),"It's Odious!")
list_evil2 = [5000000, 5000003, 5000005, 5000006, 5000009, 5000010, 5000012, 5000015, 5000017, 5000018, 5000020, 5000023, 5000024, 5000027, 5000029, 5000030, 5000033, 5000034, 5000036, 5000039, 5000040, 5000043, 5000045, 5000046, 5000048, 5000051, 5000053, 5000054, 5000057, 5000058, 5000060, 5000063, 5000064, 5000067, 5000069, 5000070, 5000073, 5000074, 5000076, 5000079, 5000081, 5000082, 5000084, 5000087, 5000088, 5000091, 5000093, 5000094, 5000097, 5000098, 5000100, 5000103, 5000104, 5000107, 5000109, 5000110, 5000112, 5000115, 5000117, 5000118, 5000121, 5000122, 5000124, 5000127, 5000129, 5000130, 5000132, 5000135, 5000136, 5000139, 5000141, 5000142, 5000144, 5000147, 5000149, 5000150, 5000153, 5000154, 5000156, 5000159, 5000160, 5000163, 5000165, 5000166, 5000169, 5000170, 5000172, 5000175, 5000177, 5000178, 5000180, 5000183, 5000184, 5000187, 5000189, 5000190, 5000192, 5000195, 5000197, 5000198]
list_odious2 = [5000001, 5000002, 5000004, 5000007, 5000008, 5000011, 5000013, 5000014, 5000016, 5000019, 5000021, 5000022, 5000025, 5000026, 5000028, 5000031, 5000032, 5000035, 5000037, 5000038, 5000041, 5000042, 5000044, 5000047, 5000049, 5000050, 5000052, 5000055, 5000056, 5000059, 5000061, 5000062, 5000065, 5000066, 5000068, 5000071, 5000072, 5000075, 5000077, 5000078, 5000080, 5000083, 5000085, 5000086, 5000089, 5000090, 5000092, 5000095, 5000096, 5000099, 5000101, 5000102, 5000105, 5000106, 5000108, 5000111, 5000113, 5000114, 5000116, 5000119, 5000120, 5000123, 5000125, 5000126, 5000128, 5000131, 5000133, 5000134, 5000137, 5000138, 5000140, 5000143, 5000145, 5000146, 5000148, 5000151, 5000152, 5000155, 5000157, 5000158, 5000161, 5000162, 5000164, 5000167, 5000168, 5000171, 5000173, 5000174, 5000176, 5000179, 5000181, 5000182, 5000185, 5000186, 5000188, 5000191, 5000193, 5000194, 5000196, 5000199]
test.assert_equals(evil(random.choice(list_evil2)),"It's Evil!")
test.assert_equals(evil(random.choice(list_evil2)),"It's Evil!")
test.assert_equals(evil(random.choice(list_evil2)),"It's Evil!")
test.assert_equals(evil(random.choice(list_evil2)),"It's Evil!")
test.assert_equals(evil(random.choice(list_evil2)),"It's Evil!")
test.assert_equals(evil(random.choice(list_evil2)),"It's Evil!")
test.assert_equals(evil(random.choice(list_odious2)),"It's Odious!")
test.assert_equals(evil(random.choice(list_odious2)),"It's Odious!")
test.assert_equals(evil(random.choice(list_odious2)),"It's Odious!")
test.assert_equals(evil(random.choice(list_odious2)),"It's Odious!")
test.assert_equals(evil(random.choice(list_odious2)),"It's Odious!")
test.assert_equals(evil(random.choice(list_odious2)),"It's Odious!")