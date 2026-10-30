count = 0
bottles = 99
pass_beer = "Take one down and pass it around,"
wall_beer = "of beer on the wall"

while count < 3:
    while bottles > 0:
        plural_or_single_former = "bottle" if bottles == 1 else "bottles"
        line_1 = f"{bottles} {plural_or_single_former} {wall_beer}, {bottles} {plural_or_single_former} of beer."
        print(line_1)
        bottles -= 1
        plural_or_single_latter = "bottle" if bottles == 1 else "bottles"
        int_or_no_more = bottles if bottles > 0 else "no more"
        line_2 = f"{pass_beer} {int_or_no_more} {plural_or_single_latter} {wall_beer}."
        print(line_2)
    if bottles == 0:
        print("Go to the store and buy some more,", "99 bottles of beer on the wall.")
    count += 1
    bottles = 99

print(
    f"We sang that {count} times and went through about {99 * count} bottles of beer.\nNext destination: h...hopital"
)
