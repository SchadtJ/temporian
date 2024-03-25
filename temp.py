import temporian as tp
import numpy as np

def main():
    a = tp.event_set(
        timestamps=[0, 1, 2, 5, 6, 7],
        features={
            "value": [np.nan, 1, 5, 10, 15, 20],
            "other": [7,100,2,3,4,5]
        },
    )
    b = a.min()
    print(b)
    # print("TOMATO SALAD")
    # print(b.end())

    # for index_data in b.data.values():
    #     print(repr(index_data.features))
    # # print("CAR")
    # # print(b.__dict__)

if __name__ == "__main__":
    main()