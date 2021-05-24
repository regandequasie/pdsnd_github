import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please choose a city: new york city, chicago, or washington\n").lower()
    # test input
    while city not in ['chicago', 'new york city', 'washington']:
        city = input ("Incorrect input. Please choose chicago, new york city or washington: ").lower()
        
    # show them their selection

    print("Great. You entered {}.".format(city))


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please pick a month: january, february, march, april, may, or june. If you would like no month filter, type          all\n").lower()
    
    # test input
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = input ("Incorrect input. Please pick a month: january, february, march, april, may, or june. If you would like no         month filter, type all\n").lower()
        
    # show them their selection 

    print("Great. You entered {}.".format(month))

        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please pick a day of the week: sunday, monday, tuesday, wednesday, thursday, friday, saturday, or sunday. If you would like no day filter, type all\n").lower()
    
    # test input
    day = input ("Incorrect input. Please pick a day of the week: sunday, monday, tuesday, wednesday, thursday, friday, saturday, or sunday. If you would like no day filter, type all\n").lower()
    # show them their selection
    
    print("Great. You entered {}.".format(day))
            
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please choose a city: new york city, chicago, or washington\n").lower()
    # test input
    while city not in ['chicago', 'new york city', 'washington']:
        city = input ("Incorrect input. Please choose chicago, new york city or washington: ").lower()
        
    # show them their selection
    print("Great. You entered {}.".format(city))


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please pick a month: january, february, march, april, may, or june. If you would like no month filter, type all\n").lower()
    
    # test input
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = input ("Incorrect input. Please pick a month: january, february, march, april, may, or june. If you would like no month filter, type all\n").lower()
        
    # show them their selection 
    print("Great. You entered {}.".format(month))
          

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please pick a day of the week: sunday, monday, tuesday, wednesday, thursday, friday, saturday, or sunday. If you would like no day filter, type all\n").lower()
    
    #test input
    while day not in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:

    day = input ("Incorrect input. Please pick a day of the week: sunday, monday, tuesday, wednesday, thursday, friday, saturday, or sunday. If you would like no day filter, type all\n").lower()
    # show them their selection
    
    print("Great. You entered {}.".format(day))
            
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

# load data file into a dataframe - getting city data frame
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)


    # TO DO: display the most common day of week   
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day of the Week:', popular_day)

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)


    # TO DO: display the most common day of week   
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day of the Week:', popular_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["popular combination"] = df["Start Station"] + ', ' + df["End Station"]
    popular_station_combination = df['popular combination'].mode()[0]
    print('Most frequent combination of start station and end station:', popular_station_combination)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time:", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Average travel time:", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender - account for df possibly not having data
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender)
        
    # TO DO: Display earliest, most recent, and most common year of birth - account for df possibly not having data
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print("The earliest birth year:", earliest)
        print("The most recent birth year:", most_recent)
        print("The most common birth year:", most_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# prompt user to see if they want to see raw data according to their filters
def raw_data (df):
    """Displays the data due filteration.
    5 rows will added in each press"""
    print('press enter to see 5 rows of raw data, press no to exit')
    x = 0
    while (input()!= 'no'):
        x = x+5
        print(df.head(x))

      
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data (df)
      
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


