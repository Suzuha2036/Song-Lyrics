#include <iostream>
#include <chrono>
#include <thread>

using namespace std;

void showLyrics( const string lyrics, int typeSpeed,int pause){
    for(int i = 0; i < lyrics.length();i++){
        cout<<lyrics[i]<<flush;
        this_thread::sleep_for(chrono::milliseconds(typeSpeed));
    }
    this_thread::sleep_for(chrono::milliseconds(pause));
    cout<<endl;
}


int main()
{
    showLyrics("Cause no one will love you,",94,210);
    showLyrics("Like her",92,43);
    showLyrics("It's pointless",95,55);
    showLyrics("Like tears in the rain",110,3010);
    showLyrics("So now that she's gone",123,410);
    showLyrics("Embrace all that comes",134,113);
    showLyrics("And die with a smile",124,213);
    showLyrics("Don't show the world how alone you've become",174,33);
    

    return 0;
}