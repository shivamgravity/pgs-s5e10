# returns the processed dataframe

# import required libraries
import pandas as pd

# function
def preprocess(df):
    road_type = []
    for x in df['road_type']:
        if x == "urban":
            road_type.append(3)
        elif x == "highway":
            road_type.append(2)
        elif x == "rural":
            road_type.append(1)
        else:
            print("Road Type Error!")
            break
    df['road_type'] = road_type

    lighting = []
    for x in df['lighting']:
        if x == "daylight":
            lighting.append(1)
        elif x == "dim":
            lighting.append(2)
        elif x == "night":
            lighting.append(3)
        else:
            print("Lightning Type Error!")
            break
    df['lighting'] = lighting

    weather = []
    for x in df['weather']:
        if x == "clear":
            weather.append(1)
        elif x == "foggy":
            weather.append(2)
        elif x == "rainy":
            weather.append(3)
        else:
            print("Weather Type Error!")
            break
    df['weather'] = weather

    road_signs_present = []
    for x in df['road_signs_present']:
        if x is True:
            road_signs_present.append(-1)
        elif x is False:
            road_signs_present.append(1)
        else:
            print("Road Sign Type Error!")
            break
    df['road_signs_present'] = road_signs_present

    public_road = []
    for x in df['public_road']:
        if x is True:
            public_road.append(1)
        elif x is False:
            public_road.append(-1)
        else:
            print("Public Road Type Error!")
            break
    df['public_road'] = public_road

    time_of_day = []
    for x in df['time_of_day']:
        if x == "afternoon":
            time_of_day.append(1)
        elif x == "morning":
            time_of_day.append(2)
        elif x == "evening":
            time_of_day.append(3)
        else:
            print("Time of day Error!")
            break
    df['time_of_day'] = time_of_day

    holiday = []
    for x in df['holiday']:
        if x is True:
            holiday.append(1)
        elif x is False:
            holiday.append(-1)
        else:
            print("Holiday Error!")
            break
    df['holiday'] = holiday

    school_season = []
    for x in df['school_season']:
        if x is True:
            school_season.append(-1)
        elif x is False:
            school_season.append(1)
        else:
            print("School Error!")
            break
    df['school_season'] = school_season

    return df

if __name__ == '__main__':
    df = input("Enter dataset file location: ")
    df = preprocess(df)
    df.head()