import requests
import json
import os
import click

cookies = {
    'PREF': 'hl=en&tz=UTC',
    'SOCS': 'CAI',
    'GPS': '1',
    'YSC': 'Nz90PHqwzjQ',
    'VISITOR_INFO1_LIVE': 'qdEa8-nzhn8',
    'VISITOR_PRIVACY_METADATA': 'CgJJThIEGgAgJA%3D%3D',
}
headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'com.google.ios.youtube/19.09.3 (iPhone14,3; U; CPU iOS 15_6 like Mac OS X)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-us,en;q=0.5',
    'Sec-Fetch-Mode': 'navigate',
    'X-Youtube-Client-Name': '5',
    'X-Youtube-Client-Version': '19.09.3',
    'Origin': 'https://www.youtube.com',
}
params = {
    'key': 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc',
    'prettyPrint': 'false',
}

@click.group()
def Video():
    pass

@Video.command()
@click.option("--link", "-L", type=str, required=True, help="Enter your Youtube Link")
@click.option("--quality", "-Q", type=str, required=True, help="Enter your Video Quality")
@click.option("-ss", type=str, required=True, help="Enter input time")
@click.option("-to", type=str, required=True, help="Enter output time")
@click.option("--output", "-O", type=str, required=True, help="Enter Output filename")
def yt(link, quality, output, ss, to):
    """Download youtube videos"""
    if "?" in link:
        video_id = link.split("?")[0].split("/")[-1]
    else:
        video_id = link.split("/")[-1]
    json_data = {
    'context': {
        'client': {
            'clientName': 'IOS',
            'clientVersion': '19.09.3',
            'deviceModel': 'iPhone14,3',
            'userAgent': 'com.google.ios.youtube/19.09.3 (iPhone14,3; U; CPU iOS 15_6 like Mac OS X)',
            'hl': 'en',
            'timeZone': 'UTC',
            'utcOffsetMinutes': 0,
        },
    },
    'videoId': f"{video_id}",
    'playbackContext': {
        'contentPlaybackContext': {
            'html5Preference': 'HTML5_PREF_WANTS',
        },
    },
    'contentCheckOk': True,
    'racyCheckOk': True,
}
    response = requests.post(
            'https://www.youtube.com/youtubei/v1/player',
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data,
    )
    Links = [
    ]

    [
        (
            Links.append({"Audio": __['url']}) if 'AUDIO_QUALITY_MEDIUM' in str(__) else None,
            Links.append({"Video": __['url']}) if f'{quality}' in str(__) and "mp4" in str(__) else None
        )
        for __ in json.loads(response.text)['streamingData']['adaptiveFormats']
    ]

    video = Links[0]['Video']
    audio = Links[1]['Audio']
    os.system(f"ffmpeg -ss {ss} -to {to} -i \"{video}\" -ss {ss} -to {to} -i \"{audio}\" -c copy {output}")
if __name__ == '__main__':
    try:
        yt()
    except (KeyError, NameError):
        os.system("Quality Not Available")
