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
                }
                details {
                    padding: 0.2em;
                    font-size:2em; 
                }
                iframe { 
                    width: 100%;
                    height: 400px;
                }
                .row {
                    display: flex;
                    justify-content: center;
                    flex-direction: row;
                    flex-wrap: wrap;
                    width: 100%;
                }
                @media only screen and (max-width: 1000px) {
                    iframe { 
                        width: 100%;
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
                 <details>
                 <summary>{name}</summary>
                 <div class="row">
                 """
        for m, c in zip(ms, cs):
            html += f"""
                       <div style="padding: 10px;">
                           <!--<iframe style="height:100%;" data-src="{m}"></iframe>-->
                           <iframe class="column" data-src="{c}"></iframe>
                       </div>
                       <br>
                     """
        html += """
                </div>
                </details>
                <hr>
                """

    html += """
                </div>
                <script>
                  document.querySelectorAll('details').forEach(det => {
                    det.addEventListener('toggle', () => {
                      const iframes = det.querySelectorAll('iframe[data-src]');
                      if (det.open) {
                        iframes.forEach(ifr => {
                          ifr.src = ifr.dataset.src;
                        });
                      } else {
                        // Optionally clear src when closing to stop playback
                        iframes.forEach(ifr => {
                          ifr.src = '';
                        });
                      }
                    });
                  });
                </script>
            </body>
            </html>
    """
    print(html)

if __name__ == "__main__":
    main()

