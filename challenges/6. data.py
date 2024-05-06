"""
A pharmaceutical company wants to know whether an experimental drug affects systolic blood pressure.
Fifteen randomly selected subjects were given the drug and, after sufficient time for the drug to have an impact,
their systolic blood pressures were recorded.
The data appears in a python list.

THE FOLLOWING POINTS MUST BE DONE USING SOME FUNCTIONS OF SOME MODULE, AND WITH ANOTHER FUNCTION THAT YOU BUILT,
THAT IS, IMITATE THE BEHAVIOUR OF THAT FUNCTION

1. Calculate the value of 'x bar' (sample mean) and the value of s (the sample standard deviation)

"""

data = [172, 140, 123, 130, 115, 148, 108, 129, 137, 161, 123, 152, 133, 128, 142]

import statistics

def sample_statistics(data):
    sample_mean = statistics.mean(data)
    sample_stdev = statistics.stdev(data)
    return sample_mean, sample_stdev

def main():
    data = [172, 140, 123, 130, 115, 148, 108, 129, 137, 161, 123, 152, 133, 128, 142]
    sample_mean, sample_stdev = sample_statistics(data)
    print("Sample Mean (x̄):", sample_mean)
    print("Sample Standard Deviation (s):", sample_stdev)

if __name__ == "__main__":
    main()
