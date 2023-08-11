import time


"""
We're given a list of strings
find the shortest within that list
if there's an equal short, return the first instance
"""

"""
first strag would be:
    count every entry
    store the first
    replace what's stored if it's less (not less than or equal to)

    ["test", "helllo", "robert", "flying", "fly", "ball" ]
     
    store = 3
    return fly

second way:
    create a dictionary 

"""

def main(string_array):

    tracker = None
    length = 0

    for word in string_array:
        if tracker == None:
            tracker = word
            length = len(tracker)
            continue
        
        if length > len(word):
            tracker = word
            length = len(word)


    return tracker


if __name__ == "__main__":
    test_values = [
        ["tester", "ball", "house", "fly", "united", "aerospace"],
        ["aaaa", "bbbb", "cccc", "dddd", "a", "b"],
        ["united airlines", "airplane", "macbook air", "", "airplane", "airplane", "airplane", "airplane", "airplane"]
    ]
    test_answers= [
        "fly",
        "a",
        ""
    ]


    for value, answer in zip(test_values, test_answers):
        result = main(value)

        assert answer == result, f"Incorrect answer, expected {answer}, got {result}"
        print(f"Successful test")

    #BENCHMARK
    start_time = time.time()

    for i in range(1000):
        main(['flower', 'juniper', 'lily', 'dandelion'])

    avg_time = ( time.time() - start_time ) / 1000

    print(avg_time)