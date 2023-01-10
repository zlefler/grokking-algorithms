def can_attend_all_appointments(appointments):
    '''Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.'''

    # appointments.sort(key=lambda x: x[0])
    # start, end = 0, 1

    # for i in range(1, len(appointments)):
    #     if appointments[i][start] < appointments[i-1][end]:
    #         return False
    # return True


# Doesn't work:
    appointments.sort(key=lambda x: x[0])

    end = appointments[0][1]

    for i in range(1, len(appointments)):
        if appointments[i][0] < end:
            return False
        else:
            end = appointments[i][1]

    return True


def main():
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()
