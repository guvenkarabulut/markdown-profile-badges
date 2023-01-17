from simpleicons.all import icons
import os

dosya = open("brandAndIcons.md", "w")

dosya.write(
    "| Brand | Flat Icon | Plastic Icon | Squared Bold Icon | Squared Icon | Markdown \n")

dosya.write("| --- | --- | --- | --- | --- | --- | \n")
if os.path.exists("allBrandInSimpleIcons.txt"):
    with open("allBrandInSimpleIcons.txt", "r") as f:
        for line in f:
            try:
                icon = icons.get(line.strip())
                dosya.write(f"| {icon.title} | ")
                dosya.write
                dosya.write(
                    f"![{icon.title}](https://img.shields.io/badge/{icon.slug}-{icon.hex}.svg?style=flat&logo={icon.slug}&logoColor=white )|"
                )
                dosya.write(
                    f"![{icon.title}](https://img.shields.io/badge/{icon.slug}-{icon.hex}.svg?style=plastic&logo={icon.slug}&logoColor=white&)|"
                )
                dosya.write(
                    f"![{icon.title}](https://img.shields.io/badge/{icon.slug}-{icon.hex}.svg?style=for-the-badge&logo={icon.slug}&logoColor=white)|"
                )
                dosya.write(
                    f"![{icon.title}](https://img.shields.io/badge/{icon.slug}-{icon.hex}.svg?style=flat-square&logo={icon.slug}&logoColor=white)|"
                )
                dosya.write(
                    f"```![{icon.title}](https://img.shields.io/badge/{icon.slug}-{icon.hex}.svg?style=<STYLE_NAME>&logo={icon.slug}&logoColor=white)```|"
                )
                dosya.write("\n")
            except:
                pass
dosya.close()
