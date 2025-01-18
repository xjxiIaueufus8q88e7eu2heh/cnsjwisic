import requests
import json
import os
import click

cookies = {
    'ST-1ogbdv2': 'csn=suQgQRtQ8FQ1rGmy&itct=CPwBEPxaIhMIusj6kvD7igMVrVSdCR2WSy_2MgpnLWhpZ2gtcmVjWg9GRXdoYXRfdG9fd2F0Y2iaAQYQjh4YngE%3D',
    'SIDCC': 'AKEyXzVD8dAPhOtBN1NoFL-FkUBL-x-HP9vuDBtBYeIyDA7NX3uAHoE0wOvqacil7tthedq3Aw',
    '__Secure-1PSIDCC': 'AKEyXzWubPGfj3X3oUYiJlpaC8L8lNCmDBIljjBLf3hT1jTezQXxRokdwwHKS_BR-6BtWfFZ',
    '__Secure-3PSIDCC': 'AKEyXzUbvGlb5vaPRQ4Dm3LpYdw_7T_cm1EvYAu0cXRoYSaPZl21wIHGoWQOiXDbUdcj1V8Ejw',
    'PREF': 'f6=40000000&tz=Asia.Calcutta',
    'VISITOR_INFO1_LIVE': 'JbymmX3cjqw',
    'VISITOR_PRIVACY_METADATA': 'CgJJThIEGgAgLA%3D%3D',
    'APISID': 'XUk6Yz1CdpY05NHc/AtKNQ0go_MSzsW8hL',
    'HSID': 'A9aIpDwNKXwR7TSmE',
    'LOGIN_INFO': 'AFmmF2swRQIhALJ7me90CiwhHBorYw4-RPAcFxwRSHZ9_wlQ7v9VH21JAiAUUEb26qzapVB9Lmvd1Qb69afXcc3ZMNW_gKbfZvo7fA:QUQ3MjNmeVJ0OEY0d29ES1BHMXhqdHdDcklBX29tMEIzbmwwRnhnWGI5ZEhLRC1ZMV9maGNVZnVzd01fVkl3SXZBU0hyaVBkLWgwLWp1TE1aZ2F5TllmSVEzTmRPcjJ3YjRaYnZMa3ZtSFZnNFJacnBtM2VCQWZwRHA3enpCTGN1UUNFczItcVlXWEo0d0lBTVE2TE9YbU1vajJPMVZzNWZR',
    'SAPISID': 'MRbTjuXLm7oVGXww/Aa1QTwfjQvIpkjEmE',
    'SID': 'g.a000sgi68DwTx-omqUQJB0Rwf1Ce46bJWNhUTmY8MCZU2SatNX1oD2vl3hNhZ6jzY1PUq4PK1QACgYKAYQSARASFQHGX2Mi8-y1TVBi0UaByXFqs7xVrhoVAUF8yKq-IiIdkgw5xLLeSNuXb5L20076',
    'SSID': 'ALDgFNJTxsK5DkcSH',
    '__Secure-1PAPISID': 'MRbTjuXLm7oVGXww/Aa1QTwfjQvIpkjEmE',
    '__Secure-1PSID': 'g.a000sgi68DwTx-omqUQJB0Rwf1Ce46bJWNhUTmY8MCZU2SatNX1oa837-d06PUTEX-nhHaJpPgACgYKARYSARASFQHGX2Mi08-3-Eu6Dl3NNcg49C8rMxoVAUF8yKreQi01sN4w6Yfxarsri9OT0076',
    '__Secure-1PSIDTS': 'sidts-CjEBmiPuTeqD7J1zhTBbcA5qAM9sHtP_Yb5d_U_ItaTcHyVMRvJAXlb01TCuVdkImqK5EAA',
    '__Secure-3PAPISID': 'MRbTjuXLm7oVGXww/Aa1QTwfjQvIpkjEmE',
    '__Secure-3PSID': 'g.a000sgi68DwTx-omqUQJB0Rwf1Ce46bJWNhUTmY8MCZU2SatNX1ohy_v2mc-jNhDrQ7KzjnT0gACgYKAUoSARASFQHGX2MiO5SxOIjZINWv_mmoxHP3DhoVAUF8yKoy1gbW_EfG7-n387dztuMB0076',
    '__Secure-3PSIDTS': 'sidts-CjEBmiPuTeqD7J1zhTBbcA5qAM9sHtP_Yb5d_U_ItaTcHyVMRvJAXlb01TCuVdkImqK5EAA',
    'YSC': 'Hlb1AMowAYw',
    '__Secure-ROLLOUT_TOKEN': 'CPqA3Nv80OSIExDkideA2NuKAxj6wsa37fuKAw%3D%3D',
}
headers = {
    'content-type': 'application/json',
    'accept': '*/*',
    'x-youtube-client-version': '2.20250114.08.00',
    'authorization': 'SAPISIDHASH 1737086701_4f8b24316079b84b5119dbb2b790da7b3fff72e5_u SAPISID1PHASH 1737086701_4f8b24316079b84b5119dbb2b790da7b3fff72e5_u SAPISID3PHASH 1737086701_4f8b24316079b84b5119dbb2b790da7b3fff72e5_u',
    'sec-fetch-site': 'same-origin',
    'x-youtube-client-name': '2',
    'x-origin': 'https://m.youtube.com',
    'sec-fetch-mode': 'same-origin',
    'x-goog-authuser': '1',
    'origin': 'https://m.youtube.com',
    'user-agent': 'Mozilla/5.0 (iPad; CPU OS 18_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 Mobile/15E148 Safari/604.1',
    'referer': 'https://m.youtube.com/watch?v=E9mctvE_YS4',
    'x-goog-visitor-id': 'CgtKYnltbVgzY2pxdyjVrae8BjIKCgJJThIEGgAgLA%3D%3D',
    'sec-fetch-dest': 'empty',
    'x-youtube-bootstrap-logged-in': 'true',
    'accept-language': 'en-IN,en-GB;q=0.9,en;q=0.8',
    'priority': 'u=3, i',
}
params = {
    'prettyPrint': 'false',
}

