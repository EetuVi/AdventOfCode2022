from Util.file_reader import get_lines


def main():
    file = open("input.txt")
    lines = get_lines(file, True)
    overlapping_sectors_task1 = 0
    overlapping_sectors_task2 = 0
    for line in lines:
        elf1, elf2 = line.split(",")
        sect1 = [int(x) for x in elf1.split("-")]
        sect2 = [int(x) for x in elf2.split("-")]
        overlap_task1 = check_overlap_task1(sect1, sect2)
        overlap_task2 = check_overlap_task2(sect1, sect2)
        overlapping_sectors_task1 += overlap_task1
        overlapping_sectors_task2 += overlap_task2
    print("Overlapping sectors task 1: ", overlapping_sectors_task1)
    print("Overlapping sectors task 2: ", overlapping_sectors_task2)


def check_overlap_task1(sect1, sect2):
    if sect1[0] <= sect2[0] <= sect1[1]:
        if sect1[0] <= sect2[1] <= sect1[1]:
            return 1

    if sect2[0] <= sect1[0] <= sect2[1]:
        if sect2[0] <= sect1[1] <= sect2[1]:
            return 1

    return 0


def check_overlap_task2(sect1, sect2):
    if sect1[0] <= sect2[0] <= sect1[1]:
        return 1
    if sect1[0] <= sect2[1] <= sect1[1]:
        return 1

    if sect2[0] <= sect1[0] <= sect2[1]:
        return 1
    if sect2[0] <= sect1[1] <= sect2[1]:
        return 1
    return 0

if __name__ == '__main__':
    main()