import re

from manc import Spider

s = Spider()


def is_living(live_url):
    r1 = s.get(live_url, cookies={"__ac_nonce": "..."})
    match_list = re.findall(r'"roomId\\":\\"(\d+)\\",', r1.text)
    room_id = match_list[0]
    ttwid = r1.cookies.get('ttwid')

    live_id = live_url.split('/')[-1]
    url = "https://live.douyin.com/webcast/room/web/enter/"
    params = {
        "aid": "6383",
        "app_name": "douyin_web",
        "live_id": "1",
        "device_platform": "web",
        "language": "zh-CN",
        "enter_from": "page_refresh",
        "cookie_enabled": "true",
        "screen_width": "1920",
        "screen_height": "1080",
        "browser_language": "zh-CN",
        "browser_platform": "Win32",
        "browser_name": "Edge",
        "browser_version": "131.0.0.0",
        "web_rid": live_id,
        "room_id_str": room_id,
        "enter_source": "",
        "is_need_double_stream": "false",
        "insert_task_id": "",
        "live_reason": "",
    }
    r2 = s.get(url, params=params, cookies={"ttwid": ttwid})
    jsonData = r2.json()
    room_status = jsonData["data"]["room_status"]
    return True if room_status == 0 else False


if __name__ == '__main__':
    url = "https://live.douyin.com/646454278948"  # 抖音【与辉同行】直播间
    status = is_living(url)
    print(status)
