# Intro

Dear applicant,

First of all, thank you for taking the time to do this. We ask
people to perform it not because we believe it gives us a definitive
view of a candidate's skill but rather as conversation-starter.

For that reason, we've put in a few elements that we hope you pick up.

Do not spend more than 4 hours on completing it. We know you're busy.

Thanks again, and we hope it doesn't bore you :)

# Description

In the root directory you find [./tracks.json] which contains a list of Spotify `trackId`s.

Please write a program that when executed, reads the track-ids from the input file and outputs
an HTML `table`, which is made-up of 3 columns: `title`, `artist` and `release_date` Please look up
these bits of data using the [Spotify web API](https://developer.spotify.com/documentation/web-api/).

The program should take two mandatory arguments from the command-line: 
 1. `-o [FILENAME]`. This is the file it will write its output to, which 
    we should be able to open in a web-browser. No need to bother with styling.
 2. `-t [TOKEN]` the authorization token your program will need to contact the Spotify API.

**A few pointers:**

 - You will need a (free) Spotify account to [create a dummy spotify app](https://developer.spotify.com/documentation/general/guides/authorization/app-settings/).
 - To get a token, pass the `client-id` and `client-secret` belonging to 
   the app you created above to [./get-token.sh](get-token.sh) script to get it.
   Run it like so `./get-token.sh [client-id] [client-secret]`
 - Pick any language you find suitable for this task.
 - Use any 3rd-party library you like if you feel so inclined.
   If you do this, please use the well-known build/dependency-tooling to get them (eg pypi, maven, npm). 
   Do not add them to the git repo.
 - The spotify API returns the 'artist' as a json-array. You can simply pick the first element from that array.
 - Please put instructions in the [RUNNING.md](RUNNING.md) file with any instructions we need 
   to be able to run the program (e.g. install dependencies)
 - Once completed to your satisfaction, commit the result to the git-repo, tar+gzip it, 
   and email it to [hr@we4sea.com]


**BONUS**
- Sort the tracks by release-date in ascending order.
- What if [./tracks.json](tracks.json) contained a thousand tracks, and we would need the results within a few seconds?
(ignore any rate-limiting).
