import requests

with open("sources.txt","r",encoding="utf-8") as f:
    urls=[i.strip() for i in f if i.strip()]

result="#EXTM3U\n"

for url in urls:
    try:
        print("Downloading:",url)
        txt=requests.get(url,timeout=20).text
        lines=txt.splitlines()

        if lines and lines[0].startswith("#EXTM3U"):
            lines=lines[1:]

        result+="\n".join(lines)+"\n"

    except Exception as e:
        print(e)

with open("iptv.m3u","w",encoding="utf-8") as f:
    f.write(result)
