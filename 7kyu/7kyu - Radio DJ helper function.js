// 7kyu - Radio DJ helper function

/* James is a DJ at a local radio station. As it's getting to the top of the hour, he needs to 
find a song to play that will be short enough to fit in before the news block. 
He's got a database of songs that he'd like you to help him filter in order to do that.

Create longestPossible(longest_possible in python and ruby) helper function that 
takes 1 integer argument which is a maximum length of a song in seconds.

songs is an array of objects which are formatted as follows:

{artist: 'Artist', title: 'Title String', playback: '04:30'}

You can expect playback value to be formatted exactly like above.

Output should be a title of the longest song from the database that matches the criteria of 
not being longer than specified time. If there's no songs matching criteria in the database, return false */

let songs = [{
    artist: 'Artist',
    title: 'Title String',
    playback: '04:30'
}]

function longestPossible(playback) {
    for (let song of songs) {
        [min, sec] = song.playback.split(':')
        song.time = min * 60 + sec * 1
    }
    songs.sort((a, b) => b.time - a.time)
    return (s = songs.find(v => v.time < playback)) ? s.title : false
}

q = longestPossible(215) // "For Reasons Unknown"
q