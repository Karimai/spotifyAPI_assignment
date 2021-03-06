import json
import os
import webbrowser
import getopt
import sys
import requests


def usage():
    print("main.py -i client_id -s client_secret")


if __name__ == "__main__":
    output_file = "result.html"
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:s:o:", ["help", "client_id", "client_secret"])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-i", "--client_id"):
            client_id = a
        elif o in ("-s", "--client_secret"):
            client_secret = a
        elif o in ("-o",):
            if a != "":
                output_file = a
        else:
            assert False, "unhandled option"
    body_params = {'grant_type': 'client_credentials'}
    url = 'https://accounts.spotify.com/api/token'
    response = requests.post(url, data=body_params, auth=(client_id, client_secret))

    access_token = json.loads(response.content.decode('UTF-8'))["access_token"]

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}',
    }
    out_file = "<table>\n<tbody>\n"
    out_file += "    <tr>\n"
    out_file += f"    <td><b>title</b></td>\n"
    out_file += f"    <td><b>name</b></td>\n"
    out_file += f"    <td><b>release_date</b></td>\n"
    out_file += "    </tr>\n"
    tracks = ""
    with open("./tracks.json") as fd:
        tracks = json.load(fd)
    results = []
    for track in tracks:
        res = requests.get(f'https://api.spotify.com/v1/tracks/{track}', headers=headers)
        jres = res.json()
        results.append([jres["album"]["name"],
                        jres["album"]["artists"][0]["name"],
                        jres["album"]["release_date"]])
    sorted_results = sorted(results, key=lambda x: x[2])
    for items in sorted_results:
        out_file += "    <tr>\n"
        for item in items:
            out_file += f"    <td>{item}</td>\n"
        out_file += "    </tr>\n"

    out_file += "</table>\n</tbody>\n"
    with open(output_file, "w") as res_fd:
        res_fd.write(out_file)

    webbrowser.open('file://' + os.path.realpath(output_file))
