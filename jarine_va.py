import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
from feature import check_file, read_content
import pywhatkit


# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recognizer method for recognizing
def take_command():
    r = sr.Recognizer()

    # from the speech_Recognition module
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        print('Listening')

        # seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)

        # Now we will be using the try and catch
        # method so that if sound is recognized
        # it is good else we will have exception
        # handling
        try:
            print("Recognizing")

            # for Listening the command in indian
            # english we can also use 'hi-In'
            # for hindi recognizing
            query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", query)

        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return query


def speak(audio):
    engine = pyttsx3.init()
    # getter method(gets the current value
    # of engine property)
    voices = engine.getProperty('voices')

    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    engine.setProperty('voice', voices[1].id)

    # Method for the speaking of the the assistant
    engine.say(audio)

    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()


def tell_day():
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1

    # this line tells us about the number
    # that will help us in telling the day
    day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in day_dict.keys():
        day_of_the_week = day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def tell_time():
    # This method will give the time
    time = str(datetime.datetime.now())

    # the time will be displayed like
    # this "2020-06-05 17:50:14.582630"
    # nd then after slicing we can get time
    print(time)
    hour = time[11:13]
    mins = time[14:16]
    speak("The time is sir" + hour + "Hours and" + mins + "minutes")


def hello():
    # This function is for when the assistant
    # is called it will say hello and then
    # take query
    speak("hello sir I am Jarine, your virtual assistant. Tell me how may I help you")


def take_query():
    # calling the hello function for
    # making it more interactive
    hello()

    # This loop is infinite as it will take
    # our queries continuously until and unless
    # we don't say bye to exit or terminate
    # the program
    while True:

        # taking the query and making it into
        # lower case so that most of the times
        # query matches and we get the perfect
        # output
        query = take_command().lower()
        if "open geeksforgeeks" in query:
            speak("Opening GeeksforGeeks ")

            # in the open method we just to give the link
            # of the website and it automatically open
            # it in your default browser
            webbrowser.open("www.geeksforgeeks.com")
            #continue

        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            #continue

        elif "which day it is" in query:
            tell_day()
            #continue

        elif "tell me the time" in query:
            tell_time()
            #continue

        # this will exit and terminsate the program
        elif "bye" in query:
            speak("Bye. Check Out GFG for more exciting things")
            exit()

        elif "from wikipedia" in query:

            # if any one wants to have a information
            # from wikipedia
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")

            # it will give the summary of 4 lines from
            # wikipedia we can increase and decrease
            # it also.
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)

        elif "tell me your name" in query:
            speak("I am Jarine. Your desktop Assistant")

        elif "read the file" in query:
            query1 = []
            print('Ozzius:\t', query)
            query1.append(query.replace("read", '').replace('the file', '').replace('from', ''))
            query1 = ' '.join(query1).split()
            print('Ozzius2:\t', query1)
            filename = str(''.join(query1[:-1]))
            print('file_Name@172:\t', filename)
            path = str(query1[-1])
            print('path:\t', path)
            file = check_file(filename, path)
            print('file_Name:\t', file)
            data = read_content(file)
            speak(data)

        elif 'play song' in query:
            try:
                query_song = query.replace('play song', '')
                pywhatkit.playonyt(query_song)
            except:
                speak('repeat the song name again')


if __name__ == '__main__':
    take_query()
