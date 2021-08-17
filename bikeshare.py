#Import neccessary stuff
import time
import pandas as pd
import numpy as np

#create an fill variables
wrong_input = "This is not a valid choice. Please try again. "
ques_city = "Would you like to see Chicago, New York, or Washington? "
ques_month = "Would you like filter by month? If 'Yes' type the name (e.g. January), if not type 'None' "
ques_day = "Would you like filter by day? If 'Yes' type the name (e.g. Monday), if not type 'None' "

#import data
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#create arrays
city_list = ['Chicago', 'New York', 'Washington']
month_list = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'None']
day_list = ['Monday', 'Tuesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'None']

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    input_city = input(ques_city)
    print ("You entered: " + input_city) 

    while input_city not in city_list :
        print (wrong_input)
        input_city = input(ques_city)
        print ("You entered: " + input_city) 
        
    # TO DO: get user input for month (all, january, february, ... , june)
    input_month = input(ques_month)
    print ("You entered: " + input_month) 

    while input_month not in month_list :
        print (wrong_input)
        input_month = input(ques_month)
        print ("You entered: " + input_month) 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
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
    #select correct CSV
    if city == city_list[0]
        df = pd.read_csv('chicago.csv')
    elif city == city_list[1]
        df = pd.read_csv('new_york_city.csv')
    elif city == city_list[2]
        df = pd.read_csv('washington.csv')    


    # convert the Start Time column to datetime
    starttime = data['Start Time']
    data['Start Time'] = pd.to_datetime(data['Start Time'])

    # extract day from the Start Time column to create an month column
    data['month'] = data['Start Time'].dt.month
    
    # extract hour from the Start Time column to create an day column
    data['weekday'] = data['Start Time'].dt.day
    
    # create an hour column
    data['datehour'] = data['Start Time'].dt.hour

    #TO DO: Filtern  
    return df

###Calculate the most frequent times of travel
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    com_month = df['month'].value_counts().idxmax()
    print(com_month)

    # TO DO: display the most common day of week
    com_day = df['weekday'].value_counts().idxmax()
    print(com_day)
    
    # TO DO: display the most common start hour
    com_hour = df['datehour'].value_counts().idxmax()
    print(com_day)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

### Calculate the most popular stations and trip
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


### Calculate the total and average trip duration
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


###Display the results
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

### Main Function
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
