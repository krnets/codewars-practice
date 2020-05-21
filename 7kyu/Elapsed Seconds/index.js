// 7kyu - Elapsed Seconds

/* Complete the function so that it returns the number of seconds that have elapsed between the start and end times given.

    The start/end times are given as Date instances.
    The start time will always be before the end time. */

const elapsedSeconds = (startDate, endDate) => (endDate - startDate) / 1000

q = elapsedSeconds(new Date("Thu Feb 27 2020 09:28:04 GMT+1100 (Australian Eastern Daylight Time)"), new Date("Thu Feb 27 2020 09:29:52 GMT+1100 (Australian Eastern Daylight Time)"))
q
// 108