@click.group()
def Video():
    pass

@Video.command()
@click.option("--link", "-L", type=str, required=True, help="Enter your Youtube Link")
@click.option("-ss", type=str, required=True, help="Enter input time")
@click.option("-res", type=str, required=True, help="Enter quality")
@click.option("-to", type=str, required=True, help="Enter output time")
@click.option("--output", "-O", type=str, required=True, help="Enter Output filename")
def yt(link, output, ss, to, res):
    """Download youtube videos"""
    if "?" in link:
        video_id = link.split("?")[0].split("/")[-1]
    else:
        video_id = link.split("/")[-1]
#        print(video_id, res)
    json_data = {
    'context': {
        'client': {
            'hl': 'en-GB',
            'gl': 'IN',
            'remoteHost': '2406:7400:ca:fecb:3584:a441:2e50:12f',
            'deviceMake': 'Apple',
            'deviceModel': 'iPad',
            'visitorData': 'CgtKYnltbVgzY2pxdyjVrae8BjIKCgJJThIEGgAgLA%3D%3D',
            'userAgent': 'Mozilla/5.0 (iPad; CPU OS 18_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 Mobile/15E148 Safari/604.1,gzip(gfe)',
            'clientName': 'MWEB',
            'clientVersion': '2.20250114.08.00',
            'osName': 'iPad',
            'osVersion': '18_1_1',
            'originalUrl': f"https://m.youtube.com/watch?v={video_id}",
            'playerType': 'UNIPLAYER',
            'screenPixelDensity': 2,
            'platform': 'TABLET',
            'clientFormFactor': 'LARGE_FORM_FACTOR',
            'configInfo': {
                'appInstallData': 'CNWtp7wGEK7BzhwQh6zOHBCIh7AFEIfUrwUQhL3OHBDBws4cENGUzhwQjtexBRDZqs4cEIzQsQUQ_LLOHBDh7LAFEL22rgUQ0I2wBRCT0rAFEKKjzhwQv8LOHBCHw7EFEIqhsQUQppOxBRCU_rAFEMn3rwUQvZmwBRDerbEFEK_CzhwQwavOHBCSuM4cEKuezhwQ3rzOHBDrws4cENzIzhwQrKexBRCk9a4FENnBsQUQj8OxBRD2q7AFEIvUsQUQjdSxBRCO0LEFEIjjrwUQvoqwBRDT4a8FEKiasAUQyNixBRDBzbEFEMK3zhwQgYO4IhCNzLAFEMnmsAUQ9oaxBRD6uM4cELfvrwUQytixBRCe0LAFEIHDsQUQt6TOHBCSy7EFEJS7zhwQ6-j-EhDOr68FEMrUsQUQ56jOHBC8ss4cEOeazhwQ37TOHBCB1rEFEMTYsQUQmZixBRDlubEFEIPDsQUQwLfOHBDtoc4cEJnS_xIQzN-uBRDTuc4cEPirsQUQ7bmxBRDG2LEFEJmNsQUQhaexBRCazrEFELfq_hIQz7LOHBDqw68FEObPsQUQotSxBRDDu84cEPCcsAUQs8DOHBDhvM4cEN3o_xIqKENBTVNHaFVSb0wyd0ROSGtCdUx3LVF1ZTRRYVJoZ2JJZktQX0JCMEg%3D',
                'coldConfigData': 'CNWtp7wGGjJBT2pGb3gzMWF5dkg2YVNldlctcWI2Z3IxdldXbDVsNThLREMzM0ZzeWx4VUZjNUltUSIyQU9qRm94MXU3STRUb3Z3QUpSM0F0ZDZ6U0k4UGlCNnZMLXk1QkhlRHVLUl83QW13VkE%3D',
                'coldHashData': 'CNWtp7wGEhQxNjE1MjE0MzQ5NTI2NTA3ODQzMBjVrae8BjIyQU9qRm94MzFheXZINmFTZXZXLXFiNmdyMXZXV2w1bDU4S0RDMzNGc3lseFVGYzVJbVE6MkFPakZveDF1N0k0VG92d0FKUjNBdGQ2elNJOFBpQjZ2TC15NUJIZUR1S1JfN0Ftd1ZB',
                'hotHashData': 'CNWtp7wGEhQxODE4OTA5NTk4NzQ2ODYzMTYwNxjVrae8BjIyQU9qRm94MzFheXZINmFTZXZXLXFiNmdyMXZXV2w1bDU4S0RDMzNGc3lseFVGYzVJbVE6MkFPakZveDF1N0k0VG92d0FKUjNBdGQ2elNJOFBpQjZ2TC15NUJIZUR1S1JfN0Ftd1ZB',
            },
            'screenDensityFloat': 2,
            'userInterfaceTheme': 'USER_INTERFACE_THEME_DARK',
            'timeZone': 'Asia/Calcutta',
            'browserName': 'Safari Mobile',
            'browserVersion': '18.1.1.15E148',
            'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'deviceExperimentId': 'ChxOelEyTURjek1EUTJPREl3TlRjeE16QTBPQT09ENWtp7wGGNWtp7wG',
            'rolloutToken': 'CPqA3Nv80OSIExDkideA2NuKAxj6wsa37fuKAw%3D%3D',
            'screenWidthPoints': 704,
            'screenHeightPoints': 619,
            'utcOffsetMinutes': 330,
            'clientScreen': 'WATCH',
            'mainAppWebInfo': {
                'graftUrl': f"/watch?v={video_id}",
                'webDisplayMode': 'WEB_DISPLAY_MODE_BROWSER',
                'isWebNativeShareAvailable': True,
            },
        },
        'user': {
            'lockedSafetyMode': False,
        },
        'request': {
            'useSsl': True,
            'internalExperimentFlags': [],
            'consistencyTokenJars': [],
        },
        'clickTracking': {
            'clickTrackingParams': 'CPwBEPxaIhMIusj6kvD7igMVrVSdCR2WSy_2MgpnLWhpZ2gtcmVjWg9GRXdoYXRfdG9fd2F0Y2iaAQYQjh4YngE=',
        },
    },
    'videoId': f"{video_id}",
    'playbackContext': {
        'contentPlaybackContext': {
            'currentUrl': f"/watch?v={video_id}",
            'vis': 0,
            'splay': False,
            'autoCaptionsDefaultOn': False,
            'autonavState': 'STATE_NONE',
            'html5Preference': 'HTML5_PREF_WANTS',
            'signatureTimestamp': 20102,
            'referer': 'https://m.youtube.com/',
            'lactMilliseconds': '-1',
            'watchAmbientModeContext': {
                'watchAmbientModeEnabled': True,
            },
        },
    },
    'racyCheckOk': False,
    'contentCheckOk': False,
    'serviceIntegrityDimensions': {
        'poToken': 'MlOJvu5bxinodImC2_aabxpJSxpJL3Lruc7pciZYMD7ZrroOnLnuW-F7ODOmElAWQJa-LoAf25DpJI7L6Q3tsNNtcusd-LAAe1YwbGh7IlDiV1XYFw==',
    },
}
#    print(json.dumps(json_data, indent=4))
    response = requests.post(
            'https://m.youtube.com/youtubei/v1/player?prettyPrint=false',
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data
    )
    hls = json.loads(response.text)['streamingData']["hlsManifestUrl"]
    os.system(f"ffmpeg -ss {ss} -to {to} -i \"{hls}\" -c copy {output}")
if __name__ == '__main__':
    try:
        yt()
    except (KeyError, NameError):
        os.system("Quality Not Available")
