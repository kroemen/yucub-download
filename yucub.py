from pytube import YouTube as yete
import time
import datetime
from os import system as st
import sys
'''
watch and learn it.
dont forget for give a star and follow my github yeaa.
coded by github.com/kroemen.
iam still newbie and still learn python.
どうぞ、あっっとありがとうございます
fb : Denvert Leistuch
'''
あおい = ('\033[0;36m')
き= ('\033[1;33m')
みどり = ('\033[0;32m')
あかい = ('\033[31;1m')

st('clear')

banner = (f'''
{あかい}__   __        _____     _                     _ _ 
{あかい}\ \ / /       |_   _|   | |                   | | |
{あかい} \ V /___  _   _| |_   _| |__   ___         __| | |
{あかい}  \ // _ \| | | | | | | | '_ \ / _ \       / _` | |
{き}  | | (_) | |_| | | |_| | |_) |  __/ ____ | (_| | |
{き}  \_/\___/ \__,_\_/\__,_|_.__/ \___||____| \__,_|_|
{みどり}                             ____________________ 
{みどり}{datetime.datetime.now()}  |{あかい} github.com/kroemen {みどり}|
{みどり}                            ``````````````````````
{あおい}''')

def animation():
    animation = '/-|\\'
    for i in range(100):
        time.sleep(0.2)
        sys.stdout.write('\r\tʟօǟɖɨռɢ '+animation[i%len(animation)])
        sys.stdout.flush()

def main():
    try:
        print('\n')
        yu = yete(url)
        res = (yu.streams.all())
        for i in range(len(res)):
            print(i,'. ',res[i])
        print(f'\n{き}Song Title: {yu.title}{あおい}')
    except Exception:
        st('python yucub.py')
    except KeyboardInterrupt:
        print('EXIT')
    print(' Except:\n\tFor music select mime_type="audio/webm"\n')
    reso = int(input('Input The Resolution on Number: '))
    res[reso].download(r'/sdcard/ytdownload')
    print(f'{あかい}\n\t\t[!]Finish Download\n{あおい}')
    print('Check our download on /sdcard/ytdownload')
    print('Except:\n\tfor change to music, Change the extension file to .webm and play on GooglePlayMusic\n\tGBRAND-TrapSad.webm ==> GBRAND-TrapSad.mp3')

if __name__== "__main__":
    print(banner)
    url = input('Input URL: ')
    animation()
    main()
