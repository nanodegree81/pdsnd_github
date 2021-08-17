#Import neccessary stuff
import time
import pandas as pd
import numpy as np
import datetime
import calendar

#create an fill variables
wrong_input = "This is not a valid choice. Please try again. "
ques_city = "Would you like to see Chicago, New York, or Washington? "
ques_month = "Would you like filter by month? If 'Yes' type the name (e.g. January), if not type 'No' "
ques_day = "Would you like filter by day? If 'Yes' type the name (e.g. Monday), if not type 'No' "

#import data
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#create arrays
city_list = ['Chicago', 'New York', 'Washington']
month_list = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'No']
day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'No']

#METHODS
### Get the input data from the user
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    input_city = input(ques_city)
    print ("You entered: " + input_city) 

    while input_city not in city_list :
        print (wrong_input)
        input_city = input(ques_city)
        print ("You entered: " + input_city) 
        
    # get user input for month (all, january, february, ... , june)
    input_month = input(ques_month)
    print ("You entered: " + input_month) 

    while input_month not in month_list :
        print (wrong_input)
        input_month = input(ques_month)
        print ("You entered: " + input_month) 

    # get user input for day of week (all, monday, tuesday, ... sunday)
    input_day = input(ques_day)
    print ("You entered: " + input_day) 

    while input_day not in day_list :
        print (wrong_input)
        input_day = input(ques_day)
        print ("You entered: " + input_day) 

    print('-'*40)
    return input_city, input_month, input_day

### load csv files based on the input data
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
    if city == city_list[0]:
        df = pd.read_csv('chicago.csv')
    elif city == city_list[1]:
        df = pd.read_csv('new_york_city.csv')
    elif city == city_list[2]:
        df = pd.read_csv('washington.csv')    

    # create all neccessary columns for futher questions
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df['station_combi'] = 'Start: ' + df['Start Station'] + ' with End: ' + df['End Station']
    df['travel_duration'] = df['End Time']-df['Start Time']
    
    # filter data
    if not month == 'No':
        query1 = 'month ==' + str(month_list.index(month)+1)
        df = df.query(query1)
    
    if not day == 'No':
        df[df['day'].str.contains(day)]

    return df

###Calculate the most frequent times of travel
def time_stats(df):
     """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].value_counts().idxmax()
    print(popular_month)
    print('The most popular month: ', datetime.date(1900, popular_month, 1).strftime('%B'))
 
    # display the most common day of week
    popular_day = df['day'].value_counts().idxmax()
    print('The most popular day: ', popular_day)

    # display the most common start hour
    popular_hour = df['hour'].value_counts().idxmax()
    print('The most popular hour: ', popular_hour, ' o\'clock')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

### Calculate the most popular stations and trip
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df['Start Station'].value_counts().idxmax()
    print('The most popular Start Station: ', popular_start)

    # display most commonly used end station
    popular_end = df['End Station'].value_counts().idxmax()
    print('The most popular End Station: ', popular_end)

    # display most frequent combination of start station and end station trip
    popular_combi = df['station_combi'].value_counts().idxmax()
    print('The most popular Start and End Station combination - ', popular_combi)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


### Calculate the total and average trip duration
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_dur = df['travel_duration'].sum()
    print('The total travel time: ', total_dur)

    # display mean travel time
    mean_dur = df['travel_duration'].mean()
    print('The mean travel time: ', mean_dur)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


###Display statistics on bikeshare users
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    if 'Gender' in df.columns:
        # display counts of gender
        gender_types = df['Gender'].value_counts()
        print('Counts of gender types: ')
        print(gender_types)

    if 'Birth Year' in df.columns:
        # display earliest, most recent, and most common year of birth
        recent_year = df['Birth Year'].max()
        earliest_year = df['Birth Year'].min()
        mostcommon_year = df['Birth Year'].value_counts().idxmax()
        print('Most recent birth year: ', recent_year)
        print('Earliest birth year: ', earliest_year)
        print('Most common birth year: ', mostcommon_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

###Display Data
def display_data(df):
    view_data = input('\nWould you like to view the first 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0

    while (view_data.lower() == 'yes' and (start_loc+4) <= len(df)):
      print (df.loc[start_loc:start_loc+4,:])
      start_loc += 5
      view_data = input("Do you wish to continue?: ").lower()

### Main Function
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if not df.empty:
            
            display_data(df)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

        else:
            print('There is no data for selection')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
