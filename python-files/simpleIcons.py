from simpleicons.all import icons
import os

if os.path.exists("allBrandInSimpleIcons.txt"):
    with open("allBrandInSimpleIcons.txt", "r") as f:
        firstLetter = f.readline().strip()[0]
        dosya = open(f"brandsdot.md", "w")
        dosya.write(
            f"<table><tr><th>Brand</th><th>Flat Icon</th><th>Plastic Icon/th><th>Squared Bold Icon</th><th>Squared Icon</th><th>Markdown </th></tr>")
        for line in f:
            if firstLetter.upper() != line[0].upper():
                dosya.write("</table></details>")
                dosya.close()
                dosya = open(f"brands{line[0].upper()}.md", "w")
                firstLetter = line[0]
                dosya.write(
                    f"<table><tr><th>Brand</th><th>Flat Icon</th><th>Plastic Icon/th><th>Squared Bold Icon</th><th>Squared Icon</th><th>Markdown </th></tr>")
            try:
                icon = icons.get(line.strip())
                dosya.write("<tr>"
                            + f"<td>{icon.title}</td>"
                            + f"<td><img src='https://img.shields.io/badge/{icon.slug}-{icon.hex}.svg?style=flat&logo={icon.slug}&logoColor=white' /></td>"
                            + f"<td><img src='https://img.shields.io/badge/{icon.slug}-{icon.hex}.svg?style=plastic&logo={icon.slug}&logoColor=white' /></td>"
                            + f"<td><img src='https://img.shields.io/badge/{icon.slug}-{icon.hex}.svg?style=for-the-badge&logo={icon.slug}&logoColor=white' /></td>"
                            + f"<td><img src='https://img.shields.io/badge/{icon.slug}-{icon.hex}.svg?style=flat-square&logo={icon.slug}&logoColor=white' /></td>"
                            + f"<td>![{icon.title}](https://img.shields.io/badge/{icon.slug}-{icon.hex}.svg?style=[style_name]&logo={icon.slug}&logoColor=white)</td>"
                            + "</tr>"
                            + "\n"
                            )
            except:
                pass
dosya.write("</table>")

dosya.close()
