from yt_dlp import YoutubeDL
import siaskynet as skynet
import argparse
import urllib.parse
import sys

def main():
    portal_url = 'https://siasky.net'
    parser = argparse.ArgumentParser() 
    parser.add_argument('url', help='ダウンロード対象のurl')
    parser.add_argument('-p','--portalurl', help='使用するポータルのurl, 指定しない場合は https://siasky.net')
    args = parser.parse_args()

    if args.portalurl:
        portal_url = args.portalurl

    ydl_opts = {'outtmpl':'%(id)s_%(title)s.%(ext)s'}
    url = args.url
    title = ''
    id = ''
    ext = ''
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url)
            title = info['title']
            id = info['id']
            ext = info['ext']
        print('Download completed')
        upload_file = f'{id}_{title}.{ext}'

        print(f"Uploading video: {upload_file}")
        client = skynet.SkynetClient(portal_url)
        link = client.upload_file(path=upload_file)
        print('Upload completed')
        print(urllib.parse.urljoin(portal_url,link[6:]))
    except Exception as e:
        sys.exit(e)

if __name__ == "__main__":
    main()