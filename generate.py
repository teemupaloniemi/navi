#!/usr/bin/python3
def get_urls(map_codes, name_codes):
    map_url = lambda code : f"https://navi.jyu.fi/space/{code}"
    calendar_url = lambda code : f"https://kovs-calendar.app.jyu.fi/room/{code}"
    map_urls = []
    cal_urls = []
    for map_code, name_code in zip(map_codes, name_codes):
        map_urls.append(map_url(map_code))
        cal_urls.append(calendar_url(name_code))
    return map_urls, cal_urls

def main():

    lähde = [["m3406546", "m3406547", "m3406548", "m3406549", "m3406550", "m3406453", "m3406452", "m3406451", "m3406450"],
             ["BP 45.2" , "BP 55.2" , "BP 55.1" , "BYP 45.4", "BYP 45.3", "BYP 45.2", "BYP 45.3", "BYP 45.4", "BYP 45.5"]]
    agora = [["m2137966"       , "m2137961"       ],
             ["Ag B301"        , "Ag B201"        ]]

    buildings = [["Lähde", lähde], ["Agora", agora]]

    html = """
           <!DOCTYPE html>
	       <html>
	       <head>
               <meta charset="UTF-8">
           </head>
           <style>
                body {
                    font-family: monospace, sans-serif;
                    background: #f1eee5;
                    margin-left: 0.5em;
                    margin-right: 0.5em;
                }
                details {
                    padding: 1em;
                    background: rgba(0,0,0,0.1);
                    border-radius: 15px;
                }
                @media only screen and (max-width: 900px) {
                  body {
                    margin-left: 10em;
                    margin-right: 10em;
                  }
                }
           </style>
           <body>
               <div style="width:100%; height: 100vh;">
            """
    for building in buildings:
        name = building[0]
        ms, cs = get_urls(building[1][0], building[1][1])
        html += f"""
                <h1>{name}</h1>
                <details>
                """
        for m, c in zip(ms, cs):
            html += f"""
                       <div style="display:flex; width:100%; height:300px;">
	                       <iframe style="margin-left: 1em; width:50%; height:100%;" src="{m}"></iframe>
	                       <iframe style="margin-right: 1em; width:50%; height:100%;" src="{c}"></iframe>
	                   </div><br>
	                  """
        html += """
                </details>
                <hr>
                """
    html += """
                </div>
            </body>
            </html>
            """
    print(html)

if __name__ == "__main__":
    main()

